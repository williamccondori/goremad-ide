from datetime import datetime
from uuid import uuid4

from fastapi import Depends

from app.aplicacion.dtos.visor.buscar_imagen_satelital_request import BuscarImagenSatelitalRequest
from app.aplicacion.dtos.visor.buscar_imagen_satelital_response import BuscarImagenSatelitalResponse
from app.aplicacion.dtos.visor.capa_response import CapaResponse
from app.aplicacion.dtos.visor.obtener_capas_imagen_satelital_request import ObtenerCapasImagenSatelitalRequest
from app.aplicacion.dtos.visor.obtener_capas_imagen_satelital_response import ObtenerCapasImagenSatelitalResponse, \
    ImagenSatelitalPadreResponse
from app.aplicacion.utilidades import constantes
from app.aplicacion.utilidades.wms import obtener_url_leyenda
from app.dominio.entidades.compartido import base_entidad
from app.dominio.entidades.imagen_satelital_entidad import ImagenSatelitalEntidad
from app.dominio.repositorios.imagen_satelital_repositorio import IImagenSatelitalRepositorio
from app.infraestructura.mongo_db.repositorios.imagen_satelital_repositorio import ImagenSatelitalRepositorio
from app.settings import settings


class ImagenSatelitalServicio:
    def __init__(
            self,
            imagen_satelital_repositorio: IImagenSatelitalRepositorio = Depends(ImagenSatelitalRepositorio)
    ):
        self._imagen_satelital_repositorio = imagen_satelital_repositorio

    async def buscar(self, request: BuscarImagenSatelitalRequest) -> list[BuscarImagenSatelitalResponse]:
        filtros = {
            "estado": base_entidad.ESTADO_ACTIVO
        }
        if request.identificador:
            filtros["identificador"] = request.identificador
        else:
            # Se transforma a ISO para que el filtro funcione correctamente.
            fecha_inicio = datetime(
                request.fecha_inicio.year,
                request.fecha_inicio.month,
                request.fecha_inicio.day, 0, 0, 0
            )
            fecha_fin = datetime(
                request.fecha_fin.year,
                request.fecha_fin.month,
                request.fecha_fin.day, 23, 59, 59
            )
            filtros["fecha"] = {
                "$lt": fecha_fin,
                "$gte": fecha_inicio
            }
        imagenes_satelitales: list[ImagenSatelitalEntidad] = await self._imagen_satelital_repositorio.obtener_todos(
            filtros
        )
        return [
            BuscarImagenSatelitalResponse(
                **imagen_satelital.dict()
            ) for imagen_satelital in imagenes_satelitales
        ]

    async def obtener_capas(self, request: ObtenerCapasImagenSatelitalRequest) -> ObtenerCapasImagenSatelitalResponse:
        imagen_satelital: ImagenSatelitalEntidad = await self._imagen_satelital_repositorio.obtener_por_id(
            request.id
        )
        capas: list[CapaResponse] = []
        variaciones = ["RGB", "NDVI", "NDWI"]
        variaciones_identificadores = {}
        for variacion in variaciones:
            capa = f"{imagen_satelital.identificador}_{variacion}"
            capa_id: str = str(uuid4())
            variaciones_identificadores[variacion] = capa_id
            capas.append(CapaResponse(
                id=capa_id,
                servicio_id=imagen_satelital.id,
                servicio_titulo=imagen_satelital.identificador,
                nombre=capa,
                titulo=f"[{variacion}] {imagen_satelital.identificador}",
                url=f"{settings.GEOSERVER_URL_CLIENTE}/{constantes.ESPACIO_TRABAJO_IMAGENES_SATELITALES}/wms",
                url_leyenda=obtener_url_leyenda(settings.GEOSERVER_URL_CLIENTE, capa),
                atribucion="",
                cuadro_delimitador=[],
                grupo_capa_id=None,
                transparencia=1
            ))
        return ObtenerCapasImagenSatelitalResponse(
            imagen_satelital=ImagenSatelitalPadreResponse(
                id=imagen_satelital.id,
                identificador=imagen_satelital.identificador,
                descripcion=imagen_satelital.descripcion,
                rgb=variaciones_identificadores["RGB"],
                ndvi=variaciones_identificadores["NDVI"],
                ndwi=variaciones_identificadores["NDWI"]
            ),
            capas=capas
        )
