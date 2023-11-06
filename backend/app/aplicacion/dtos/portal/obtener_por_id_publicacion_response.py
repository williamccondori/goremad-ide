from typing import Optional

from app.aplicacion.parseadores.base_modelo import BaseModelo


class ObtenerPorIdPublicacionResponse(BaseModelo):
    id: str
    titulo: str
    resumen: str
    contenido: Optional[str]
    imagen: Optional[str]
