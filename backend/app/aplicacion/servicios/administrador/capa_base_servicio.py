from fastapi import Depends
from starlette import status

from app.aplicacion.dtos.administrador.actualizar_capa_base_request import (
    ActualizarCapaBaseRequest,
)
from app.aplicacion.dtos.administrador.crear_capa_base_request import (
    CrearCapaBaseRequest,
)
from app.aplicacion.dtos.administrador.obtener_por_id_capa_base_response import (
    ObtenerPorIdCapaBaseResponse,
)
from app.aplicacion.dtos.administrador.obtener_todos_capa_base_response import (
    ObtenerTodosCapaBaseResponse,
)
from app.dependencies import registrar_repo_capa_base
from app.dominio.entidades.capa_base_entidad import CapaBaseEntidad
from app.dominio.excepciones.aplicacion_exception import AplicacionException
from app.dominio.repositorios.base_repositorio import IBaseRepositorio


# noinspection DuplicatedCode
class CapaBaseServicio:
    def __init__(
            self,
            capa_base_repositorio: IBaseRepositorio = Depends(registrar_repo_capa_base),
    ):
        self._capa_base_repositorio = capa_base_repositorio

    async def obtener_todos(self) -> list[ObtenerTodosCapaBaseResponse]:
        capas_base: list[CapaBaseEntidad] = await self._capa_base_repositorio.obtener_todos()
        return [
            ObtenerTodosCapaBaseResponse(**capa_base.dict()) for capa_base in capas_base
        ]

    async def obtener_por_id(self, capa_base_id: str) -> ObtenerPorIdCapaBaseResponse:
        capa_base: CapaBaseEntidad = await self._capa_base_repositorio.obtener_por_id(
            capa_base_id
        )
        return ObtenerPorIdCapaBaseResponse(**capa_base.dict())

    async def crear(
            self, request: CrearCapaBaseRequest, usuario_auditoria_id: str
    ) -> str:
        capa_base: CapaBaseEntidad = CapaBaseEntidad(
            nombre=request.nombre,
            url=request.url,
            atribucion=request.atribucion,
            esta_habilitado=request.esta_habilitado,
        )
        capa_base.registrar_creacion(usuario_auditoria_id)
        return await self._capa_base_repositorio.crear(capa_base)

    async def actualizar(
            self,
            capa_base_id: str,
            request: ActualizarCapaBaseRequest,
            usuario_auditoria_id: str,
    ) -> str:
        capa_base = await self._capa_base_repositorio.obtener_por_id(capa_base_id)
        capa_base.nombre = request.nombre
        capa_base.url = request.url
        capa_base.atribucion = request.atribucion
        capa_base.esta_habilitado = request.esta_habilitado
        capa_base.registrar_actualizacion(usuario_auditoria_id)
        return await self._capa_base_repositorio.actualizar(capa_base_id, capa_base)

    async def eliminar(self, capa_base_id: str, usuario_auditoria_id: str) -> str:
        existe_capa_base: bool = await self._capa_base_repositorio.verificar_existencia(
            capa_base_id
        )
        if not existe_capa_base:
            raise AplicacionException(
                "La capa base no existe", status.HTTP_404_NOT_FOUND
            )
        return await self._capa_base_repositorio.eliminar(
            capa_base_id, usuario_auditoria_id
        )
