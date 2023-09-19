from fastapi import Depends
from starlette import status

from app.aplicacion.dtos.administrador.actualizar_grupo_request import ActualizarGrupoRequest
from app.aplicacion.dtos.administrador.crear_grupo_request import CrearGrupoRequest
from app.aplicacion.dtos.administrador.obtener_por_id_grupo_response import ObtenerPorIdGrupoResponse
from app.aplicacion.dtos.administrador.obtener_todos_grupo_response import ObtenerTodosGrupoResponse
from app.dependencies import registrar_repo_grupo, registrar_repo_tema
from app.dominio.entidades.grupo_entidad import GrupoEntidad
from app.dominio.excepciones.aplicacion_exception import AplicacionException
from app.dominio.repositorios.base_repositorio import IBaseRepositorio


class GrupoServicio:
    def __init__(self, grupo_repositorio: IBaseRepositorio = Depends(registrar_repo_grupo),
                 tema_repositorio: IBaseRepositorio = Depends(registrar_repo_tema)):
        self._grupo_repositorio = grupo_repositorio
        self._tema_repositorio = tema_repositorio

    async def validar_request(self, request: CrearGrupoRequest, grupo_id: str = None):
        filtros = {"codigo": request.codigo}
        if grupo_id:
            filtros["id__ne"] = grupo_id
        if await self._grupo_repositorio.obtener_por_filtros(filtros):
            raise AplicacionException("El código ingresado ya ha sido asignado")

        if not await self._tema_repositorio.verificar_existencia(request.tema_id):
            raise AplicacionException("El tema seleccionado no existe", status.HTTP_404_NOT_FOUND)

    async def obtener_todos(self) -> list[ObtenerTodosGrupoResponse]:
        grupos: list[GrupoEntidad] = await self._grupo_repositorio.obtener_todos()
        registros = []
        for grupo in grupos:
            tema = await self._tema_repositorio.obtener_por_id(grupo.tema_id)
            registros.append({
                **grupo.dict(),
                "tema_nombre": tema.nombre if tema else ""
            })
        return [ObtenerTodosGrupoResponse(**registro) for registro in registros]

    async def obtener_por_id(self, grupo_id: str) -> ObtenerPorIdGrupoResponse:
        grupo: GrupoEntidad = await self._grupo_repositorio.obtener_por_id(grupo_id)
        if not grupo.estado:
            raise AplicacionException("El grupo no existe", status.HTTP_404_NOT_FOUND)
        return ObtenerPorIdGrupoResponse(**grupo.dict())

    async def crear(self, request: CrearGrupoRequest, usuario_auditoria_id: str) -> str:
        await self.validar_request(request)
        grupo = GrupoEntidad(
            codigo=request.codigo,
            nombre=request.nombre,
            descripcion=request.descripcion,
            tema_id=request.tema_id
        )
        grupo.registrar_creacion(usuario_auditoria_id)
        return await self._grupo_repositorio.crear(grupo)

    async def actualizar(self, grupo_id: str, request: ActualizarGrupoRequest, usuario_auditoria_id: str) -> str:
        await self.validar_request(request, grupo_id)
        grupo = await self._grupo_repositorio.obtener_por_id(grupo_id)
        grupo.codigo = request.codigo
        grupo.nombre = request.nombre
        grupo.descripcion = request.descripcion
        grupo.tema_id = request.tema_id
        grupo.registrar_actualizacion(usuario_auditoria_id)
        return await self._grupo_repositorio.actualizar(grupo_id, grupo)

    async def eliminar(self, grupo_id: str, usuario_auditoria_id: str) -> str:
        existe_grupo: bool = await self._grupo_repositorio.verificar_existencia(grupo_id)
        if not existe_grupo:
            raise AplicacionException("El grupo no existe", status.HTTP_404_NOT_FOUND)
        return await self._grupo_repositorio.eliminar(grupo_id, usuario_auditoria_id)
