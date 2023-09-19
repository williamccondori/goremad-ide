import json

from fastapi import Depends
from geo.Geoserver import Geoserver  # noqa
from starlette import status

from app.aplicacion.dtos.administrador.crear_publicacion_request import (
    CrearPublicacionRequest,
)
from app.aplicacion.dtos.administrador.obtener_todos_publicacion_response import (
    ObtenerTodosPublicacionResponse,
)
from app.aplicacion.utilidades import constantes
from app.dominio.entidades.compartido import base_entidad
from app.dominio.entidades.compartido.servicio_entidad import CapaEntidad
from app.dominio.entidades.publicacion_entidad import PublicacionEntidad
from app.dominio.excepciones.aplicacion_exception import AplicacionException
from app.dominio.repositorios.grupo_capa_repositorio import IGrupoCapaRepositorio
from app.dominio.repositorios.publicacion_repositorio import IPublicacionRepositorio
from app.infraestructura.mongo_db.repositorios.grupo_capa_repositorio import (
    GrupoCapaRepositorio,
)
from app.infraestructura.mongo_db.repositorios.publicacion_repositorio import (
    PublicacionRepositorio,
)
from app.settings import settings


class PublicacionServicio:
    def __init__(
        self,
        publicacion_repositorio: IPublicacionRepositorio = Depends(
            PublicacionRepositorio
        ),
        grupo_capa_repositorio: IGrupoCapaRepositorio = Depends(GrupoCapaRepositorio),
    ):
        self._publicacion_repositorio = publicacion_repositorio
        self._grupo_capa_repositorio = grupo_capa_repositorio

    async def validar_existencia_grupo_capa(self, grupo_capa_id):
        if grupo_capa_id == constantes.CADENA_VACIA:
            raise AplicacionException(
                "El grupo de capa no puede estar vacío (puede ser NULO)",
                status.HTTP_400_BAD_REQUEST,
            )
        if grupo_capa_id:
            existe_grupo_capa: bool = (
                await self._grupo_capa_repositorio.verificar_existencia(grupo_capa_id)
            )
            if not existe_grupo_capa:
                raise AplicacionException(
                    "El grupo de capa no existe", status.HTTP_404_NOT_FOUND
                )

    async def obtener_todos(self) -> list[ObtenerTodosPublicacionResponse]:
        """
        Obtiene todas las publicaciones activas.
        Returns:
            list[ObtenerTodosCapaBaseResponse]: Lista de publicaciones activas.
        """
        publicaciones: list[
            PublicacionEntidad
        ] = await self._publicacion_repositorio.obtener_todos(
            {"estado": base_entidad.ESTADO_ACTIVO}
        )
        return [
            ObtenerTodosPublicacionResponse(**publicacion.dict())
            for publicacion in publicaciones
        ]

    async def crear(
        self, request: CrearPublicacionRequest, usuario_auditoria_id: str
    ) -> str:
        """
        Crea una publicacion a partir de una capa de GeoServer.
        Args:
            request (CrearPublicacionRequest): Informacion de la publicacion.
            usuario_auditoria_id (str): Identificador del usuario que realiza la accion.
        Returns:
            str: Identificador de la publicacion creada.
        """
        # Se estandariza el nombre de la capa.
        nombre_capa = request.capa.strip()
        # nombre_capa = nombre_capa.lower()
        # Se verifica si ya existe la publicacion.
        existe: bool = (
            await self._publicacion_repositorio.verificar_existencia_por_filtros(
                {"estado": base_entidad.ESTADO_ACTIVO, "capa": nombre_capa}
            )
        )
        if existe:
            raise AplicacionException(
                "La capa ya se encuentra publicada", status.HTTP_400_BAD_REQUEST
            )
        await self.validar_existencia_grupo_capa(request.grupo_capa_id)
        # Buscar la informacion de la capa en GeoServer.
        geoserver = Geoserver(
            settings.GEOSERVER_URL,
            username=settings.GEOSERVER_USER,
            password=settings.GEOSERVER_PASSWORD,
        )
        # Se verifica si existe la capa en GeoServer.
        try:
            capa_geoserver = geoserver.get_layer(
                nombre_capa, workspace=request.espacio_trabajo
            )
        except Exception as excepcion:
            print(excepcion)
            raise AplicacionException(
                "La capa no existe en GeoServer", status.HTTP_404_NOT_FOUND
            )
        # Se genera el nombre de la capa.
        nombre_capa_geoserver = f"{request.espacio_trabajo}:{nombre_capa}"

        print(json.dumps(capa_geoserver))

        capa: CapaEntidad = CapaEntidad(
            nombre=nombre_capa_geoserver, titulo=request.titulo, cuadro_delimitador=[]
        )

        # Se procede con el registro de la publicacion.
        publicacion: PublicacionEntidad = PublicacionEntidad(
            url="",
            nombre="",
            atribucion="",
            grupo_capa_id=request.grupo_capa_id,
            capas=[capa],
            opacidad=1,
            es_consultable=request.es_consultable,
            esta_habilitado=request.esta_habilitado,
        )
        publicacion.registrar_creacion(usuario_auditoria_id)
        return await self._publicacion_repositorio.crear(publicacion)
