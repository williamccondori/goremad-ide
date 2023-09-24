import json
from datetime import datetime
from typing import Optional

from fastapi import Depends
from owslib.wfs import WebFeatureService

from app.aplicacion.dtos.visor.obtener_informacion_objeto_geografico_response import \
    ObtenerInformacionObjetoGeograficoResponse
from app.dependencies import registrar_repo_objeto_geografico, registrar_repo_objeto_geografico_geometria
from app.dominio.entidades.objeto_geografico_entidad import ObjetoGeograficoEntidad
from app.dominio.entidades.objeto_geografico_geometria_entidad import ObjetoGeograficoGeometriaEntidad
from app.dominio.excepciones.aplicacion_exception import AplicacionException
from app.dominio.repositorios.base_repositorio import IBaseRepositorio
from app.settings import settings

ESTILO_PREDETERMINADO = {
    "color": "#000000",
    "fillColor": "#333333",
    "fillOpacity": 0.5,
}

RANGO_ACTUALIZACION = 3600


class ObjetoGeograficoServicio:

    def __init__(self,
                 objeto_geografico_repositorio: IBaseRepositorio = Depends(registrar_repo_objeto_geografico),
                 objeto_geografico_geometria_repositorio: IBaseRepositorio = Depends(
                     registrar_repo_objeto_geografico_geometria)):
        self._objeto_geografico_repositorio = objeto_geografico_repositorio
        self._objeto_geografico_informacion_repositorio = objeto_geografico_geometria_repositorio

    async def obtener_objeto_geografico_por_id(self, objeto_geografico_id: str) -> ObjetoGeograficoEntidad:
        objeto_geografico: ObjetoGeograficoEntidad = await self._objeto_geografico_repositorio.obtener_por_id(
            objeto_geografico_id)
        if not objeto_geografico.esta_habilitado:
            raise AplicacionException("El objeto geográfico no está habilitado")
        return objeto_geografico

    @staticmethod
    async def obtener_geometria_desde_geoserver(
            objeto_geografico_nombre_geoserver: str) -> str:
        geoserver_host = settings.GEOSERVER_URL
        owslib_wfs = WebFeatureService(url=f"{geoserver_host}/geoserver/wfs", version="1.1.0")

        # Obtener la geometría sin propiedades.
        response = owslib_wfs.getfeature(
            typename=objeto_geografico_nombre_geoserver,
            outputFormat='application/json',
            srsname='EPSG:4326'
        )

        # Eliminar las propiedades de la geometría.
        geojson = json.loads(response.read())
        return json.dumps(geojson)

    async def obtener_geometria_desde_local(self, objeto_geografico_id: str) -> str:
        objeto_geografico_geometria: ObjetoGeograficoGeometriaEntidad = await (
            self._objeto_geografico_informacion_repositorio.obtener_por_filtros({
                "objeto_geografico_id": objeto_geografico_id
            })
        )
        return objeto_geografico_geometria.geometria

    async def obtener_informacion_objeto_geografico(self, objeto_geografico_id: str, incluir_propiedades: bool) \
            -> ObtenerInformacionObjetoGeograficoResponse:
        objeto_geografico: ObjetoGeograficoEntidad = await self.obtener_objeto_geografico_por_id(objeto_geografico_id)

        # Estlos.
        try:
            estilo_renderizado = json.loads(objeto_geografico.estilo)
            estilo = json.dumps(estilo_renderizado)
        except TypeError:
            estilo = json.dumps(ESTILO_PREDETERMINADO)

            # Geometría.
        fecha_actual = datetime.now()

        objeto_geografico_geometria: Optional[ObjetoGeograficoGeometriaEntidad] = await (
            self._objeto_geografico_informacion_repositorio.obtener_por_filtros({
                "objeto_geografico_id": objeto_geografico_id
            })
        )
        if not objeto_geografico_geometria:
            geometria = await self.obtener_geometria_desde_geoserver(objeto_geografico.nombre_geoserver)
            objeto_geografico_informacion = ObjetoGeograficoGeometriaEntidad(
                objeto_geografico_id=objeto_geografico_id,
                geometria=geometria,
                fecha_ultima_actualizacion=fecha_actual
            )
            await self._objeto_geografico_informacion_repositorio.crear(objeto_geografico_informacion)
        else:
            fecha_proxima_actualizacion = (
                    objeto_geografico_geometria.fecha_ultima_actualizacion.timestamp() + RANGO_ACTUALIZACION)
            if fecha_actual.timestamp() > fecha_proxima_actualizacion:
                geometria = await self.obtener_geometria_desde_geoserver(objeto_geografico.nombre_geoserver)
                objeto_geografico_geometria.geometria = geometria
                objeto_geografico_geometria.fecha_ultima_actualizacion = fecha_actual
                await self._objeto_geografico_informacion_repositorio.actualizar(
                    objeto_geografico_geometria.id, objeto_geografico_geometria)
            else:
                geometria = objeto_geografico_geometria.geometria

        if not incluir_propiedades:
            geojson = json.loads(geometria)
            for feature in geojson["features"]:
                feature["properties"] = {}
            geometria = json.dumps(geojson)

        return ObtenerInformacionObjetoGeograficoResponse(
            id=objeto_geografico.id,
            codigo=objeto_geografico.codigo,
            nombre=objeto_geografico.nombre,
            nombre_geoserver=objeto_geografico.nombre_geoserver,
            descripcion=objeto_geografico.descripcion,
            estilo=estilo,
            geometria=geometria
        )
