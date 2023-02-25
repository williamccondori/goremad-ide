from app.aplicacion.parseadores.base_modelo import BaseModelo


class ObtenerPorIdUsuarioResponse(BaseModelo):
    id: str
    email: str
    username: str
    nombres: str | None
    apellidos: str | None
    roles: list[str] = []
    esta_habilitado: bool
