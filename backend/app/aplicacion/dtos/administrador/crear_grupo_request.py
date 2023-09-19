from typing import Optional

from app.aplicacion.parseadores.base_modelo import BaseModelo


class CrearGrupoRequest(BaseModelo):
    codigo: str
    nombre: str
    descripcion: Optional[str]
    tema_id: str
