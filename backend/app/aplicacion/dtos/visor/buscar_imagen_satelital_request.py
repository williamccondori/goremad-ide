from datetime import datetime
from typing import Optional

from app.aplicacion.parseadores.base_modelo import BaseModelo


class BuscarImagenSatelitalRequest(BaseModelo):
    identificador: Optional[str]
    satelite: Optional[str]
    fecha_inicio: datetime = datetime.now()
    fecha_fin: datetime = datetime.now()
