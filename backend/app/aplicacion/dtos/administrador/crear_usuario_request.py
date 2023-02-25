from pydantic import EmailStr

from app.aplicacion.parseadores.base_modelo import BaseModelo


class CrearUsuarioRequest(BaseModelo):
    email: EmailStr
    username: str
    password: str
    nombres: str | None
    apellidos: str | None
    esta_habilitado: bool
