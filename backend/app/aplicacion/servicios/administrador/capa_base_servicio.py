from fastapi import Depends
from starlette import status

from app.aplicacion.dtos.administrador.actualizar_capa_base_request import ActualizarCapaBaseRequest
from app.aplicacion.dtos.administrador.crear_capa_base_request import CrearCapaBaseRequest
from app.aplicacion.dtos.administrador.obtener_por_id_capa_base_response import ObtenerPorIdCapaBaseResponse
from app.aplicacion.dtos.administrador.obtener_todos_capa_base_response import ObtenerTodosCapaBaseResponse
from app.dominio.entidades.capa_base_entidad import CapaBaseEntidad
from app.dominio.entidades.compartido import base_entidad
from app.dominio.excepciones.aplicacion_exception import AplicacionException
from app.dominio.repositorios.capa_base_repositorio import ICapaBaseRepositorio
from app.infraestructura.mongo_db.repositorios.capa_base_repositorio import CapaBaseRepositorio


class CapaBaseServicio:
    """
    Clase que contiene la logica de negocio para la administracion de capas base.
    """

    def __init__(self,
                 capa_base_repositorio: ICapaBaseRepositorio = Depends(CapaBaseRepositorio)
                 ):
        self._capa_base_repositorio = capa_base_repositorio

    async def obtener_todos(self) -> list[ObtenerTodosCapaBaseResponse]:
        """
        Obtiene todas las capas base activas.
        Returns:
            list[ObtenerTodosCapaBaseResponse]: Lista de capas base activas.
        """
        capas_base: list[CapaBaseEntidad] = await self._capa_base_repositorio.obtener_todos({
            "estado": base_entidad.ESTADO_ACTIVO
        })
        return [ObtenerTodosCapaBaseResponse(**capa_base.dict()) for capa_base in capas_base]

    async def obtener_por_id(self, capa_base_id: str) -> ObtenerPorIdCapaBaseResponse:
        """
        Obtiene una capa base por su identificador.
        Args:
            capa_base_id (str): Identificador de la capa base.
        Returns:
            ObtenerPorIdCapaBaseResponse: Capa base.
        """
        capa_base: CapaBaseEntidad = await self._capa_base_repositorio.obtener_por_id(capa_base_id)
        if not capa_base.estado:
            raise AplicacionException("La capa base no existe", status.HTTP_404_NOT_FOUND)
        return ObtenerPorIdCapaBaseResponse(**capa_base.dict())

    async def crear(self, request: CrearCapaBaseRequest, usuario_auditoria_id: str) -> str:
        """
        Crea una nueva capa base.
        Args:
            request (CrearCapaBaseRequest): Informacion de la capa base a crear.
            usuario_auditoria_id (str): Identificador del usuario que crea la capa base.
        Returns:
            str: Identificador de la capa base creada.
        """
        capa_base: CapaBaseEntidad = CapaBaseEntidad(
            nombre=request.nombre,
            url=request.url,
            atribucion=request.atribucion,
            esta_habilitado=request.esta_habilitado
        )
        capa_base.registrar_creacion(usuario_auditoria_id)
        return await self._capa_base_repositorio.crear(capa_base)

    async def actualizar(self, capa_base_id: str, request: ActualizarCapaBaseRequest, usuario_auditoria_id: str) -> str:
        """
        Actualiza una capa base existente.
        Args:
            capa_base_id (str): Identificador de la capa base.
            request (ActualizarCapaBaseRequest): Informacion de la capa base a actualizar.
            usuario_auditoria_id (str): Identificador del usuario que actualiza la capa base.
        Returns:
            str: Identificador de la capa base actualizada.
        """
        capa_base = await self._capa_base_repositorio.obtener_por_id(capa_base_id)
        capa_base.nombre = request.nombre
        capa_base.url = request.url
        capa_base.atribucion = request.atribucion
        capa_base.esta_habilitado = request.esta_habilitado
        capa_base.registrar_actualizacion(usuario_auditoria_id)
        return await self._capa_base_repositorio.actualizar(capa_base_id, capa_base)

    async def eliminar(self, capa_base_id: str, usuario_auditoria_id: str) -> str:
        """
        Elimina una capa base existente.
        Args:
            capa_base_id (str): Identificador de la capa base.
            usuario_auditoria_id (str): Identificador del usuario que elimina la capa base.
        Returns:
            str: Identificador de la capa base eliminada.
        """
        existe_capa_base: bool = await self._capa_base_repositorio.verificar_existencia(capa_base_id)
        if not existe_capa_base:
            raise AplicacionException("La capa base no existe", status.HTTP_404_NOT_FOUND)
        return await self._capa_base_repositorio.eliminar(capa_base_id, usuario_auditoria_id)
