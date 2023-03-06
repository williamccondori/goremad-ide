from typing import Optional

from app.aplicacion.parseadores.base_modelo import BaseModelo


class ObtenerActualProgramacionResponse(BaseModelo):
    id: str
    tipo: str
    fecha_inicio: str
    fecha_fin: Optional[str]
    estado_ejecucion: str
    observaciones: Optional[str]
    usuario: str
