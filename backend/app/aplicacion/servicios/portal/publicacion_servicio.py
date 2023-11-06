from fastapi import Depends

from app.aplicacion.dtos.portal.obtener_todos_publicacion_response import ObtenerTodosPublicacionResponse
from app.dependencies import registrar_repo_publicacion
from app.dominio.entidades.publicacion_entidad import PublicacionEntidad
from app.dominio.repositorios.base_repositorio import IBaseRepositorio


class PublicacionServicio:
    def __init__(
            self,
            publicacion_repositorio: IBaseRepositorio = Depends(registrar_repo_publicacion),
    ):
        self._publicacion_repositorio = publicacion_repositorio

    async def obtener_todos(self, tipo_publicacion: str) -> list[ObtenerTodosPublicacionResponse]:
        publicaciones: list[PublicacionEntidad] = await self._publicacion_repositorio.obtener_todos({
            "tipo": tipo_publicacion
        })
        return [
            ObtenerTodosPublicacionResponse(**publicacion.dict()) for publicacion in publicaciones
        ]
