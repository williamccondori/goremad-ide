from fastapi import APIRouter, Depends

from app.aplicacion.dtos.administrador.actualizar_capa_base_request import ActualizarCapaBaseRequest
from app.aplicacion.dtos.administrador.crear_capa_base_request import CrearCapaBaseRequest
from app.aplicacion.dtos.administrador.obtener_por_id_capa_base_response import ObtenerPorIdCapaBaseResponse
from app.aplicacion.dtos.administrador.obtener_todos_capa_base_response import ObtenerTodosCapaBaseResponse
from app.aplicacion.servicios.administrador.capa_base_servicio import CapaBaseServicio
from app.infraestructura.oauth_2.autorizador import obtener_usuario_registrado
from app.infraestructura.oauth_2.modelos.usuario_registrado_modelo import UsuarioRegistradoModelo

capa_base_controller = APIRouter()


@capa_base_controller.get("/", response_model=list[ObtenerTodosCapaBaseResponse])
async def obtener_todos(
        capa_base_servicio: CapaBaseServicio = Depends(CapaBaseServicio),
        _: UsuarioRegistradoModelo = Depends(obtener_usuario_registrado)) -> list[ObtenerTodosCapaBaseResponse]:
    return await capa_base_servicio.obtener_todos()


@capa_base_controller.get("/{capa_base_id}/", response_model=ObtenerPorIdCapaBaseResponse)
async def obtener_por_id(
        capa_base_id: str,
        capa_base_servicio: CapaBaseServicio = Depends(CapaBaseServicio),
        _: UsuarioRegistradoModelo = Depends(obtener_usuario_registrado)) -> ObtenerPorIdCapaBaseResponse:
    return await capa_base_servicio.obtener_por_id(capa_base_id)


@capa_base_controller.post("/", response_model=str)
async def crear(
        request: CrearCapaBaseRequest,
        capa_base_servicio: CapaBaseServicio = Depends(CapaBaseServicio),
        usuario_registrado: UsuarioRegistradoModelo = Depends(obtener_usuario_registrado)) -> str:
    return await capa_base_servicio.crear(request, usuario_registrado.id)


@capa_base_controller.put("/{capa_base_id}/", response_model=str)
async def actualizar(
        capa_base_id: str,
        request: ActualizarCapaBaseRequest,
        capa_base_servicio: CapaBaseServicio = Depends(CapaBaseServicio),
        usuario_registrado: UsuarioRegistradoModelo = Depends(obtener_usuario_registrado)) -> str:
    return await capa_base_servicio.actualizar(capa_base_id, request, usuario_registrado.id)


@capa_base_controller.delete("/{capa_base_id}/", response_model=str)
async def eliminar(
        capa_base_id: str,
        capa_base_servicio: CapaBaseServicio = Depends(CapaBaseServicio),
        usuario_registrado: UsuarioRegistradoModelo = Depends(obtener_usuario_registrado)) -> str:
    return await capa_base_servicio.eliminar(capa_base_id, usuario_registrado.id)
