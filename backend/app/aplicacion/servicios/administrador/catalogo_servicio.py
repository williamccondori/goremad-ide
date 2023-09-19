from fastapi import Depends
from starlette import status
from app.aplicacion.dtos.administrador.actualizar_catalogo_request import (
    ActualizarCatalogoRequest,
)
from app.aplicacion.dtos.administrador.crear_catalogo_request import (
    CrearCatalogoRequest,
)
from app.aplicacion.dtos.administrador.obtener_por_id_catalogo_response import (
    ObtenerPorIdCatalogoResponse,
)
from app.aplicacion.dtos.administrador.obtener_todos_catalogo_response import (
    ObtenerTodosCatalogoResponse,
)
from app.dominio.entidades.catalogo_entidad import CatalogoEntidad
from app.dominio.entidades.compartido import base_entidad
from app.dominio.excepciones.aplicacion_exception import AplicacionException
from app.dominio.repositorios.catalogo_repositorio import ICatalogoRepositorio
from app.infraestructura.mongo_db.repositorios.catalogo_repositorio import (
    CatalogoRepositorio,
)


class CatalogoServicio:
    """
    Clase que contiene la lógica de negocio para la administración de catálogos.
    """

    def __init__(
        self, catalogo_repositorio: ICatalogoRepositorio = Depends(CatalogoRepositorio)
    ):
        self._catalogo_repositorio = catalogo_repositorio

    async def obtener_todos(self) -> list[ObtenerTodosCatalogoResponse]:
        """
        Obtiene todos los catálogos activos.
        Returns:
            list[ObtenerTodosCatalogoResponse]: Lista de catálogos activos.
        """
        catalogos: list[
            CatalogoEntidad
        ] = await self._catalogo_repositorio.obtener_todos(
            {"estado": base_entidad.ESTADO_ACTIVO}
        )
        return [
            ObtenerTodosCatalogoResponse(**catalogo.dict()) for catalogo in catalogos
        ]

    async def obtener_por_id(self, catalogo_id: str) -> ObtenerPorIdCatalogoResponse:
        """
        Obtiene un catálogo por su identificador.
        Args:
            catalogo_id (str): Identificador del catálogo.
        Returns:
            ObtenerPorIdCatalogoResponse: Catálogo.
        """
        catalogo: CatalogoEntidad = await self._catalogo_repositorio.obtener_por_id(
            catalogo_id
        )
        if not catalogo.estado:
            raise AplicacionException(
                "El catálogo no existe", status.HTTP_404_NOT_FOUND
            )
        return ObtenerPorIdCatalogoResponse(**catalogo.dict())

    async def crear(
        self, request: CrearCatalogoRequest, usuario_auditoria_id: str
    ) -> str:
        """
        Crea un nuevo catálogo.
        Args:
            request (CrearCatalogoRequest): Información del catálogo a crear.
            usuario_auditoria_id (str): Identificador del usuario que crea el catálogo.
        Returns:
            str: Identificador del catálogo creado.
        """
        catalogo: CatalogoEntidad = CatalogoEntidad(
            codigo=request.codigo,
            nombre=request.nombre,
            descripcion=request.descripcion,
            fecha_creacion=request.fecha_creacion,
        )
        catalogo.registrar_creacion(usuario_auditoria_id)
        return await self._catalogo_repositorio.crear(catalogo)

    async def actualizar(
        self,
        catalogo_id: str,
        request: ActualizarCatalogoRequest,
        usuario_auditoria_id: str,
    ) -> str:
        """
        Actualiza un catálogo existente.
        Args:
            catalogo_id (str): Identificador del catálogo.
            request (ActualizarCatalogoRequest): Información del catálogo a actualizar.
            usuario_auditoria_id (str): Identificador del usuario que actualiza el catálogo.
        Returns:
            str: Identificador del catálogo actualizado.
        """
        catalogo = await self._catalogo_repositorio.obtener_por_id(catalogo_id)
        catalogo.codigo = request.codigo
        catalogo.nombre = request.nombre
        catalogo.descripcion = request.descripcion
        catalogo.registrar_actualizacion(usuario_auditoria_id)
        return await self._catalogo_repositorio.actualizar(catalogo_id, catalogo)

    async def eliminar(self, catalogo_id: str, usuario_auditoria_id: str) -> str:
        """
        Elimina un catálogo existente.
        Args:
            catalogo_id (str): Identificador del catálogo.
            usuario_auditoria_id (str): Identificador del usuario que elimina el catálogo.
        Returns:
            str: Identificador del catálogo eliminado.
        """
        existe_catalogo: bool = await self._catalogo_repositorio.verificar_existencia(
            catalogo_id
        )
        if not existe_catalogo:
            raise AplicacionException(
                "El catálogo no existe", status.HTTP_404_NOT_FOUND
            )
        return await self._catalogo_repositorio.eliminar(
            catalogo_id, usuario_auditoria_id
        )
