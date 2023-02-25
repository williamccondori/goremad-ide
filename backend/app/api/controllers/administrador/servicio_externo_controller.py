from fastapi import APIRouter, Depends

from app.aplicacion.dtos.administrador.actualizar_servicio_externo_request import ActualizarServicioExternoRequest
from app.aplicacion.dtos.administrador.crear_servicio_externo_request import CrearServicioExternoRequest
from app.aplicacion.dtos.administrador.obtener_por_id_servicio_externo_response import \
    ObtenerPorIdServicioExternoResponse
from app.aplicacion.dtos.administrador.obtener_todos_servicio_externo_request import ObtenerTodosServicioExternoRequest
from app.aplicacion.dtos.administrador.obtener_todos_servicio_externo_response import \
    ObtenerTodosServicioExternoResponse
from app.aplicacion.servicios.administrador.servicio_externo_servicio import ServicioExternoServicio
from app.infraestructura.oauth_2.autorizador import obtener_usuario_registrado
from app.infraestructura.oauth_2.modelos.usuario_registrado_modelo import UsuarioRegistradoModelo

servicio_externo_controller = APIRouter()


@servicio_externo_controller.get("/", response_model=list[ObtenerTodosServicioExternoResponse])
async def obtener_todos(
        obtener_todos_servicio_externo_request: ObtenerTodosServicioExternoRequest = Depends(),
        servicio_externo_servicio: ServicioExternoServicio = Depends(ServicioExternoServicio),
        _: UsuarioRegistradoModelo = Depends(obtener_usuario_registrado)) -> list[ObtenerTodosServicioExternoResponse]:
    return await servicio_externo_servicio.obtener_todos(obtener_todos_servicio_externo_request)


@servicio_externo_controller.get("/{servicio_externo_id}/", response_model=ObtenerPorIdServicioExternoResponse)
async def obtener_por_id(
        servicio_externo_id: str,
        servicio_externo_servicio: ServicioExternoServicio = Depends(ServicioExternoServicio),
        _: UsuarioRegistradoModelo = Depends(obtener_usuario_registrado)) -> ObtenerPorIdServicioExternoResponse:
    return await servicio_externo_servicio.obtener_por_id(servicio_externo_id)


@servicio_externo_controller.post("/", response_model=str)
async def crear(
        request: CrearServicioExternoRequest,
        servicio_externo_servicio: ServicioExternoServicio = Depends(ServicioExternoServicio),
        usuario_registrado: UsuarioRegistradoModelo = Depends(obtener_usuario_registrado)) -> str:
    return await servicio_externo_servicio.crear(request, usuario_registrado.id)


@servicio_externo_controller.put("/{servicio_externo_id}/", response_model=str)
async def actualizar(
        servicio_externo_id: str,
        request: ActualizarServicioExternoRequest,
        servicio_externo_servicio: ServicioExternoServicio = Depends(ServicioExternoServicio),
        usuario_registrado: UsuarioRegistradoModelo = Depends(obtener_usuario_registrado)) -> str:
    return await servicio_externo_servicio.actualizar(servicio_externo_id, request, usuario_registrado.id)


@servicio_externo_controller.delete("/{servicio_externo_id}/", response_model=str)
async def eliminar(
        servicio_externo_id: str,
        servicio_externo_servicio: ServicioExternoServicio = Depends(ServicioExternoServicio),
        usuario_registrado: UsuarioRegistradoModelo = Depends(obtener_usuario_registrado)) -> str:
    return await servicio_externo_servicio.eliminar(servicio_externo_id, usuario_registrado.id)
