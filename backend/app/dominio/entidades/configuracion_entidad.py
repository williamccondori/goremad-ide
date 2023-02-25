from typing import Optional

from app.dominio.entidades.compartido.base_entidad import BaseEntidad


class ConfiguracionEntidad(BaseEntidad):
    id: str = None
    nombre: str
    valor: Optional[str]
