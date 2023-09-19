from typing import Optional

from bson import ObjectId
from fastapi import Depends
from starlette import status

from app.aplicacion.dtos.administrador.actualizar_servicio_externo_request import (
    ActualizarServicioExternoRequest,
)
from app.aplicacion.dtos.administrador.crear_servicio_externo_request import (
    CrearServicioExternoRequest,
)
from app.aplicacion.dtos.administrador.obtener_por_id_servicio_externo_response import (
    ObtenerPorIdServicioExternoResponse,
)
from app.aplicacion.dtos.administrador.obtener_todos_servicio_externo_request import (
    ObtenerTodosServicioExternoRequest,
)
from app.aplicacion.dtos.administrador.obtener_todos_servicio_externo_response import (
    ObtenerTodosServicioExternoResponse,
)
from app.aplicacion.utilidades.wms import (
    obtener_informacion_wms,
    InformacionWebMapServiceModelo,
)
from app.dominio.entidades.compartido.base_entidad import ESTADO_ACTIVO
from app.dominio.entidades.grupo_capa_entidad import GrupoCapaEntidad
from app.dominio.entidades.servicio_externo_entidad import (
    ServicioExternoEntidad,
    ServicioExternoCapaEntidad,
)
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


class ServicioExternoServicio:
    def __init__(
        self,
        servicio_externo_repositorio: IServicioExternoRepositorio = Depends(
            ServicioExternoRepositorio
        ),
        grupo_capa_repositorio: IGrupoCapaRepositorio = Depends(GrupoCapaRepositorio),
    ):
        self._servicio_externo_repositorio = servicio_externo_repositorio
        self._grupo_capa_repositorio = grupo_capa_repositorio

    async def __validar_existencia_grupo_capa(
        self, grupo_capa_id: Optional[str]
    ) -> None:
        if grupo_capa_id:
            existe_grupo_capa: bool = (
                await self._grupo_capa_repositorio.verificar_existencia(grupo_capa_id)
            )
            if not existe_grupo_capa:
                raise AplicacionException(
                    "El grupo de capa no existe", status.HTTP_404_NOT_FOUND
                )
        if grupo_capa_id == "":
            raise AplicacionException(
                "El grupo de capa no puede estar vacío (puede ser NULO)",
                status.HTTP_400_BAD_REQUEST,
            )

    async def __obtener_grupo_capa_descripcion(
        self, grupo_capa_id: Optional[str]
    ) -> Optional[str]:
        if not grupo_capa_id:
            return None
        grupo_capa: GrupoCapaEntidad = (
            await self._grupo_capa_repositorio.obtener_por_filtros(
                {"_id": ObjectId(grupo_capa_id), "estado": ESTADO_ACTIVO}
            )
        )
        if not grupo_capa:
            return None
        return grupo_capa.nombre

    async def obtener_todos(
        self, request: ObtenerTodosServicioExternoRequest
    ) -> list[ObtenerTodosServicioExternoResponse]:
        servicios_externos: list[
            ServicioExternoEntidad
        ] = await self._servicio_externo_repositorio.obtener_todos(
            {"estado": ESTADO_ACTIVO}
        )
        servicios_externos_respuesta = []
        # Si se solicita incluir las capas, se obtienen las capas de cada servicio externo.
        if request.incluir_capas:
            for servicio_externo in servicios_externos:
                if servicio_externo.esta_habilitado:
                    for capa in servicio_externo.capas:
                        servicios_externos_respuesta.append(
                            ObtenerTodosServicioExternoResponse(
                                id=f"{servicio_externo.id}__{capa.nombre}",
                                url=servicio_externo.url,
                                nombre=f"{servicio_externo.nombre}: {capa.titulo}",
                                atribucion=servicio_externo.atribucion,
                                grupo_capa=await self.__obtener_grupo_capa_descripcion(
                                    servicio_externo.grupo_capa_id
                                )
                                or "Principal",
                                grupo_capa_id=servicio_externo.grupo_capa_id,
                                esta_habilitado=servicio_externo.esta_habilitado,
                            )
                        )
        else:
            for servicio_externo in servicios_externos:
                servicios_externos_respuesta.append(
                    ObtenerTodosServicioExternoResponse(
                        id=servicio_externo.id,
                        url=servicio_externo.url,
                        nombre=servicio_externo.nombre,
                        atribucion=servicio_externo.atribucion,
                        grupo_capa=await self.__obtener_grupo_capa_descripcion(
                            servicio_externo.grupo_capa_id
                        )
                        or "Principal",
                        grupo_capa_id=servicio_externo.grupo_capa_id,
                        esta_habilitado=servicio_externo.esta_habilitado,
                    )
                )
        return servicios_externos_respuesta

    async def obtener_por_id(
        self, servicio_externo_id: str
    ) -> ObtenerPorIdServicioExternoResponse:
        servicio_externo: ServicioExternoEntidad = (
            await self._servicio_externo_repositorio.obtener_por_id(servicio_externo_id)
        )
        if not servicio_externo.estado:
            raise AplicacionException(
                "El servicio externo no existe", status.HTTP_404_NOT_FOUND
            )
        return ObtenerPorIdServicioExternoResponse(
            id=servicio_externo.id,
            url=servicio_externo.url,
            nombre=servicio_externo.nombre,
            atribucion=servicio_externo.atribucion,
            grupo_capa_id=servicio_externo.grupo_capa_id,
            esta_habilitado=servicio_externo.esta_habilitado,
        )

    async def crear(
        self, request: CrearServicioExternoRequest, usuario_auditoria_id: str
    ) -> str:
        # Se hace la validacion de que el grupo ingresado exista.
        await self.__validar_existencia_grupo_capa(request.grupo_capa_id)
        # Se obtiene la informacion del servicio externo.
        informacion_wms: InformacionWebMapServiceModelo = obtener_informacion_wms(
            request.url
        )
        # Se realiza la creacion del servicio externo.
        servicio_externo: ServicioExternoEntidad = ServicioExternoEntidad(
            nombre=request.nombre,
            url=informacion_wms.url,
            atribucion=request.atribucion,
            grupo_capa_id=request.grupo_capa_id,
            capas=[
                ServicioExternoCapaEntidad(
                    nombre=capa.nombre,
                    titulo=capa.titulo,
                    cuadro_delimitador=capa.cuadro_delimitador,
                )
                for capa in informacion_wms.capas
            ],
            esta_habilitado=request.esta_habilitado,
        )
        servicio_externo.registrar_creacion(usuario_auditoria_id)
        return await self._servicio_externo_repositorio.crear(servicio_externo)

    async def actualizar(
        self,
        servicio_externo_id: str,
        request: ActualizarServicioExternoRequest,
        usuario_auditoria_id: str,
    ) -> str:
        # Se hace la validacion de que el grupo ingresado exista.
        await self.__validar_existencia_grupo_capa(request.grupo_capa_id)
        # Se obtiene la informacion del servicio externo.
        informacion_wms: InformacionWebMapServiceModelo = obtener_informacion_wms(
            request.url
        )
        # Se realiza la creacion del servicio externo.
        servicio_externo: ServicioExternoEntidad = (
            await self._servicio_externo_repositorio.obtener_por_id(servicio_externo_id)
        )
        servicio_externo.nombre = request.nombre
        servicio_externo.url = informacion_wms.url
        servicio_externo.atribucion = request.atribucion
        servicio_externo.grupo_capa_id = request.grupo_capa_id
        servicio_externo.capas = [
            ServicioExternoCapaEntidad(
                nombre=capa.nombre,
                titulo=capa.titulo,
                cuadro_delimitador=capa.cuadro_delimitador,
            )
            for capa in informacion_wms.capas
        ]
        servicio_externo.esta_habilitado = request.esta_habilitado
        servicio_externo.registrar_actualizacion(usuario_auditoria_id)
        return await self._servicio_externo_repositorio.actualizar(
            servicio_externo_id, servicio_externo
        )

    async def eliminar(
        self, servicio_externo_id: str, usuario_auditoria_id: str
    ) -> str:
        existe_servicio_externo: bool = (
            await self._servicio_externo_repositorio.verificar_existencia(
                servicio_externo_id
            )
        )
        if not existe_servicio_externo:
            raise AplicacionException(
                "El servicio externo no existe", status.HTTP_404_NOT_FOUND
            )
        return await self._servicio_externo_repositorio.eliminar(
            servicio_externo_id, usuario_auditoria_id
        )
