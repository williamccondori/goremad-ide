from app.aplicacion.parseadores.base_modelo import BaseModelo


class ObtenerUbicacionResponse(BaseModelo):
    """
    Modelo de respuesta para obtener ubicacion.
    Attributes:
        id (str): Id de la ubicacion.
        nombre (str): Nombre de la ubicacion.
        centro (list[float]): Centro de la ubicacion.
        zoom (int): Zoom de la ubicacion.
    """

    id: str
    nombre: str
    centro: list[float]
    zoom: int
