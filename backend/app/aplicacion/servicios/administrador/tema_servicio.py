from fastapi import Depends
from starlette import status

from app.aplicacion.dtos.administrador.actualizar_tema_request import ActualizarTemaRequest
from app.aplicacion.dtos.administrador.crear_tema_request import CrearTemaRequest
from app.aplicacion.dtos.administrador.obtener_por_id_tema_response import ObtenerPorIdTemaResponse
from app.aplicacion.dtos.administrador.obtener_todos_tema_response import ObtenerTodosTemaResponse
from app.dependencies import registrar_repo_tema, registrar_repo_catalogo
from app.dominio.entidades.compartido import base_entidad
from app.dominio.entidades.tema_entidad import TemaEntidad
from app.dominio.excepciones.aplicacion_exception import AplicacionException
from app.dominio.repositorios.base_repositorio import IBaseRepositorio


class TemaServicio:

    def __init__(self, tema_repositorio: IBaseRepositorio = Depends(registrar_repo_tema),
                 catalogo_repositorio: IBaseRepositorio = Depends(registrar_repo_catalogo)):
        self._tema_repositorio = tema_repositorio
        self._catalogo_repositorio = catalogo_repositorio

    async def validar_request(self, request: CrearTemaRequest, tema_id: str = None):
        filtros = {"codigo": request.codigo}
        if tema_id:
            filtros["id__ne"] = tema_id
        if await self._tema_repositorio.obtener_por_filtros(filtros):
            raise AplicacionException("El código ingresado ya ha sido asignado")

        if not await self._catalogo_repositorio.verificar_existencia(request.catalogo_id):
            raise AplicacionException("El catálogo seleccionado no existe", status.HTTP_404_NOT_FOUND)

    async def obtener_todos(self) -> list[ObtenerTodosTemaResponse]:
        temas: list[TemaEntidad] = await self._tema_repositorio.obtener_todos()
        return [ObtenerTodosTemaResponse(**tema.dict()) for tema in temas]

    async def obtener_por_id(self, tema_id: str) -> ObtenerPorIdTemaResponse:
        tema: TemaEntidad = await self._tema_repositorio.obtener_por_id(tema_id)
        if not tema.estado:
            raise AplicacionException("El tema no existe", status.HTTP_404_NOT_FOUND)
        return ObtenerPorIdTemaResponse(**tema.dict())

    async def crear(self, request: CrearTemaRequest, usuario_auditoria_id: str) -> str:
        await self.validar_request(request)
        tema = TemaEntidad(
            codigo=request.codigo,
            nombre=request.nombre,
            descripcion=request.descripcion,
            catalogo_id=request.catalogo_id
        )
        tema.registrar_creacion(usuario_auditoria_id)
        return await self._tema_repositorio.crear(tema)

    async def actualizar(self, tema_id: str, request: ActualizarTemaRequest, usuario_auditoria_id: str) -> str:
        await self.validar_request(request, tema_id)
        tema = await self._tema_repositorio.obtener_por_id(tema_id)
        tema.codigo = request.codigo
        tema.nombre = request.nombre
        tema.descripcion = request.descripcion
        tema.catalogo_id = request.catalogo_id
        tema.registrar_actualizacion(usuario_auditoria_id)
        return await self._tema_repositorio.actualizar(tema_id, tema)

    async def eliminar(self, tema_id: str, usuario_auditoria_id: str) -> str:
        existe_tema: bool = await self._tema_repositorio.verificar_existencia(tema_id)
        if not existe_tema:
            raise AplicacionException("El tema no existe", status.HTTP_404_NOT_FOUND)
        return await self._tema_repositorio.eliminar(tema_id, usuario_auditoria_id)
