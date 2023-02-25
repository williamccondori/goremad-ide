from app.aplicacion.parseadores.base_modelo import BaseModelo


class ActualizarRolUsuarioRequest(BaseModelo):
    esAdministrador: bool
    esUsuario: bool
