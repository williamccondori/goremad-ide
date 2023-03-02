from datetime import datetime

from app.dominio.entidades.compartido.base_entidad import BaseEntidad


class ImagenSatelitalEntidad(BaseEntidad):
    id: str = None
    identificador: str
    identificador_sentinel_hub: str
    fecha: datetime
    tamanio: str
    descripcion: str
    coberturaAgua: float
    coberturaNubosidad: float
    coberturaVegetacion: float
    metadatos: dict
