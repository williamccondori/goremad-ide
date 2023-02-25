from typing import Optional

from app.aplicacion.parseadores.base_modelo import BaseModelo


class ObtenerCoordenadaRequest(BaseModelo):
    proyeccion: str
    datum: str
    zona: Optional[int]
    x: float
    y: float
