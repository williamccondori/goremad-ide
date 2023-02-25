from app.aplicacion.parseadores.base_modelo import BaseModelo


class CrearCapaBaseRequest(BaseModelo):
    nombre: str
    url: str
    atribucion: str
    latitud: float
    longitud: float
    zoom: int
    esta_habilitado: bool
