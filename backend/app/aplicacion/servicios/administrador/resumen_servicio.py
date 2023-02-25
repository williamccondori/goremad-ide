from fastapi import Depends

from app.aplicacion.dtos.administrador.obtener_totales_resumen_response import ObtenerTotalesResumenResponse
from app.dominio.entidades.compartido import base_entidad
from app.dominio.repositorios.capa_base_repositorio import ICapaBaseRepositorio
from app.dominio.repositorios.servicio_externo_repositorio import IServicioExternoRepositorio
from app.dominio.repositorios.usuario_repositorio import IUsuarioRepositorio
from app.infraestructura.mongo_db.repositorios.capa_base_repositorio import CapaBaseRepositorio
from app.infraestructura.mongo_db.repositorios.servicio_externo_repositorio import ServicioExternoRepositorio
from app.infraestructura.mongo_db.repositorios.usuario_repositorio import UsuarioRepositorio


class ResumenServicio:
    """
    Clase que contiene la logica de negocio para la administracion de la informacion del resumen.
    """

    def __init__(self,
                 servicio_externo_repositorio: IServicioExternoRepositorio = Depends(ServicioExternoRepositorio),
                 capa_base_repositorio: ICapaBaseRepositorio = Depends(CapaBaseRepositorio),
                 usuario_repositorio: IUsuarioRepositorio = Depends(UsuarioRepositorio)
                 ):
        self._servicio_externo_repositorio = servicio_externo_repositorio
        self._capa_base_repositorio = capa_base_repositorio
        self._usuario_repositorio = usuario_repositorio

    async def obtener_totales(self) -> ObtenerTotalesResumenResponse:
        """
        Obtiene los totales de los servicios externos, capas base, usuarios y subproyectos.
        Returns:
            ObtenerTotalesResumenResponse: Resumen de los totales de los servicios externos, capas base, usuarios y
            subproyectos.
        """
        # Obtener totales de servicios externos.
        total_servicios_externos = await self._servicio_externo_repositorio.contar({
            "estado": base_entidad.ESTADO_ACTIVO
        })
        # Obtener totales de capas base.
        total_capas_base = await self._capa_base_repositorio.contar({
            "estado": base_entidad.ESTADO_ACTIVO
        })
        # Obtener totales de usuarios.
        total_usuarios: int = await self._usuario_repositorio.contar({
            "estado": base_entidad.ESTADO_ACTIVO
        })
        return ObtenerTotalesResumenResponse(
            total_servicios_locales=0,
            total_servicios_externos=total_servicios_externos,
            total_capas_base=total_capas_base,
            total_usuarios=total_usuarios
        )
