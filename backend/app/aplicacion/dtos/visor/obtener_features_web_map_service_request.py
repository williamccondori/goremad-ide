from typing import Optional

from pydantic import HttpUrl

from app.aplicacion.parseadores.base_modelo import BaseModelo


class ObtenerFeaturesWebMapServiceRequest(BaseModelo):
    """
    Modelo de peticion para obtener features de un servicio web map service.
    Attributes:
        url (HttpUrl): Url del servicio web map service.
        x (int): Coordenada x del punto de referencia.
        y (int): Coordenada y del punto de referencia.
        width (int): Ancho del area de referencia.
        height (int): Alto del area de referencia.
        bounding_box (str): Bounding box del area de referencia.
        layers (str): Capas del servicio web map service.
        filtros (str): Filtros del servicio web map service.
    """

    url: HttpUrl
    x: int
    y: int
    width: int
    height: int
    bounding_box: str
    layers: str
    filtros: Optional[str] = None
