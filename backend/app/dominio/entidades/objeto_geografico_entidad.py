from typing import Optional

from app.dominio.entidades.compartido.base_entidad import BaseEntidad


class ObjetoGeograficoEntidad(BaseEntidad):
    id: str = None
    codigo: str
    nombre: str
    descripcion: Optional[str]
    grupo_id: str
    esta_habilitado: bool
