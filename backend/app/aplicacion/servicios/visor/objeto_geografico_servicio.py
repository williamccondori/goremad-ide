import json

from fastapi import Depends
from owslib.wfs import WebFeatureService

from app.aplicacion.dtos.visor.obtener_geometria_objeto_geografico_response import \
    ObtenerGeometriaObjetoGeograficoResponse
from app.dependencies import registrar_repo_objeto_geografico
from app.dominio.entidades.objeto_geografico_entidad import ObjetoGeograficoEntidad
from app.dominio.excepciones.aplicacion_exception import AplicacionException
from app.dominio.repositorios.base_repositorio import IBaseRepositorio
from app.settings import settings


class ObjetoGeograficoServicio:

    def __init__(self,
                 objeto_geografico_repositorio: IBaseRepositorio = Depends(registrar_repo_objeto_geografico)):
        self._objeto_geografico_repositorio = objeto_geografico_repositorio

    async def obtener_geometria(self, objeto_geografico_id: str) -> ObtenerGeometriaObjetoGeograficoResponse:
        objeto_geografico: ObjetoGeograficoEntidad = await self._objeto_geografico_repositorio.obtener_por_id(
            objeto_geografico_id)
        if not objeto_geografico.esta_habilitado:
            raise AplicacionException("El objeto geográfico no está habilitado")

        geoserver_host = settings.GEOSERVER_URL
        owslib_wfs = WebFeatureService(url=f"{geoserver_host}/geoserver/wfs", version="1.1.0")

        # Obtener la geometría sin propiedades.
        response = owslib_wfs.getfeature(
            typename=objeto_geografico.nombre_geoserver,
            outputFormat='application/json',
            srsname='EPSG:4326'
        )

        # Eliminar las propiedades de la geometría.
        geojson = json.loads(response.read())
        for feature in geojson["features"]:
            feature["properties"] = {}

        # Se valida la información del estilo.
        estilo_predeterminado = {
            "color": "#000000",
            "fillColor": "#333333",
        }
        try:
            estilo_renderizado = json.loads(objeto_geografico.estilo)
            estilo = json.dumps(estilo_renderizado)
        except TypeError:
            estilo = json.dumps(estilo_predeterminado)

        return ObtenerGeometriaObjetoGeograficoResponse(
            id=objeto_geografico.id,
            codigo=objeto_geografico.codigo,
            nombre=objeto_geografico.nombre,
            descripcion=objeto_geografico.descripcion,
            estilo=estilo,
            geometria=json.dumps(geojson)
        )
