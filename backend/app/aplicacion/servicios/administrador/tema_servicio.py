from fastapi import Depends, status
from app.aplicacion.dtos.administrador.actualizar_tema_request import (
    ActualizarTemaRequest,
)
from app.aplicacion.dtos.administrador.crear_tema_request import CrearTemaRequest
from app.aplicacion.dtos.administrador.obtener_por_id_tema_response import (
    ObtenerPorIdTemaResponse,
)
from app.aplicacion.dtos.administrador.obtener_todos_tema_response import (
    ObtenerTodosTemaResponse,
)
from app.dominio.entidades.tema_entidad import TemaEntidad
from app.dominio.entidades.compartido import base_entidad
from app.dominio.excepciones.aplicacion_exception import AplicacionException
from app.dominio.repositorios.catalogo_repositorio import ICatalogoRepositorio
from app.dominio.repositorios.tema_repositorio import ITemaRepositorio
from app.infraestructura.mongo_db.repositorios.catalogo_repositorio import (
    CatalogoRepositorio,
)
from app.infraestructura.mongo_db.repositorios.tema_repositorio import TemaRepositorio


class TemaServicio:
    """
    Clase que contiene la lógica de negocio para la administración de temas.
    """

    def __init__(
        self,
        tema_repositorio: ITemaRepositorio = Depends(TemaRepositorio),
        catalogo_repositorio: ICatalogoRepositorio = Depends(CatalogoRepositorio),
    ):
        self._catalogo_repositorio = catalogo_repositorio
        self._tema_repositorio = tema_repositorio

    async def obtener_todos(self) -> list[ObtenerTodosTemaResponse]:
        temas: list[TemaEntidad] = await self._tema_repositorio.obtener_todos(
            {"estado": base_entidad.ESTADO_ACTIVO}
        )
        return [ObtenerTodosTemaResponse(**tema.dict()) for tema in temas]

    async def obtener_por_id(self, tema_id: str) -> ObtenerPorIdTemaResponse:
        tema: TemaEntidad = await self._tema_repositorio.obtener_por_id(tema_id)
        if not tema.estado:
            raise AplicacionException("El tema no existe", status.HTTP_404_NOT_FOUND)
        return ObtenerPorIdTemaResponse(**tema.dict())

    async def crear(self, request: CrearTemaRequest, usuario_auditoria_id: str) -> str:
        if not await self._catalogo_repositorio.verificar_existencia(
            request.catalogo_id
        ):
            raise AplicacionException(
                "El catálogo no existe", status.HTTP_404_NOT_FOUND
            )

        tema: TemaEntidad = TemaEntidad(
            codigo=request.codigo,
            nombre=request.nombre,
            descripcion=request.descripcion,
            catalogo_id=request.catalogo_id,
            fecha_creacion=request.fecha_creacion,
        )
        tema.registrar_creacion(usuario_auditoria_id)
        return await self._tema_repositorio.crear(tema)

    async def actualizar(
        self,
        tema_id: str,
        request: ActualizarTemaRequest,
        usuario_auditoria_id: str,
    ) -> str:
        if not await self._catalogo_repositorio.verificar_existencia(
            request.catalogo_id
        ):
            raise AplicacionException(
                "El catálogo no existe", status.HTTP_404_NOT_FOUND
            )

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
