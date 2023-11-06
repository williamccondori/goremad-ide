from fastapi import Depends
from starlette import status

from app.aplicacion.dtos.administrador.actualizar_publicacion_request import ActualizarPublicacionRequest
from app.aplicacion.dtos.administrador.crear_publicacion_request import CrearPublicacionRequest
from app.aplicacion.dtos.administrador.obtener_por_id_publicacion_response import ObtenerPorIdPublicacionResponse
from app.aplicacion.dtos.administrador.obtener_todos_publicacion_response import ObtenerTodosPublicacionResponse
from app.dependencies import registrar_repo_publicacion
from app.dominio.entidades.publicacion_entidad import PublicacionEntidad
from app.dominio.excepciones.aplicacion_exception import AplicacionException
from app.dominio.repositorios.base_repositorio import IBaseRepositorio


class PublicacionServicio:
    def __init__(
            self,
            publicacion_repositorio: IBaseRepositorio = Depends(registrar_repo_publicacion),
    ):
        self._publicacion_repositorio = publicacion_repositorio

    async def obtener_todos(self) -> list[ObtenerTodosPublicacionResponse]:
        publicaciones: list[PublicacionEntidad] = await self._publicacion_repositorio.obtener_todos()
        return [
            ObtenerTodosPublicacionResponse(**publicacion.dict()) for publicacion in publicaciones
        ]

    async def obtener_por_id(self, publicacion_id: str) -> ObtenerPorIdPublicacionResponse:
        publicacion: PublicacionEntidad = await self._publicacion_repositorio.obtener_por_id(publicacion_id)
        return ObtenerPorIdPublicacionResponse(**publicacion.dict())

    async def crear(
            self, request: CrearPublicacionRequest, usuario_auditoria_id: str
    ) -> str:
        publicacion: PublicacionEntidad = PublicacionEntidad(
            tipo=request.tipo,
            titulo=request.titulo,
            resumen=request.resumen,
            contenido=request.contenido,
            imagen=request.imagen,
            esta_habilitado=request.esta_habilitado
        )
        publicacion.registrar_creacion(usuario_auditoria_id)
        return await self._publicacion_repositorio.crear(publicacion)

    async def actualizar(
            self,
            publicacion_id: str,
            request: ActualizarPublicacionRequest,
            usuario_auditoria_id: str,
    ) -> str:
        publicacion = await self._publicacion_repositorio.obtener_por_id(publicacion_id)
        publicacion.tipo = request.tipo
        publicacion.titulo = request.titulo
        publicacion.resumen = request.resumen
        publicacion.contenido = request.contenido
        publicacion.imagen = request.imagen
        publicacion.esta_habilitado = request.esta_habilitado
        publicacion.registrar_actualizacion(usuario_auditoria_id)
        return await self._publicacion_repositorio.actualizar(publicacion_id, publicacion)

    async def eliminar(self, publicacion_id: str, usuario_auditoria_id: str) -> str:
        existe_publicacion: bool = await self._publicacion_repositorio.verificar_existencia(
            publicacion_id
        )
        if not existe_publicacion:
            raise AplicacionException(
                "La publicación no existe", status.HTTP_404_NOT_FOUND
            )
        return await self._publicacion_repositorio.eliminar(
            publicacion_id, usuario_auditoria_id
        )
