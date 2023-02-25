from fastapi import APIRouter, Depends

from app.aplicacion.dtos.administrador.crear_publicacion_request import CrearPublicacionRequest
from app.aplicacion.dtos.administrador.obtener_todos_publicacion_response import ObtenerTodosPublicacionResponse
from app.aplicacion.servicios.administrador.publicacion_servicio import PublicacionServicio
from app.infraestructura.oauth_2.autorizador import obtener_usuario_registrado
from app.infraestructura.oauth_2.modelos.usuario_registrado_modelo import UsuarioRegistradoModelo

publicacion_controller = APIRouter()


@publicacion_controller.get("/", response_model=list[ObtenerTodosPublicacionResponse])
async def obtener_todos(
        publicacion_servicio: PublicacionServicio = Depends(PublicacionServicio),
        _: UsuarioRegistradoModelo = Depends(obtener_usuario_registrado)) -> list[ObtenerTodosPublicacionResponse]:
    return await publicacion_servicio.obtener_todos()


@publicacion_controller.post("/", response_model=str)
async def crear(
        request: CrearPublicacionRequest,
        publicacion_servicio: PublicacionServicio = Depends(PublicacionServicio),
        usuario_registrado: UsuarioRegistradoModelo = Depends(obtener_usuario_registrado)) -> str:
    return await publicacion_servicio.crear(request, usuario_registrado.id)
