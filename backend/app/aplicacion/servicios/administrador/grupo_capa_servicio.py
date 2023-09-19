from typing import Optional

from bson import ObjectId
from fastapi import Depends
from starlette import status

from app.aplicacion.dtos.administrador.actualizar_grupo_capa_request import (
    ActualizarGrupoCapaRequest,
)
from app.aplicacion.dtos.administrador.crear_grupo_capa_request import (
    CrearGrupoCapaRequest,
)
from app.aplicacion.dtos.administrador.obtener_estructura_grupo_capa_response import (
    ObtenerEstructuraGrupoCapaResponse,
)
from app.aplicacion.dtos.administrador.obtener_por_id_grupo_capa_response import (
    ObtenerPorIdGrupoCapaResponse,
)
from app.aplicacion.dtos.administrador.obtener_todos_grupo_capa_response import (
    ObtenerTodosGrupoCapaResponse,
)
from app.dominio.entidades.compartido.base_entidad import ESTADO_ACTIVO
from app.dominio.entidades.grupo_capa_entidad import GrupoCapaEntidad
from app.dominio.excepciones.aplicacion_exception import AplicacionException
from app.dominio.repositorios.grupo_capa_repositorio import IGrupoCapaRepositorio
from app.dominio.repositorios.servicio_externo_repositorio import (
    IServicioExternoRepositorio,
)
from app.infraestructura.mongo_db.repositorios.grupo_capa_repositorio import (
    GrupoCapaRepositorio,
)
from app.infraestructura.mongo_db.repositorios.servicio_externo_repositorio import (
    ServicioExternoRepositorio,
)


class GrupoCapaServicio:
    def __init__(
        self,
        grupo_capa_repositorio: IGrupoCapaRepositorio = Depends(GrupoCapaRepositorio),
        servicio_externo_repositorio: IServicioExternoRepositorio = Depends(
            ServicioExternoRepositorio
        ),
    ):
        self._grupo_capa_repositorio = grupo_capa_repositorio
        self._servicio_externo_repositorio = servicio_externo_repositorio

    async def __obtener_grupo_capa_descripcion(
        self, grupo_capa_id: Optional[str]
    ) -> Optional[str]:
        grupo_capa: GrupoCapaEntidad = (
            await self._grupo_capa_repositorio.obtener_por_filtros(
                {"_id": ObjectId(grupo_capa_id), "estado": ESTADO_ACTIVO}
            )
        )
        if not grupo_capa:
            return None
        else:
            return grupo_capa.nombre

    def __obtener_hijos(
        self, grupo_capa_id: str, grupos_capas: list[GrupoCapaEntidad]
    ) -> list[ObtenerEstructuraGrupoCapaResponse]:
        hijos: list[ObtenerEstructuraGrupoCapaResponse] = []
        for grupo_capa in grupos_capas:
            if grupo_capa.grupo_capa_id == grupo_capa_id:
                hijos.append(
                    ObtenerEstructuraGrupoCapaResponse(
                        id=grupo_capa.id,
                        label=grupo_capa.nombre,
                        children=self.__obtener_hijos(grupo_capa.id, grupos_capas),
                    )
                )
        return hijos

    def __obtener_estructura_grupos_capas(
        self, grupos_capas: list[GrupoCapaEntidad]
    ) -> list[ObtenerEstructuraGrupoCapaResponse]:
        raices: list[ObtenerEstructuraGrupoCapaResponse] = []
        for grupo_capa in grupos_capas:
            if grupo_capa.grupo_capa_id is None:
                raices.append(
                    ObtenerEstructuraGrupoCapaResponse(
                        id=grupo_capa.id,
                        label=grupo_capa.nombre,
                        children=self.__obtener_hijos(grupo_capa.id, grupos_capas),
                    )
                )
        return raices

    async def obtener_todos(self) -> list[ObtenerTodosGrupoCapaResponse]:
        grupos_capas: list[
            GrupoCapaEntidad
        ] = await self._grupo_capa_repositorio.obtener_todos({"estado": ESTADO_ACTIVO})
        return [
            ObtenerTodosGrupoCapaResponse(
                id=grupo_capa.id,
                nombre=grupo_capa.nombre,
                grupo_capa=await self.__obtener_grupo_capa_descripcion(
                    grupo_capa.grupo_capa_id
                ),
                grupo_capa_id=grupo_capa.grupo_capa_id,
                esta_habilitado=grupo_capa.esta_habilitado,
            )
            for grupo_capa in grupos_capas
        ]

    async def obtener_por_id(self, grupo_capa_id: str) -> ObtenerPorIdGrupoCapaResponse:
        grupo_capa: GrupoCapaEntidad = (
            await self._grupo_capa_repositorio.obtener_por_id(grupo_capa_id)
        )
        if not grupo_capa.estado:
            raise AplicacionException(
                "El grupo de capas no existe", status.HTTP_404_NOT_FOUND
            )
        return ObtenerPorIdGrupoCapaResponse(**grupo_capa.dict())

    async def obtener_estructura(self) -> list[ObtenerEstructuraGrupoCapaResponse]:
        grupos_capas: list[
            GrupoCapaEntidad
        ] = await self._grupo_capa_repositorio.obtener_todos({"estado": ESTADO_ACTIVO})
        elementos_no_agrupados: list[
            ObtenerEstructuraGrupoCapaResponse
        ] = self.__obtener_estructura_grupos_capas(grupos_capas)
        return [
            ObtenerEstructuraGrupoCapaResponse(
                id="root", label="Todos los elementos", children=elementos_no_agrupados
            )
        ]

    async def crear(
        self, request: CrearGrupoCapaRequest, usuario_auditoria_id: str
    ) -> str:
        # Si se ha especificado un grupo de capas padre, se verifica que exista.
        if request.grupo_capa_id:
            existe_grupo_capa: bool = (
                await self._grupo_capa_repositorio.verificar_existencia(
                    request.grupo_capa_id
                )
            )
            if not existe_grupo_capa:
                raise AplicacionException(
                    "El grupo de capas padre no existe", status.HTTP_404_NOT_FOUND
                )
        grupo_capa: GrupoCapaEntidad = GrupoCapaEntidad(
            nombre=request.nombre,
            grupo_capa_id=request.grupo_capa_id,
            esta_habilitado=request.esta_habilitado,
        )
        grupo_capa.registrar_creacion(usuario_auditoria_id)
        return await self._grupo_capa_repositorio.crear(grupo_capa)

    async def actualizar(
        self,
        grupo_capa_id: str,
        request: ActualizarGrupoCapaRequest,
        usuario_auditoria_id: str,
    ) -> str:
        if request.grupo_capa_id:
            existe_grupo_capa: bool = (
                await self._grupo_capa_repositorio.verificar_existencia(
                    request.grupo_capa_id
                )
            )
            if not existe_grupo_capa:
                raise AplicacionException(
                    "El grupo de capas padre no existe", status.HTTP_404_NOT_FOUND
                )
        # El padre no puede ser el mismo grupo de capas.
        if grupo_capa_id == request.grupo_capa_id:
            raise AplicacionException(
                "El grupo de capas padre no puede ser el mismo grupo de capas",
                status.HTTP_400_BAD_REQUEST,
            )
        grupo_capa: GrupoCapaEntidad = (
            await self._grupo_capa_repositorio.obtener_por_id(grupo_capa_id)
        )
        grupo_capa.nombre = request.nombre
        grupo_capa.grupo_capa_id = request.grupo_capa_id
        grupo_capa.esta_habilitado = request.esta_habilitado
        grupo_capa.registrar_actualizacion(usuario_auditoria_id)
        return await self._grupo_capa_repositorio.actualizar(grupo_capa_id, grupo_capa)

    async def eliminar(self, grupo_capa_id: str, usuario_auditoria_id: str) -> str:
        # Se verifica que el grupo de capas exista.
        existe_grupo_capa: bool = (
            await self._grupo_capa_repositorio.verificar_existencia(grupo_capa_id)
        )
        if not existe_grupo_capa:
            raise AplicacionException(
                "El grupo de capas no existe", status.HTTP_404_NOT_FOUND
            )
        # Se verifica que el grupo de capas no tenga otros grupos de capas internos.
        existe_elementos_internos: bool = (
            await self._grupo_capa_repositorio.verificar_existencia_por_filtros(
                {"estado": ESTADO_ACTIVO, "grupo_capa_id": grupo_capa_id}
            )
        )
        if existe_elementos_internos:
            raise AplicacionException(
                "El grupo de capas tiene elementos internos, elimínelos primero",
                status.HTTP_400_BAD_REQUEST,
            )
        # Se verifica que el grupo de capas no tenga servicios internos.
        existen_servicios_internos: bool = (
            await self._servicio_externo_repositorio.verificar_existencia_por_filtros(
                {"estado": ESTADO_ACTIVO, "grupo_capa_id": grupo_capa_id}
            )
        )
        if existen_servicios_internos:
            raise AplicacionException(
                "El grupo de capas tiene servicios externos, elimínelos primero",
                status.HTTP_400_BAD_REQUEST,
            )
        return await self._grupo_capa_repositorio.eliminar(
            grupo_capa_id, usuario_auditoria_id
        )
