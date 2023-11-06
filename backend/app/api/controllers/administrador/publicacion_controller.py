from fastapi import APIRouter, Depends

from app.aplicacion.dtos.administrador.actualizar_publicacion_request import ActualizarPublicacionRequest
from app.aplicacion.dtos.administrador.crear_publicacion_request import CrearPublicacionRequest
from app.aplicacion.dtos.administrador.obtener_por_id_publicacion_response import ObtenerPorIdPublicacionResponse
from app.aplicacion.dtos.administrador.obtener_todos_publicacion_response import ObtenerTodosPublicacionResponse
from app.aplicacion.servicios.administrador.publicacion_servicio import PublicacionServicio
from app.infraestructura.oauth_2.autorizador import obtener_usuario_registrado
from app.infraestructura.oauth_2.modelos.usuario_registrado_modelo import UsuarioRegistradoModelo

publicacion_controller = APIRouter()


@publicacion_controller.get("/", response_model=list[ObtenerTodosPublicacionResponse])
async def obtener_todos(publicacion_servicio: PublicacionServicio = Depends(PublicacionServicio),
                        _: UsuarioRegistradoModelo = Depends(obtener_usuario_registrado)) -> list[
    ObtenerTodosPublicacionResponse]:
    return await publicacion_servicio.obtener_todos()


@publicacion_controller.get("/{publicacion_id}/", response_model=ObtenerPorIdPublicacionResponse)
async def obtener_por_id(
        publicacion_id: str,
        publicacion_servicio: PublicacionServicio = Depends(PublicacionServicio),
        _: UsuarioRegistradoModelo = Depends(obtener_usuario_registrado)) -> ObtenerPorIdPublicacionResponse:
    return await publicacion_servicio.obtener_por_id(publicacion_id)


@publicacion_controller.post("/", response_model=str)
async def crear(
        request: CrearPublicacionRequest,
        publicacion_servicio: PublicacionServicio = Depends(PublicacionServicio),
        usuario_registrado: UsuarioRegistradoModelo = Depends(obtener_usuario_registrado)) -> str:
    return await publicacion_servicio.crear(request, usuario_registrado.id)


@publicacion_controller.put("/{publicacion_id}/", response_model=str)
async def actualizar(
        publicacion_id: str,
        request: ActualizarPublicacionRequest,
        publicacion_servicio: PublicacionServicio = Depends(PublicacionServicio),
        usuario_registrado: UsuarioRegistradoModelo = Depends(obtener_usuario_registrado)) -> str:
    return await publicacion_servicio.actualizar(publicacion_id, request, usuario_registrado.id)


@publicacion_controller.delete("/{publicacion_id}/", response_model=str)
async def eliminar(
        publicacion_id: str,
        publicacion_servicio: PublicacionServicio = Depends(PublicacionServicio),
        usuario_registrado: UsuarioRegistradoModelo = Depends(obtener_usuario_registrado)) -> str:
    return await publicacion_servicio.eliminar(publicacion_id, usuario_registrado.id)
