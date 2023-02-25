from typing import Optional

from app.dominio.entidades.compartido.base_entidad import BaseEntidad


class GrupoCapaEntidad(BaseEntidad):
    id: str = None
    nombre: str
    grupo_capa_id: Optional[str]
    esta_habilitado: bool
