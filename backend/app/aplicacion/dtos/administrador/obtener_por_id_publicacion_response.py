from typing import Optional

from app.aplicacion.parseadores.base_modelo import BaseModelo


class ObtenerPorIdPublicacionResponse(BaseModelo):
    id: str
    tipo: str
    titulo: str
    resumen: str
    contenido: Optional[str]
    imagen: Optional[str]
    esta_habilitado: bool
