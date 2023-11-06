from typing import Optional

from app.aplicacion.parseadores.base_modelo import BaseModelo


class CrearPublicacionRequest(BaseModelo):
    tipo: str
    titulo: str
    resumen: str
    contenido: Optional[str]
    imagen: Optional[str]
    esta_habilitado: bool
