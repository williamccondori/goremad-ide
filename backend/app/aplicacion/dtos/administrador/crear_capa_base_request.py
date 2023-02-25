from pydantic import HttpUrl

from app.aplicacion.parseadores.base_modelo import BaseModelo


class CrearCapaBaseRequest(BaseModelo):
    nombre: str
    url: HttpUrl
    atribucion: str
    esta_habilitado: bool
