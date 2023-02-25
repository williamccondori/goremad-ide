from app.aplicacion.parseadores.base_modelo import BaseModelo


class CapaResponse(BaseModelo):
    """
    Modelo de respuesta para obtener informacion de una capa de un servicio web map service.
    Informacion de una capa de un servicio web map service.
    Attributes:
        nombre (str): Nombre de la capa.
        titulo (str): Titulo de la capa.
    """

    nombre: str
    titulo: str


class ObtenerInformacionWebMapServiceResponse(BaseModelo):
    """
    Modelo de respuesta para obtener informacion de un servicio web map service.
    Attributes:
        url (str): Url del servicio web map service.
        nombre (str): Nombre del servicio web map service.
        titulo (str): Titulo del servicio web map service.
        version (str): Version del servicio web map service.
        descripcion (str): Descripcion del servicio web map service.
        palabras_clave (str): Palabras clave del servicio web map service.
        operaciones (list[str]): Lista de operaciones del servicio web map service.
        capas (list[CapaResponse]): Lista de capas del servicio web map service.
    """

    url: str
    nombre: str
    titulo: str
    version: str
    descripcion: str
    palabras_clave: list[str]
    operaciones: list[str]
    capas: list[CapaResponse] = []
