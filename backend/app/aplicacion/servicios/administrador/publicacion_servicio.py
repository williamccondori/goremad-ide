from fastapi import Depends
from starlette import status

from app.dominio.entidades.publicacion_entidad import PublicacionEntidad
from app.dominio.excepciones.aplicacion_exception import AplicacionException
from app.dominio.repositorios.base_repositorio import IBaseRepositorio


class PublicacionServicio:
    def __init__(
            self,
            publicacion_repositorio: IBaseRepositorio = Depends(registrar_repo_publicacion),
    ):
        self._publicacion_repositorio = publicacion_repositorio

    async def crear(
            self, request: CrearPublicacionRequest, usuario_auditoria_id: str
    ) -> str:
        publicacion: PublicacionEntidad = PublicacionEntidad(
            tipo=request.tipo,
            titulo=request.titulo,
            resumen=request.resumen,
            contenido=request.contenido,
            imagen=request.imagen,
            esta_habilitado=request.esta_habilitado,
            fecha_publicacion=request.imagen,
            usuario=request.usuario,
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
        publicacion.nombre = request.nombre
        publicacion.url = request.url
        publicacion.atribucion = request.atribucion
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
