from typing import Optional

from app.aplicacion.parseadores.base_modelo import BaseModelo


class CrearTemaRequest(BaseModelo):
    codigo: str
    nombre: str
    descripcion: Optional[str]
    catalogo_id: str
