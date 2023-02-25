from typing import Optional

from app.aplicacion.parseadores.base_modelo import BaseModelo


class ActualizarTodosConfiguracionRequest(BaseModelo):
    nombre_empresa: str
    latitud_inicial: float
    longitud_inicial: float
    zoom_inicial: int
    capa_base_inicial_id: Optional[str]
    servicios_externos_activos: Optional[str]
