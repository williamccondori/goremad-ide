import json
import os
import shutil
import zipfile
from datetime import datetime, date, timedelta

import geopandas as gpd
import numpy as np
import rasterio
from fastapi import Depends
from geo.Geoserver import Geoserver  # noqa
from rasterio.mask import mask
from sentinelsat import SentinelAPI, geojson_to_wkt

from app.aplicacion.utilidades import constantes
from app.dominio.entidades import programacion_entidad
from app.dominio.entidades.compartido import base_entidad
from app.dominio.entidades.imagen_satelital_entidad import ImagenSatelitalEntidad
from app.dominio.entidades.programacion_entidad import ProgramacionEntidad
from app.dominio.repositorios.imagen_satelital_repositorio import IImagenSatelitalRepositorio
from app.dominio.repositorios.programacion_repositorio import IProgramacionRepositorio
from app.infraestructura.mongo_db.repositorios.imagen_satelital_repositorio import ImagenSatelitalRepositorio
from app.infraestructura.mongo_db.repositorios.programacion_repositorio import ProgramacionRepositorio
from app.settings import settings

GEOJSON_ARCHIVO = 'mdd.geojson'


class ImagenSatelitalServicio:
    def __init__(self,
                 programacion_repositorio: IProgramacionRepositorio = Depends(ProgramacionRepositorio),
                 imagen_satelital_repositorio: IImagenSatelitalRepositorio = Depends(ImagenSatelitalRepositorio)
                 ):
        self._programacion_repositorio = programacion_repositorio
        self._imagen_satelital_repositorio = imagen_satelital_repositorio

    async def descargar(self, programacion_id: str) -> None:
        programacion: ProgramacionEntidad = await self._programacion_repositorio.obtener_por_id(programacion_id)
        try:
            api = SentinelAPI(settings.SENTINEL_HUB_USUARIO, settings.SENTINEL_HUB_PASSWORD,
                              'https://scihub.copernicus.eu/dhus')
            with open(GEOJSON_ARCHIVO, 'r') as f:
                geojson_texto = f.read()
            geojson = geojson_to_wkt(
                json.loads(geojson_texto)
            )
            fecha_final = date.today()
            fecha_inicial = fecha_final - timedelta(days=10)
            productos = api.query(geojson,
                                  date=(fecha_inicial, fecha_final),
                                  platformname='Sentinel-2',
                                  processinglevel='Level-2A',
                                  cloudcoverpercentage=(0, 30)
                                  )
            api.download_all(list(productos), directory_path=settings.CARPETA_IMAGENES_SATELITALES)
            # Se procede con el procesamiento de las imagenes descargadas.
            for i in range(len(productos)):
                producto = list(productos.values())[i]
                identificador = producto['identifier']
                existe_imagen_satelital = await self._imagen_satelital_repositorio.verificar_existencia_por_filtros(
                    {"estado": base_entidad.ESTADO_ACTIVO, "identificador": identificador})
                if not existe_imagen_satelital:
                    print("Imagen satelital a descargar: ", identificador)
                    folder_salida = os.path.join(settings.CARPETA_IMAGENES_SATELITALES, identificador)
                    if not os.path.exists(folder_salida):
                        os.makedirs(folder_salida)
                    rutas = {}
                    archivo_zip = os.path.join(settings.CARPETA_IMAGENES_SATELITALES, identificador + '.zip')
                    with zipfile.ZipFile(archivo_zip, 'r') as zf:
                        for nombre in zf.namelist():
                            if nombre.endswith('_10m.jp2'):
                                banda = nombre.split('_')[-2]
                                rutas[banda] = zf.extract(nombre, folder_salida)
                    with rasterio.open(rutas['B04']) as red:
                        crs = red.crs
                        perfil = red.profile
                    # Se hace el corte de la imagen satelital.
                    gdf = gpd.read_file(GEOJSON_ARCHIVO)
                    gdf = gdf.to_crs(crs=crs)
                    geometria_mdd = gdf[['geometry']].values.flatten()
                    with rasterio.open(rutas['B04']) as red:
                        corte, out_transform = mask(red, geometria_mdd, crop=True)
                        corte_dimensiones = corte.shape
                        corte_transformaciones = out_transform
                        banda_roja = corte[0].astype('float32')
                    with rasterio.open(rutas['B03']) as green:
                        corte, _ = mask(green, geometria_mdd, crop=True)
                        banda_verde = corte[0].astype('float32')
                    with rasterio.open(rutas['B02']) as blue:
                        corte, _ = mask(blue, geometria_mdd, crop=True)
                        banda_azul = corte[0].astype('float32')
                    with rasterio.open(rutas['B08']) as nir:
                        corte, _ = mask(nir, geometria_mdd, crop=True)
                        banda_nir = corte[0].astype('float32')
                    # Se genera la imagen satelital RGB.
                    perfil.update(
                        count=3,
                        driver='GTiff',
                        dtype=rasterio.float32,
                        height=corte_dimensiones[1],
                        width=corte_dimensiones[2],
                        transform=corte_transformaciones
                    )
                    with rasterio.open(os.path.join(folder_salida, identificador + '_RGB.tif'), 'w',
                                       **perfil) as salida:
                        salida.write(banda_roja, 1)
                        salida.write(banda_azul, 3)
                        salida.write(banda_verde, 2)
                    perfil.update(
                        count=1,
                        driver='GTiff',
                        dtype=rasterio.float32
                    )
                    np.seterr(divide='ignore', invalid='ignore')
                    # Indice normalizado diferencial de vegetacion.
                    ndvi = np.divide((banda_nir - banda_roja), (banda_nir + banda_roja))
                    with rasterio.open(os.path.join(folder_salida, identificador + '_NDVI.tif'), 'w',
                                       **perfil) as salida:
                        salida.write(ndvi, 1)
                    # Indice normalizado diferencial de agua.
                    ndwi = np.divide((banda_verde - banda_nir), (banda_verde + banda_nir))
                    with rasterio.open(os.path.join(folder_salida, identificador + '_NDWI.tif'), 'w',
                                       **perfil) as salida:
                        salida.write(ndwi, 1)

                    ruta_temporal = os.path.join(folder_salida, identificador + '.SAFE')
                    if os.path.exists(ruta_temporal):
                        shutil.rmtree(ruta_temporal)

                    imagenes = ['RGB', 'NDVI', 'NDWI']
                    for imagen in imagenes:
                        geoserver = Geoserver(settings.GEOSERVER_URL, username=settings.GEOSERVER_USER,
                                              password=settings.GEOSERVER_PASSWORD)
                        nombre_capa: str = identificador + '_' + imagen
                        geoserver.create_coveragestore(
                            os.path.join(folder_salida, identificador + '_' + imagen + '.tif'),
                            constantes.ESPACIO_TRABAJO_IMAGENES_SATELITALES,
                            nombre_capa
                        )
                        geoserver.publish_style(
                            nombre_capa,
                            imagen,
                            constantes.ESPACIO_TRABAJO_IMAGENES_SATELITALES
                        )
                    print("Imagen satelital descargada: ", identificador)

                    imagen_satelital: ImagenSatelitalEntidad = ImagenSatelitalEntidad(
                        identificador=identificador,
                        identificador_sentinel_hub=producto["uuid"],
                        fecha=producto["generationdate"],
                        tamanio=producto["size"],
                        descripcion=producto["summary"],
                        coberturaAgua=producto["waterpercentage"],
                        coberturaNubosidad=producto["cloudcoverpercentage"],
                        coberturaVegetacion=producto["vegetationpercentage"],
                        metadatos=producto
                    )
                    imagen_satelital.registrar_creacion(programacion.usuario)
                    await self._imagen_satelital_repositorio.crear(imagen_satelital)

            programacion.estado_ejecucion = programacion_entidad.ESTADO_TERMINADO
            programacion.fecha_fin = datetime.now()
            programacion.registrar_actualizacion(programacion.usuario_creacion)
            await self._programacion_repositorio.actualizar(programacion_id, programacion)
        except Exception as e:
            print("Error al descargar imagen satelital", str(e))
            programacion.estado_ejecucion = programacion_entidad.ESTADO_ERROR
            programacion.fecha_fin = datetime.now()
            programacion.observaciones = str(e)
            programacion.registrar_actualizacion(programacion.usuario_creacion)
            await self._programacion_repositorio.actualizar(programacion_id, programacion)
