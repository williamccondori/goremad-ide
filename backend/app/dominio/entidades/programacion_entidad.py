from datetime import datetime
from typing import Optional

from app.dominio.entidades.compartido.base_entidad import BaseEntidad

PROGRAMACION_IMAGEN_SATELITAL = "imagen_satelital"

ESTADO_PENDIENTE = "pendiente"
ESTADO_TERMINADO = "terminado"
ESTADO_ERROR = "error"


class ProgramacionEntidad(BaseEntidad):
    id: str = None
    tipo: str
    fecha_inicio: datetime
    fecha_fin: Optional[str]
    estado_ejecucion: Optional[str]
    observaciones: Optional[str]
    usuario: str
