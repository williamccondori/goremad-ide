from fastapi import Depends
from starlette import status

from app.aplicacion.dtos.administrador.actualizar_objeto_geografico_request import ActualizarObjetoGeograficoRequest
from app.aplicacion.dtos.administrador.crear_objeto_geografico_request import CrearObjetoGeograficoRequest
from app.aplicacion.dtos.administrador.obtener_por_id_objeto_geografico_response import \
    ObtenerPorIdObjetoGeograficoResponse
from app.aplicacion.dtos.administrador.obtener_todos_objeto_geografico_response import \
    ObtenerTodosObjetoGeograficoResponse
from app.dependencies import registrar_repo_objeto_geografico, registrar_repo_grupo
from app.dominio.entidades.objeto_geografico_entidad import ObjetoGeograficoEntidad
from app.dominio.excepciones.aplicacion_exception import AplicacionException
from app.dominio.repositorios.base_repositorio import IBaseRepositorio


class ObjetoGeograficoServicio:
    def __init__(self,
                 objeto_geografico_repositorio: IBaseRepositorio = Depends(registrar_repo_objeto_geografico),
                 grupo_repositorio: IBaseRepositorio = Depends(registrar_repo_grupo)
                 ):
        self._objeto_geografico_repositorio = objeto_geografico_repositorio
        self._grupo_repositorio = grupo_repositorio

    async def validar_request(self, request: CrearObjetoGeograficoRequest, objeto_geografico_id: str = None):
        filtros = {"codigo": request.codigo}
        if objeto_geografico_id:
            filtros["id__ne"] = objeto_geografico_id
        if await self._objeto_geografico_repositorio.obtener_por_filtros(filtros):
            raise AplicacionException("El código ingresado ya ha sido asignado")

        if not await self._grupo_repositorio.verificar_existencia(request.grupo_id):
            raise AplicacionException("El grupo seleccionado no existe", status.HTTP_404_NOT_FOUND)

    async def obtener_todos(self) -> list[ObtenerTodosObjetoGeograficoResponse]:
        objetos_geograficos: list[ObjetoGeograficoEntidad] = await self._objeto_geografico_repositorio.obtener_todos()
        return [ObtenerTodosObjetoGeograficoResponse(**objeto.dict()) for objeto in objetos_geograficos]

    async def obtener_por_id(self, objeto_id: str) -> ObtenerPorIdObjetoGeograficoResponse:
        objeto_geografico: ObjetoGeograficoEntidad = await self._objeto_geografico_repositorio.obtener_por_id(objeto_id)
        if not objeto_geografico.estado:
            raise AplicacionException("El objeto geográfico no existe", status.HTTP_404_NOT_FOUND)
        return ObtenerPorIdObjetoGeograficoResponse(**objeto_geografico.dict())

    async def crear(self, request: CrearObjetoGeograficoRequest, usuario_auditoria_id: str) -> str:
        await self.validar_request(request)
        objeto_geografico = ObjetoGeograficoEntidad(
            codigo=request.codigo,
            nombre=request.nombre,
            descripcion=request.descripcion,
            grupo_id=request.grupo_id
        )
        objeto_geografico.registrar_creacion(usuario_auditoria_id)
        return await self._objeto_geografico_repositorio.crear(objeto_geografico)

    async def actualizar(self, objeto_geografico_id: str, request: ActualizarObjetoGeograficoRequest,
                         usuario_auditoria_id: str) -> str:
        await self.validar_request(request, objeto_geografico_id)
        objeto_geografico = await self._objeto_geografico_repositorio.obtener_por_id(objeto_geografico_id)
        objeto_geografico.codigo = request.codigo
        objeto_geografico.nombre = request.nombre
        objeto_geografico.descripcion = request.descripcion
        objeto_geografico.grupo_id = request.grupo_id
        objeto_geografico.registrar_actualizacion(usuario_auditoria_id)
        return await self._objeto_geografico_repositorio.actualizar(objeto_geografico_id, objeto_geografico)

    async def eliminar(self, objeto_id: str, usuario_auditoria_id: str) -> str:
        existe_objeto_geografico: bool = await self._objeto_geografico_repositorio.verificar_existencia(objeto_id)
        if not existe_objeto_geografico:
            raise AplicacionException("El objeto geográfico no existe", status.HTTP_404_NOT_FOUND)
        return await self._objeto_geografico_repositorio.eliminar(objeto_id, usuario_auditoria_id)
