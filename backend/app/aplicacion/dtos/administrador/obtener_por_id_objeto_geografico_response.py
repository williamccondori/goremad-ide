from typing import Optional

from app.aplicacion.parseadores.base_modelo import BaseModelo


class ObtenerPorIdObjetoGeograficoResponse(BaseModelo):
    id: str = None
    codigo: str
    nombre: str
    descripcion: Optional[str]
    grupo_id: str
