from fastapi import Depends, status
from app.aplicacion.dtos.administrador.actualizar_grupo_request import (
    ActualizarGrupoRequest,
)
from app.aplicacion.dtos.administrador.crear_grupo_request import CrearGrupoRequest
from app.aplicacion.dtos.administrador.obtener_por_id_grupo_response import (
    ObtenerPorIdGrupoResponse,
)
from app.aplicacion.dtos.administrador.obtener_todos_grupo_response import (
    ObtenerTodosGrupoResponse,
)
from app.dominio.entidades.grupo_entidad import GrupoEntidad
from app.dominio.entidades.compartido import base_entidad
from app.dominio.excepciones.aplicacion_exception import AplicacionException
from app.dominio.repositorios.tema_repositorio import ITemaRepositorio
from app.dominio.repositorios.grupo_repositorio import IGrupoRepositorio
from app.infraestructura.mongo_db.repositorios.tema_repositorio import (
    TemaRepositorio,
)
from app.infraestructura.mongo_db.repositorios.grupo_repositorio import GrupoRepositorio


class GrupoServicio:
    """
    Clase que contiene la lógica de negocio para la administración de grupos.
    """

    def __init__(
        self,
        grupo_repositorio: IGrupoRepositorio = Depends(GrupoRepositorio),
        tema_repositorio: ITemaRepositorio = Depends(TemaRepositorio),
    ):
        """
        Constructor de la clase GrupoServicio.

        Args:
            grupo_repositorio (IGrupoRepositorio, optional): El repositorio de grupos. Por defecto, utiliza GrupoRepositorio.
        """
        self._tema_repositorio = tema_repositorio
        self._grupo_repositorio = grupo_repositorio

    async def obtener_todos(self) -> list[ObtenerTodosGrupoResponse]:
        """
        Obtiene todos los grupos activos.

        Returns:
            list[ObtenerTodosGrupoResponse]: Lista de grupos activos.
        """
        grupos: list[GrupoEntidad] = await self._grupo_repositorio.obtener_todos(
            {"estado": base_entidad.ESTADO_ACTIVO}
        )
        return [ObtenerTodosGrupoResponse(**grupo.dict()) for grupo in grupos]

    async def obtener_por_id(self, grupo_id: str) -> ObtenerPorIdGrupoResponse:
        """
        Obtiene un grupo por su identificador.

        Args:
            grupo_id (str): Identificador del grupo.

        Returns:
            ObtenerPorIdGrupoResponse: Catálogo.
        """
        grupo: GrupoEntidad = await self._grupo_repositorio.obtener_por_id(grupo_id)
        if not grupo.estado:
            raise AplicacionException("El grupo no existe", status.HTTP_404_NOT_FOUND)
        return ObtenerPorIdGrupoResponse(**grupo.dict())

    async def crear(self, request: CrearGrupoRequest, usuario_auditoria_id: str) -> str:
        """
        Crea un nuevo grupo.

        Args:
            request (CrearGrupoRequest): Información del grupo a crear.
            usuario_auditoria_id (str): Identificador del usuario que crea el grupo.

        Returns:
            str: Identificador del grupo creado.
        """
        if not await self._tema_repositorio.verificar_existencia(request.tema_id):
            raise AplicacionException("El tema no existe", status.HTTP_404_NOT_FOUND)

        grupo: GrupoEntidad = GrupoEntidad(
            codigo=request.codigo,
            nombre=request.nombre,
            descripcion=request.descripcion,
            tema_id=request.tema_id,
            fecha_creacion=request.fecha_creacion,
        )
        grupo.registrar_creacion(usuario_auditoria_id)
        return await self._grupo_repositorio.crear(grupo)

    async def actualizar(
        self,
        grupo_id: str,
        request: ActualizarGrupoRequest,
        usuario_auditoria_id: str,
    ) -> str:
        """
        Actualiza un grupo existente.

        Args:
            grupo_id (str): Identificador del grupo.
            request (ActualizarGrupoRequest): Información del grupo a actualizar.
            usuario_auditoria_id (str): Identificador del usuario que actualiza el grupo.

        Returns:
            str: Identificador del grupo actualizado.
        """
        if not await self._tema_repositorio.verificar_existencia(request.tema_id):
            raise AplicacionException("El tema no existe", status.HTTP_404_NOT_FOUND)

        grupo = await self._grupo_repositorio.obtener_por_id(grupo_id)
        grupo.codigo = request.codigo
        grupo.nombre = request.nombre
        grupo.descripcion = request.descripcion
        grupo.tema_id = request.tema_id
        grupo.registrar_actualizacion(usuario_auditoria_id)
        return await self._grupo_repositorio.actualizar(grupo_id, grupo)

    async def eliminar(self, grupo_id: str, usuario_auditoria_id: str) -> str:
        """
        Elimina un grupo existente.

        Args:
            grupo_id (str): Identificador del grupo.
            usuario_auditoria_id (str): Identificador del usuario que elimina el grupo.

        Returns:
            str: Identificador del grupo eliminado.
        """
        existe_grupo: bool = await self._grupo_repositorio.verificar_existencia(
            grupo_id
        )
        if not existe_grupo:
            raise AplicacionException("El grupo no existe", status.HTTP_404_NOT_FOUND)
        return await self._grupo_repositorio.eliminar(grupo_id, usuario_auditoria_id)
