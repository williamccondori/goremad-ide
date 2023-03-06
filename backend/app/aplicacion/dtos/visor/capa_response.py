from typing import Optional

from app.aplicacion.parseadores.base_modelo import BaseModelo


class CapaResponse(BaseModelo):
    id: str
    servicio_id: str
    servicio_titulo: str
    nombre: str
    titulo: str
    url: str
    url_leyenda: str
    atribucion: str
    cuadro_delimitador: list[float]
    grupo_capa_id: Optional[str]
    transparencia: int
