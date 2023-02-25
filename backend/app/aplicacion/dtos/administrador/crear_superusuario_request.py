from app.aplicacion.dtos.administrador.crear_usuario_request import CrearUsuarioRequest


class CrearSuperusuarioRequest(CrearUsuarioRequest):
    llave_secreta: str
