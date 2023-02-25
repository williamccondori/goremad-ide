from fastapi import APIRouter, Depends

from app.aplicacion.dtos.visor.obtener_todos_servicio_externo_usuario_response import \
    ObtenerTodosServicioExternoUsuarioResponse
from app.aplicacion.servicios.visor.usuario_servicio import UsuarioServicio
from app.infraestructura.oauth_2.autorizador import obtener_usuario_registrado
from app.infraestructura.oauth_2.modelos.usuario_registrado_modelo import UsuarioRegistradoModelo

usuario_controller = APIRouter()


@usuario_controller.get("/servicios-externos/", response_model=list[ObtenerTodosServicioExternoUsuarioResponse])
async def obtener_todos(
        usuario_servicio: UsuarioServicio = Depends(UsuarioServicio),
        usuario_registrado: UsuarioRegistradoModelo = Depends(obtener_usuario_registrado)) \
        -> list[ObtenerTodosServicioExternoUsuarioResponse]:
    """
    Obtiene todos los servicios externos que tiene el usuario.
    Args:
        usuario_servicio (UsuarioServicio): Servicio de usuario.
        usuario_registrado (UsuarioRegistradoModelo): Usuario registrado.
    Returns:
        Lista de servicios externos que tiene el usuario.
    """
    return await usuario_servicio.obtener_servicios_externos(usuario_registrado.id)
