from fastapi import Depends
from starlette import status

from app.aplicacion.dtos.administrador.actualizar_catalogo_request import ActualizarCatalogoRequest
from app.aplicacion.dtos.administrador.crear_catalogo_request import CrearCatalogoRequest
from app.aplicacion.dtos.administrador.obtener_por_id_catalogo_response import ObtenerPorIdCatalogoResponse
from app.aplicacion.dtos.administrador.obtener_todos_catalogo_response import ObtenerTodosCatalogoResponse
from app.dependencies import registrar_repo_catalogo
from app.dominio.entidades.catalogo_entidad import CatalogoEntidad
from app.dominio.excepciones.aplicacion_exception import AplicacionException
from app.dominio.repositorios.base_repositorio import IBaseRepositorio


class CatalogoServicio:

    def __init__(self, catalogo_repositorio: IBaseRepositorio = Depends(registrar_repo_catalogo)):
        self._catalogo_repositorio = catalogo_repositorio

    async def validar_request(self, request: CrearCatalogoRequest, catalogo_id: str = None):
        filtros = {"codigo": request.codigo}
        if catalogo_id:
            filtros["id__ne"] = catalogo_id
        if await self._catalogo_repositorio.obtener_por_filtros(filtros):
            raise AplicacionException("El código ingresado ya ha sido asignado")

    async def obtener_todos(self) -> list[ObtenerTodosCatalogoResponse]:
        catalogos: list[CatalogoEntidad] = await self._catalogo_repositorio.obtener_todos()
        return [ObtenerTodosCatalogoResponse(**catalogo.dict()) for catalogo in catalogos]

    async def obtener_por_id(self, catalogo_id: str) -> ObtenerPorIdCatalogoResponse:
        catalogo: CatalogoEntidad = await self._catalogo_repositorio.obtener_por_id(catalogo_id)
        if not catalogo.estado:
            raise AplicacionException("El catálogo no existe", status.HTTP_404_NOT_FOUND)
        return ObtenerPorIdCatalogoResponse(**catalogo.dict())

    async def crear(self, request: CrearCatalogoRequest, usuario_auditoria_id: str) -> str:
        await self.validar_request(request)
        catalogo: CatalogoEntidad = CatalogoEntidad(
            codigo=request.codigo,
            nombre=request.nombre,
            descripcion=request.descripcion
        )
        catalogo.registrar_creacion(usuario_auditoria_id)
        return await self._catalogo_repositorio.crear(catalogo)

    async def actualizar(self, catalogo_id: str, request: ActualizarCatalogoRequest, usuario_auditoria_id: str) -> str:
        await self.validar_request(request, catalogo_id)
        catalogo = await self._catalogo_repositorio.obtener_por_id(catalogo_id)
        catalogo.codigo = request.codigo
        catalogo.nombre = request.nombre
        catalogo.descripcion = request.descripcion
        catalogo.registrar_actualizacion(usuario_auditoria_id)
        return await self._catalogo_repositorio.actualizar(catalogo_id, catalogo)

    async def eliminar(self, catalogo_id: str, usuario_auditoria_id: str) -> str:
        existe_catalogo: bool = await self._catalogo_repositorio.verificar_existencia(catalogo_id)
        if not existe_catalogo:
            raise AplicacionException("El catálogo no existe", status.HTTP_404_NOT_FOUND)
        return await self._catalogo_repositorio.eliminar(catalogo_id, usuario_auditoria_id)
