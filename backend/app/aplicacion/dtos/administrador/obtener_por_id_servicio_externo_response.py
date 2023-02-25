from typing import Optional

from app.aplicacion.parseadores.base_modelo import BaseModelo


class ObtenerPorIdServicioExternoResponse(BaseModelo):
    id: str
    url: str
    nombre: str
    atribucion: str
    grupo_capa_id: Optional[str]
    esta_habilitado: bool
