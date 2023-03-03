from datetime import datetime

from app.aplicacion.parseadores.base_modelo import BaseModelo


class ObtenerPorIdImagenSatelitalResponse(BaseModelo):
    id: str
    identificador: str
    imagen_url: str
    identificador_sentinel_hub: str
    fecha: datetime
    tamanio: str
    descripcion: str
    coberturaAgua: float
    coberturaNubosidad: float
    coberturaVegetacion: float
    metadatos: dict
