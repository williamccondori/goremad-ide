from typing import Optional

from app.aplicacion.parseadores.base_modelo import BaseModelo


class ObtenerTodosConfiguracionResponse(BaseModelo):
    id: str
    nombre: str
    valor: Optional[str]
