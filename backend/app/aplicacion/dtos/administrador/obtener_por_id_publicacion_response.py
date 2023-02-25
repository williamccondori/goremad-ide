from typing import Optional

from app.aplicacion.parseadores.base_modelo import BaseModelo


class ObtenerPorIdPublicacionResponse(BaseModelo):
    id: str
    capa: str
    espacio_trabajo: str
    titulo: str
    es_consultable: bool
    esta_habilitado: bool
    grupo_capa_id: Optional[str]
