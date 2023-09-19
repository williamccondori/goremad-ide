from typing import Optional

from app.dominio.entidades.compartido.base_entidad import BaseEntidad


class TemaEntidad(BaseEntidad):
    id: str = None
    codigo: str
    nombre: str
    descripcion: Optional[str]
    catalogo_id: str
    esta_habilitado: bool = True
