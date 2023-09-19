from app.aplicacion.dtos.administrador.actualizar_grupo_request import ActualizarGrupoRequest
from app.aplicacion.dtos.administrador.crear_grupo_request import CrearGrupoRequest
from app.aplicacion.dtos.administrador.obtener_por_id_grupo_response import ObtenerPorIdGrupoResponse
from app.aplicacion.dtos.administrador.obtener_todos_grupo_response import ObtenerTodosGrupoResponse
from fastapi import APIRouter, Depends

from app.aplicacion.servicios.administrador.grupo_servicio import GrupoServicio
from app.infraestructura.oauth_2.autorizador import obtener_usuario_registrado
from app.infraestructura.oauth_2.modelos.usuario_registrado_modelo import UsuarioRegistradoModelo

grupo_controller = APIRouter()


@grupo_controller.get("/", response_model=list[ObtenerTodosGrupoResponse])
async def obtener_todos(
        grupo_servicio: GrupoServicio = Depends(GrupoServicio),
        _: UsuarioRegistradoModelo = Depends(obtener_usuario_registrado)) -> list[ObtenerTodosGrupoResponse]:
    return await grupo_servicio.obtener_todos()


@grupo_controller.get("/{grupo_id}/", response_model=ObtenerPorIdGrupoResponse)
async def obtener_por_id(
        grupo_id: str,
        grupo_servicio: GrupoServicio = Depends(GrupoServicio),
        _: UsuarioRegistradoModelo = Depends(obtener_usuario_registrado)) -> ObtenerPorIdGrupoResponse:
    return await grupo_servicio.obtener_por_id(grupo_id)


@grupo_controller.post("/", response_model=str)
async def crear(
        request: CrearGrupoRequest,
        grupo_servicio: GrupoServicio = Depends(GrupoServicio),
        usuario_registrado: UsuarioRegistradoModelo = Depends(obtener_usuario_registrado)) -> str:
    return await grupo_servicio.crear(request, usuario_registrado.id)


@grupo_controller.put("/{grupo_id}/", response_model=str)
async def actualizar(
        grupo_id: str,
        request: ActualizarGrupoRequest,
        grupo_servicio: GrupoServicio = Depends(GrupoServicio),
        usuario_registrado: UsuarioRegistradoModelo = Depends(obtener_usuario_registrado)) -> str:
    return await grupo_servicio.actualizar(grupo_id, request, usuario_registrado.id)


@grupo_controller.delete("/{grupo_id}/", response_model=str)
async def eliminar(
        grupo_id: str,
        grupo_servicio: GrupoServicio = Depends(GrupoServicio),
        usuario_registrado: UsuarioRegistradoModelo = Depends(obtener_usuario_registrado)) -> str:
    return await grupo_servicio.eliminar(grupo_id, usuario_registrado.id)
