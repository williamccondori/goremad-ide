from datetime import datetime
from typing import Optional

import pydantic
from pydantic import BaseModel

ESTADO_ACTIVO = True


class BaseEntidad(BaseModel):
    usuario_creacion: str = None
    usuario_modificacion: Optional[str]
    fecha_creacion: datetime = None
    fecha_modificacion: Optional[datetime]
    estado: bool = True

    def registrar_creacion(self, usuario_id):
        self.estado = ESTADO_ACTIVO
        self.usuario_creacion = usuario_id
        self.fecha_creacion = datetime.now()

    def registrar_actualizacion(self, usuario_id):
        self.usuario_modificacion = usuario_id
        self.fecha_modificacion = datetime.now()

    class Config:
        orm_mode = True
        extra = pydantic.Extra.forbid
        anystr_strip_whitespace = True
