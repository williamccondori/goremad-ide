from typing import Optional

from app.aplicacion.parseadores.base_modelo import BaseModelo


class CrearGrupoCapaRequest(BaseModelo):
    nombre: str
    grupo_capa_id: Optional[str]
    esta_habilitado: bool
