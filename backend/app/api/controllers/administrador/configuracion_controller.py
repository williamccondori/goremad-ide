from fastapi import APIRouter, Depends

from app.aplicacion.dtos.administrador.actualizar_todos_configuracion_request import ActualizarTodosConfiguracionRequest
from app.aplicacion.dtos.administrador.obtener_todos_configuracion_response import ObtenerTodosConfiguracionResponse
from app.aplicacion.servicios.administrador.configuracion_servicio import ConfiguracionServicio
from app.infraestructura.oauth_2.autorizador import obtener_usuario_registrado
from app.infraestructura.oauth_2.modelos.usuario_registrado_modelo import UsuarioRegistradoModelo

configuracion_controller = APIRouter()


@configuracion_controller.get("/", response_model=list[ObtenerTodosConfiguracionResponse])
async def obtener_todos(
        configuracion_servicio: ConfiguracionServicio = Depends(ConfiguracionServicio),
        _: UsuarioRegistradoModelo = Depends(obtener_usuario_registrado)) \
        -> list[ObtenerTodosConfiguracionResponse]:
    return await configuracion_servicio.obtener_todos()


@configuracion_controller.put("/", response_model=str)
async def actualizar_todos(
        request: ActualizarTodosConfiguracionRequest,
        usuario_servicio: ConfiguracionServicio = Depends(ConfiguracionServicio),
        usuario_registrado: UsuarioRegistradoModelo = Depends(obtener_usuario_registrado)) -> str:
    return await usuario_servicio.actualizar_todos(request, usuario_registrado.id)
