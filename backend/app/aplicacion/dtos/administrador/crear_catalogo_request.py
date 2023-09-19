from typing import Optional

from app.aplicacion.parseadores.base_modelo import BaseModelo


class CrearCatalogoRequest(BaseModelo):
    codigo: str
    nombre: str
    descripcion: Optional[str]
