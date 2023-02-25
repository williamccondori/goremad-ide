from typing import Optional

from app.dominio.entidades.compartido.base_entidad import BaseEntidad


class UsuarioEntidad(BaseEntidad):
    id: str = None
    email: str
    username: str
    password: str
    nombres: Optional[str]
    apellidos: Optional[str]
    roles: list[str] = []
    esta_habilitado: bool
