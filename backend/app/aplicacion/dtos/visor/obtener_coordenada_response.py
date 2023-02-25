from app.aplicacion.parseadores.base_modelo import BaseModelo


class ObtenerCoordenadaResponse(BaseModelo):
    latitud: float
    longitud: float