from app.aplicacion.parseadores.base_modelo import BaseModelo


class ConsultarDetallesServicioRequest(BaseModelo):
    url: str
    capas: str
    cuadro_delimitador: str
    ancho: int
    alto: int
    x: int
    y: int
