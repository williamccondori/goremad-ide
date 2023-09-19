from fastapi import Depends

from app.aplicacion.dtos.administrador.obtener_totales_resumen_response import (
    ObtenerTotalesResumenResponse,
)
from app.dependencies import registrar_repo_capa_base
from app.dominio.entidades.compartido import base_entidad
from app.dominio.repositorios.base_repositorio import IBaseRepositorio
from app.dominio.repositorios.servicio_externo_repositorio import (
    IServicioExternoRepositorio,
)
from app.dominio.repositorios.usuario_repositorio import IUsuarioRepositorio

from app.infraestructura.mongo_db.repositorios.servicio_externo_repositorio import (
    ServicioExternoRepositorio,
)
from app.infraestructura.mongo_db.repositorios.usuario_repositorio import (
    UsuarioRepositorio,
)


class ResumenServicio:
    def __init__(
        self,
        servicio_externo_repositorio: IServicioExternoRepositorio = Depends(
            ServicioExternoRepositorio
        ),
        capa_base_repositorio: IBaseRepositorio = Depends(registrar_repo_capa_base),
        usuario_repositorio: IUsuarioRepositorio = Depends(UsuarioRepositorio),
    ):
        self._servicio_externo_repositorio = servicio_externo_repositorio
        self._capa_base_repositorio = capa_base_repositorio
        self._usuario_repositorio = usuario_repositorio

    async def obtener_totales(self) -> ObtenerTotalesResumenResponse:
        # Obtener totales de servicios externos.
        total_servicios_externos = await self._servicio_externo_repositorio.contar(
            {"estado": base_entidad.ESTADO_ACTIVO}
        )
        # Obtener totales de capas base.
        total_capas_base = await self._capa_base_repositorio.contar(
            {"estado": base_entidad.ESTADO_ACTIVO}
        )
        # Obtener totales de usuarios.
        total_usuarios: int = await self._usuario_repositorio.contar(
            {"estado": base_entidad.ESTADO_ACTIVO}
        )
        return ObtenerTotalesResumenResponse(
            total_servicios_locales=0,
            total_servicios_externos=total_servicios_externos,
            total_capas_base=total_capas_base,
            total_usuarios=total_usuarios,
        )
