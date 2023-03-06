from app.aplicacion.dtos.visor.buscar_imagen_satelital_response import BuscarImagenSatelitalResponse
from app.aplicacion.dtos.visor.capa_response import CapaResponse
from app.aplicacion.parseadores.base_modelo import BaseModelo


class ImagenSatelitalPadreResponse(BuscarImagenSatelitalResponse):
    rgb: str
    ndvi: str
    ndwi: str


class ObtenerCapasImagenSatelitalResponse(BaseModelo):
    imagen_satelital: ImagenSatelitalPadreResponse
    capas: list[CapaResponse] = []
