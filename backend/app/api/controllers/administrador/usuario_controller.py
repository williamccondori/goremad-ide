from fastapi import APIRouter, Depends

from app.aplicacion.dtos.administrador.actualizar_rol_usuario_request import ActualizarRolUsuarioRequest
from app.aplicacion.dtos.administrador.actualizar_usuario_request import ActualizarUsuarioRequest
from app.aplicacion.dtos.administrador.crear_superusuario_request import CrearSuperusuarioRequest
from app.aplicacion.dtos.administrador.crear_usuario_request import CrearUsuarioRequest
from app.aplicacion.dtos.administrador.obtener_por_id_usuario_response import ObtenerPorIdUsuarioResponse
from app.aplicacion.dtos.administrador.obtener_todos_usuario_response import ObtenerTodosUsuarioResponse
from app.aplicacion.servicios.administrador.usuario_servicio import UsuarioServicio
from app.infraestructura.oauth_2.autorizador import obtener_usuario_registrado
from app.infraestructura.oauth_2.modelos.usuario_registrado_modelo import UsuarioRegistradoModelo

usuario_controller = APIRouter()


@usuario_controller.get("/", response_model=list[ObtenerTodosUsuarioResponse])
async def obtener_todos(
        usuario_servicio: UsuarioServicio = Depends(UsuarioServicio),
        _: UsuarioRegistradoModelo = Depends(obtener_usuario_registrado)) -> list[ObtenerTodosUsuarioResponse]:
    return await usuario_servicio.obtener_todos()


@usuario_controller.get("/{usuario_id}/", response_model=ObtenerPorIdUsuarioResponse)
async def obtener_por_id(
        usuario_id: str,
        usuario_servicio: UsuarioServicio = Depends(UsuarioServicio),
        _: UsuarioRegistradoModelo = Depends(obtener_usuario_registrado)) -> ObtenerPorIdUsuarioResponse:
    return await usuario_servicio.obtener_por_id(usuario_id)


@usuario_controller.post("/", response_model=str)
async def crear(
        request: CrearUsuarioRequest,
        usuario_servicio: UsuarioServicio = Depends(UsuarioServicio),
        usuario_registrado: UsuarioRegistradoModelo = Depends(obtener_usuario_registrado)) -> str:
    return await usuario_servicio.crear(request, usuario_registrado.id)


@usuario_controller.post("/superusuarios/", response_model=str)
async def crear_superusuario(
        request: CrearSuperusuarioRequest,
        usuario_servicio: UsuarioServicio = Depends(UsuarioServicio)) -> str:
    return await usuario_servicio.crear_superusuario(request)


@usuario_controller.put("/{usuario_id}/", response_model=str)
async def actualizar(
        usuario_id: str,
        request: ActualizarUsuarioRequest,
        usuario_servicio: UsuarioServicio = Depends(UsuarioServicio),
        usuario_registrado: UsuarioRegistradoModelo = Depends(obtener_usuario_registrado)) -> str:
    return await usuario_servicio.actualizar(usuario_id, request, usuario_registrado.id)


@usuario_controller.delete("/{usuario_id}/", response_model=str)
async def eliminar(
        usuario_id: str,
        usuario_servicio: UsuarioServicio = Depends(UsuarioServicio),
        usuario_registrado: UsuarioRegistradoModelo = Depends(obtener_usuario_registrado)) -> str:
    return await usuario_servicio.eliminar(usuario_id, usuario_registrado.id)


@usuario_controller.put("/{usuario_id}/roles/", response_model=str)
async def actualizar_rol(
        usuario_id: str,
        request: ActualizarRolUsuarioRequest,
        usuario_servicio: UsuarioServicio = Depends(UsuarioServicio),
        usuario_registrado: UsuarioRegistradoModelo = Depends(obtener_usuario_registrado)) -> str:
    return await usuario_servicio.actualizar_rol(usuario_id, request, usuario_registrado.id)
