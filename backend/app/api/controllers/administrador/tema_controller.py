from app.aplicacion.dtos.administrador.actualizar_tema_request import ActualizarTemaRequest
from app.aplicacion.dtos.administrador.crear_tema_request import CrearTemaRequest
from app.aplicacion.dtos.administrador.obtener_por_id_tema_response import ObtenerPorIdTemaResponse
from app.aplicacion.dtos.administrador.obtener_todos_tema_response import ObtenerTodosTemaResponse
from fastapi import APIRouter, Depends

from app.aplicacion.servicios.administrador.tema_servicio import TemaServicio
from app.infraestructura.oauth_2.autorizador import obtener_usuario_registrado
from app.infraestructura.oauth_2.modelos.usuario_registrado_modelo import UsuarioRegistradoModelo

tema_controller = APIRouter()


@tema_controller.get("/", response_model=list[ObtenerTodosTemaResponse])
async def obtener_todos(
        tema_servicio: TemaServicio = Depends(TemaServicio),
        _: UsuarioRegistradoModelo = Depends(obtener_usuario_registrado)) -> list[ObtenerTodosTemaResponse]:
    return await tema_servicio.obtener_todos()


@tema_controller.get("/{tema_id}/", response_model=ObtenerPorIdTemaResponse)
async def obtener_por_id(
        tema_id: str,
        tema_servicio: TemaServicio = Depends(TemaServicio),
        _: UsuarioRegistradoModelo = Depends(obtener_usuario_registrado)) -> ObtenerPorIdTemaResponse:
    return await tema_servicio.obtener_por_id(tema_id)


@tema_controller.post("/", response_model=str)
async def crear(
        request: CrearTemaRequest,
        tema_servicio: TemaServicio = Depends(TemaServicio),
        usuario_registrado: UsuarioRegistradoModelo = Depends(obtener_usuario_registrado)) -> str:
    return await tema_servicio.crear(request, usuario_registrado.id)


@tema_controller.put("/{tema_id}/", response_model=str)
async def actualizar(
        tema_id: str,
        request: ActualizarTemaRequest,
        tema_servicio: TemaServicio = Depends(TemaServicio),
        usuario_registrado: UsuarioRegistradoModelo = Depends(obtener_usuario_registrado)) -> str:
    return await tema_servicio.actualizar(tema_id, request, usuario_registrado.id)


@tema_controller.delete("/{tema_id}/", response_model=str)
async def eliminar(
        tema_id: str,
        tema_servicio: TemaServicio = Depends(TemaServicio),
        usuario_registrado: UsuarioRegistradoModelo = Depends(obtener_usuario_registrado)) -> str:
    return await tema_servicio.eliminar(tema_id, usuario_registrado.id)
