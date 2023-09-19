from typing import Optional

from app.dominio.entidades.compartido.base_entidad import BaseEntidad


class GrupoEntidad(BaseEntidad):
    id: str = None
    codigo: str
    nombre: str
    descripcion: Optional[str]
    tema_id: str
    esta_habilitado: bool
