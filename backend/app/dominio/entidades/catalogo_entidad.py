from typing import Optional

from app.dominio.entidades.compartido.base_entidad import BaseEntidad


class CatalogoEntidad(BaseEntidad):
    id: str = None
    codigo: str
    nombre: str
    descripcion: Optional[str]
    esta_habilitado: bool = True
