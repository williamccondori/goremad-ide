from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from app.aplicacion.dtos.administrador.iniciar_sesion_response import IniciarSesionResponse
from app.aplicacion.servicios.administrador.autenticacion_servicio import AutenticacionServicio
from app.infraestructura.oauth_2.autorizador import obtener_usuario_registrado
from app.infraestructura.oauth_2.modelos.usuario_registrado_modelo import UsuarioRegistradoModelo

autenticacion_controller = APIRouter()


@autenticacion_controller.post("/", response_model=IniciarSesionResponse)
async def iniciar_sesion(request: OAuth2PasswordRequestForm = Depends(),
                         autenticacion_servicio: AutenticacionServicio = Depends(
                             AutenticacionServicio)) -> IniciarSesionResponse:
    return await autenticacion_servicio.iniciar_sesion(request)


@autenticacion_controller.get("/user/", response_model=UsuarioRegistradoModelo)
async def obtener_usuario_registrado(
        usuario_registrado: UsuarioRegistradoModelo = Depends(obtener_usuario_registrado)) -> UsuarioRegistradoModelo:
    return usuario_registrado
