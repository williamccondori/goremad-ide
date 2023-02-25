from app.aplicacion.parseadores.base_modelo import BaseModelo


class UsuarioRegistradoModelo(BaseModelo):
    id: str
    username: str
    roles: list[str] = []
