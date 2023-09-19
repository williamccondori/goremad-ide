from typing import Optional

from app.aplicacion.parseadores.base_modelo import BaseModelo


class ObtenerPorIdGrupoResponse(BaseModelo):
    id: str
    codigo: str
    nombre: str
    descripcion: Optional[str]
    tema_id: str
