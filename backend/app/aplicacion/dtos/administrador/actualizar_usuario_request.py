from typing import Optional

from app.aplicacion.dtos.administrador.crear_usuario_request import CrearUsuarioRequest


class ActualizarUsuarioRequest(CrearUsuarioRequest):
    username: Optional[str]
    password: Optional[str]
