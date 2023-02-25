from pydantic import HttpUrl

from app.aplicacion.parseadores.base_modelo import BaseModelo


class ObtenerInformacionWebMapServiceRequest(BaseModelo):
    """
    Modelo de peticion para obtener informacion de un servicio web map service.
    Attributes:
        url (HttpUrl): Url del servicio web map service.
    """

    url: HttpUrl
