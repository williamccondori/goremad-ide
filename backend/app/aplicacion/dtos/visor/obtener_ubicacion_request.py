from app.aplicacion.parseadores.base_modelo import BaseModelo


class ObtenerUbicacionRequest(BaseModelo):
    """
    Modelo de peticion para obtener ubicacion.
    Attributes:
        query (str): Ubicacion a buscar.
    """

    query: str
