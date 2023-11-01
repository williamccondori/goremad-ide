from typing import Optional

from pydantic import HttpUrl

from app.aplicacion.parseadores.base_modelo import BaseModelo


class CrearServicioExternoRequest(BaseModelo):
    url: HttpUrl
    nombre: str
    atribucion: str
    grupo_capa_id: Optional[str]
    filtros: Optional[str]
    esta_habilitado: bool
