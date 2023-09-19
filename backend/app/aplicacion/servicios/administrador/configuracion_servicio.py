from fastapi import Depends
from starlette import status

from app.aplicacion.dtos.administrador.actualizar_todos_configuracion_request import (
    ActualizarTodosConfiguracionRequest,
)
from app.aplicacion.dtos.administrador.obtener_todos_configuracion_response import (
    ObtenerTodosConfiguracionResponse,
)
from app.aplicacion.utilidades import constantes
from app.dominio.entidades.compartido import base_entidad
from app.dominio.entidades.configuracion_entidad import ConfiguracionEntidad
from app.dominio.excepciones.aplicacion_exception import AplicacionException
from app.dominio.repositorios.capa_base_repositorio import ICapaBaseRepositorio
from app.dominio.repositorios.configuracion_repositorio import IConfiguracionRepositorio
from app.infraestructura.mongo_db.repositorios.capa_base_repositorio import (
    CapaBaseRepositorio,
)
from app.infraestructura.mongo_db.repositorios.configuracion_repositorio import (
    ConfiguracionRepositorio,
)


class ConfiguracionServicio:
    """
    Clase que contiene la logica de negocio para la administracion de configuraciones.
    """

    def __init__(
        self,
        configuracion_repositorio: IConfiguracionRepositorio = Depends(
            ConfiguracionRepositorio
        ),
        capa_base_repositorio: ICapaBaseRepositorio = Depends(CapaBaseRepositorio),
    ):
        self._configuracion_repositorio = configuracion_repositorio
        self._capa_base_repositorio = capa_base_repositorio

    async def obtener_todos(self) -> list[ObtenerTodosConfiguracionResponse]:
        """
        Obtiene todas las configuraciones activas.
        Returns:
            list[ObtenerTodosConfiguracionResponse]: Lista de configuraciones activas.
        """
        configuraciones: list[
            ConfiguracionEntidad
        ] = await self._configuracion_repositorio.obtener_todos(
            {"estado": base_entidad.ESTADO_ACTIVO}
        )
        return [
            ObtenerTodosConfiguracionResponse(**configuracion.dict())
            for configuracion in configuraciones
        ]

    async def actualizar(
        self, configuracion_id: str, valor: str, usuario_auditoria_id: str
    ) -> str:
        """
        Actualiza el valor de una configuracion.
        Args:
            configuracion_id (str): Identificador de la configuracion.
            valor (str): Valor de la configuracion.
            usuario_auditoria_id (str): Identificador del usuario que realiza la actualizacion.
        Returns:
            str: Identificador de la configuracion actualizada.
        """
        configuracion = await self._configuracion_repositorio.obtener_por_id(
            configuracion_id
        )
        configuracion.valor = valor
        configuracion.registrar_actualizacion(usuario_auditoria_id)
        return await self._configuracion_repositorio.actualizar(
            configuracion.id, configuracion
        )

    async def actualizar_todos(
        self, request: ActualizarTodosConfiguracionRequest, usuario_auditoria_id: str
    ) -> str:
        """
        Actualiza todas las configuraciones.
        Args:
            request (ActualizarTodosConfiguracionRequest): Informacion de las configuraciones a actualizar.
            usuario_auditoria_id (str): Identificador del usuario que realiza la actualizacion.
        Returns:
            str: Identificadores de las configuraciones actualizadas separados por coma.
        """
        configuraciones: list[
            ConfiguracionEntidad
        ] = await self._configuracion_repositorio.obtener_todos(
            {"estado": base_entidad.ESTADO_ACTIVO}
        )
        configuraciones_actualizadas: list[str] = []
        for configuracion in configuraciones:
            # Nombre de la empresa.
            if configuracion.nombre == "nombre_empresa":
                configuracion_id: str = await self.actualizar(
                    configuracion.id, request.nombre_empresa, usuario_auditoria_id
                )
                configuraciones_actualizadas.append(configuracion_id)
            # Latitud inicial.
            elif configuracion.nombre == "latitud_inicial":
                # Validacion del rango de la latitud.
                if request.latitud_inicial < -90 or request.latitud_inicial > 90:
                    raise AplicacionException(
                        "La latitud inicial debe estar entre -90 y 90"
                    )
                configuracion_id: str = await self.actualizar(
                    configuracion.id, str(request.latitud_inicial), usuario_auditoria_id
                )
                configuraciones_actualizadas.append(configuracion_id)
            # Longitud inicial
            elif configuracion.nombre == "longitud_inicial":
                # Validacion del rango de la longitud.
                if request.longitud_inicial < -180 or request.longitud_inicial > 180:
                    raise AplicacionException(
                        "La longitud inicial debe estar entre -180 y 180"
                    )
                configuracion_id: str = await self.actualizar(
                    configuracion.id,
                    str(request.longitud_inicial),
                    usuario_auditoria_id,
                )
                configuraciones_actualizadas.append(configuracion_id)
            # Zoom inicial.
            elif configuracion.nombre == "zoom_inicial":
                # Validacion del rango del zoom.
                if request.zoom_inicial < 0 or request.zoom_inicial > 20:
                    raise AplicacionException("El zoom inicial debe estar entre 0 y 20")
                configuracion_id: str = await self.actualizar(
                    configuracion.id, str(request.zoom_inicial), usuario_auditoria_id
                )
                configuraciones_actualizadas.append(configuracion_id)
            # Capa base inicial.
            elif configuracion.nombre == "capa_base_incial_id":
                # Validacion de la capa base inicial, no puede estar vacio.
                if request.capa_base_inicial_id == constantes.CADENA_VACIA:
                    raise AplicacionException(
                        "La capa base inicial no puede estar vacío (puede ser NULO)",
                        status.HTTP_400_BAD_REQUEST,
                    )
                # Validacion de la capa base inicial, debe existir.
                if request.capa_base_inicial_id:
                    existe_capa_base: bool = (
                        await self._capa_base_repositorio.verificar_existencia(
                            request.capa_base_inicial_id
                        )
                    )
                    if not existe_capa_base:
                        raise AplicacionException(
                            "La capa base inicial seleccionada no existe"
                        )
                configuracion_id: str = await self.actualizar(
                    configuracion.id, request.capa_base_inicial_id, usuario_auditoria_id
                )
                configuraciones_actualizadas.append(configuracion_id)
            # Servicios externos activos.
            elif configuracion.nombre == "servicios_externos_activos":
                configuracion_id: str = await self.actualizar(
                    configuracion.id,
                    request.servicios_externos_activos,
                    usuario_auditoria_id,
                )
                configuraciones_actualizadas.append(configuracion_id)
        return ",".join(configuraciones_actualizadas)
