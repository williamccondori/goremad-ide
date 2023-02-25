from app.aplicacion.parseadores.base_modelo import BaseModelo


class ObtenerPorIdCapaBaseResponse(BaseModelo):
    id: str
    nombre: str
    url: str
    atribucion: str
    esta_habilitado: bool
