from app.aplicacion.dtos.administrador.crear_catalogo_request import CrearCatalogoRequest
from app.aplicacion.dtos.administrador.obtener_por_id_catalogo_response import ObtenerPorIdCatalogoResponse
from app.aplicacion.dtos.administrador.obtener_todos_catalogo_response import ObtenerTodosCatalogoResponse
from fastapi import APIRouter, Depends

from app.aplicacion.dtos.administrador.actualizar_catalogo_request import ActualizarCatalogoRequest
from app.aplicacion.servicios.administrador.catalogo_servicio import CatalogoServicio
from app.infraestructura.oauth_2.autorizador import obtener_usuario_registrado
from app.infraestructura.oauth_2.modelos.usuario_registrado_modelo import UsuarioRegistradoModelo

catalogo_controller = APIRouter()


@catalogo_controller.get("/", response_model=list[ObtenerTodosCatalogoResponse])
async def obtener_todos(
        catalogo_servicio: CatalogoServicio = Depends(CatalogoServicio),
        _: UsuarioRegistradoModelo = Depends(obtener_usuario_registrado)) -> list[ObtenerTodosCatalogoResponse]:
    return await catalogo_servicio.obtener_todos()


@catalogo_controller.get("/{catalogo_id}/", response_model=ObtenerPorIdCatalogoResponse)
async def obtener_por_id(
        catalogo_id: str,
        catalogo_servicio: CatalogoServicio = Depends(CatalogoServicio),
        _: UsuarioRegistradoModelo = Depends(obtener_usuario_registrado)) -> ObtenerPorIdCatalogoResponse:
    return await catalogo_servicio.obtener_por_id(catalogo_id)


@catalogo_controller.post("/", response_model=str)
async def crear(
        request: CrearCatalogoRequest,
        catalogo_servicio: CatalogoServicio = Depends(CatalogoServicio),
        usuario_registrado: UsuarioRegistradoModelo = Depends(obtener_usuario_registrado)) -> str:
    return await catalogo_servicio.crear(request, usuario_registrado.id)


@catalogo_controller.put("/{catalogo_id}/", response_model=str)
async def actualizar(
        catalogo_id: str,
        request: ActualizarCatalogoRequest,
        catalogo_servicio: CatalogoServicio = Depends(CatalogoServicio),
        usuario_registrado: UsuarioRegistradoModelo = Depends(obtener_usuario_registrado)) -> str:
    return await catalogo_servicio.actualizar(catalogo_id, request, usuario_registrado.id)


@catalogo_controller.delete("/{catalogo_id}/", response_model=str)
async def eliminar(
        catalogo_id: str,
        catalogo_servicio: CatalogoServicio = Depends(CatalogoServicio),
        usuario_registrado: UsuarioRegistradoModelo = Depends(obtener_usuario_registrado)) -> str:
    return await catalogo_servicio.eliminar(catalogo_id, usuario_registrado.id)
