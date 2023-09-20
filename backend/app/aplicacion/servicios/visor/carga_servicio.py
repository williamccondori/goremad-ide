import os
from typing import List
from zipfile import ZipFile

import geopandas as gpd
from fastapi import UploadFile
from starlette import status

from app.aplicacion.dtos.visor.obtener_geometria_carga_response import ObtenerGeometriaCargaResponse
from app.dominio.excepciones.aplicacion_exception import AplicacionException

# Lista de extensiones permitidas
EXTENSIONES_PERMITIDAS: List[str] = ['.shp', '.kml', '.kmz', '.geojson']


class CargaServicio:
    @staticmethod
    def verificar_archivo(archivo) -> str:
        extension = os.path.splitext(archivo.filename)[1].lower()
        if extension not in ['.zip', '.kml', '.kmz', '.geojson']:
            raise AplicacionException("Formato de archivo no permitido", status.HTTP_400_BAD_REQUEST)

        # Verificar que no pese más de 5 MB.
        if len(archivo.file.read()) > 5242880:
            raise AplicacionException("El archivo no debe pesar más de 5 MB", status.HTTP_400_BAD_REQUEST)

        # Verificar que si es un archivo ZIP, contenga al menos un archivo con una extensión permitida.
        if extension == '.zip':
            with ZipFile(archivo.file) as archivo_zip:
                nombres = archivo_zip.namelist()
                nombres = [nombre.lower() for nombre in nombres]
                if not any(os.path.splitext(nombre)[1] in EXTENSIONES_PERMITIDAS for nombre in nombres):
                    raise AplicacionException(
                        "El archivo ZIP debe contener al menos un archivo con una extensión permitida.",
                        status.HTTP_400_BAD_REQUEST)

        archivo.file.seek(0)

        return extension

    async def obtener_geometria(self, archivo: UploadFile) -> ObtenerGeometriaCargaResponse:
        extension = self.verificar_archivo(archivo)
        try:
            # Se lee el archivo.
            gdf = gpd.read_file(archivo.file)
            archivo.file.close()
            # Se transforma a CRS 4326 para que sea compatible con el mapa.
            gdf = gdf.to_crs(epsg=4326)
            # Vaciado del archivo en memoria.
            return ObtenerGeometriaCargaResponse(
                nombre=archivo.filename,
                extension=extension,
                cantidad_registros=len(gdf),
                geojson=gdf.to_json(),
                tipo_geometria=gdf.geom_type[0]
            )
        except Exception as e:
            raise AplicacionException(f"Error al leer el archivo {e}", status.HTTP_400_BAD_REQUEST)
