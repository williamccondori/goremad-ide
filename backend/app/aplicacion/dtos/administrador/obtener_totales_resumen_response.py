from app.aplicacion.parseadores.base_modelo import BaseModelo


class ObtenerTotalesResumenResponse(BaseModelo):
    total_servicios_locales: int
    total_servicios_externos: int
    total_capas_base: int
    total_usuarios: int
