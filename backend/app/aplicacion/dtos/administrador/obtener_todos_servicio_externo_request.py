from app.aplicacion.parseadores.base_modelo import BaseModelo


class ObtenerTodosServicioExternoRequest(BaseModelo):
    incluir_capas: bool = False
