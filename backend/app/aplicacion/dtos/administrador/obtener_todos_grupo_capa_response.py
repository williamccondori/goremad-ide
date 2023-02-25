from typing import Optional

from app.aplicacion.parseadores.base_modelo import BaseModelo


class ObtenerTodosGrupoCapaResponse(BaseModelo):
    id: str
    nombre: str
    grupo_capa: Optional[str]
    grupo_capa_id: Optional[str]
    esta_habilitado: bool
