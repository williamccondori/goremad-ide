from typing import Optional

import pydantic
from pydantic import BaseModel

from app.dominio.entidades.compartido.base_entidad import BaseEntidad


class CapaEntidad(BaseModel):
    nombre: str
    titulo: str
    cuadro_delimitador: list[float]

    class Config:
        orm_mode = True
        extra = pydantic.Extra.forbid
        anystr_strip_whitespace = True


class ServicioEntidad(BaseEntidad):
    id: str = None
    url: str
    nombre: str
    atribucion: str
    grupo_capa_id: Optional[str]
    capas: list[CapaEntidad]
    opacidad: float
    es_consultable: bool
    esta_habilitado: bool
