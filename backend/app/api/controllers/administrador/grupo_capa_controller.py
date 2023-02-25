from fastapi import APIRouter, Depends

from app.aplicacion.dtos.administrador.actualizar_grupo_capa_request import ActualizarGrupoCapaRequest
from app.aplicacion.dtos.administrador.crear_grupo_capa_request import CrearGrupoCapaRequest
from app.aplicacion.dtos.administrador.obtener_estructura_grupo_capa_response import ObtenerEstructuraGrupoCapaResponse
from app.aplicacion.dtos.administrador.obtener_por_id_grupo_capa_response import ObtenerPorIdGrupoCapaResponse
from app.aplicacion.dtos.administrador.obtener_todos_grupo_capa_response import ObtenerTodosGrupoCapaResponse
from app.aplicacion.servicios.administrador.grupo_capa_servicio import GrupoCapaServicio
from app.infraestructura.oauth_2.autorizador import obtener_usuario_registrado
from app.infraestructura.oauth_2.modelos.usuario_registrado_modelo import UsuarioRegistradoModelo

grupo_capa_controller = APIRouter()


@grupo_capa_controller.get("/", response_model=list[ObtenerTodosGrupoCapaResponse])
async def obtener_todos(
        grupo_capa_servicio: GrupoCapaServicio = Depends(GrupoCapaServicio),
        _: UsuarioRegistradoModelo = Depends(obtener_usuario_registrado)) -> list[ObtenerTodosGrupoCapaResponse]:
    return await grupo_capa_servicio.obtener_todos()


@grupo_capa_controller.get("/estructuras/", response_model=list[ObtenerEstructuraGrupoCapaResponse])
async def obtener_estructura(
        grupo_capa_servicio: GrupoCapaServicio = Depends(GrupoCapaServicio),
        _: UsuarioRegistradoModelo = Depends(obtener_usuario_registrado)) -> list[ObtenerEstructuraGrupoCapaResponse]:
    return await grupo_capa_servicio.obtener_estructura()


@grupo_capa_controller.get("/{grupo_capa_id}/", response_model=ObtenerPorIdGrupoCapaResponse)
async def obtener_por_id(
        grupo_capa_id: str,
        grupo_capa_servicio: GrupoCapaServicio = Depends(GrupoCapaServicio),
        _: UsuarioRegistradoModelo = Depends(obtener_usuario_registrado)) -> ObtenerPorIdGrupoCapaResponse:
    return await grupo_capa_servicio.obtener_por_id(grupo_capa_id)


@grupo_capa_controller.post("/", response_model=str)
async def crear(
        request: CrearGrupoCapaRequest,
        grupo_capa_servicio: GrupoCapaServicio = Depends(GrupoCapaServicio),
        usuario_registrado: UsuarioRegistradoModelo = Depends(obtener_usuario_registrado)) -> str:
    return await grupo_capa_servicio.crear(request, usuario_registrado.id)


@grupo_capa_controller.put("/{grupo_capa_id}/", response_model=str)
async def actualizar(
        grupo_capa_id: str,
        request: ActualizarGrupoCapaRequest,
        grupo_capa_servicio: GrupoCapaServicio = Depends(GrupoCapaServicio),
        usuario_registrado: UsuarioRegistradoModelo = Depends(obtener_usuario_registrado)) -> str:
    return await grupo_capa_servicio.actualizar(grupo_capa_id, request, usuario_registrado.id)


@grupo_capa_controller.delete("/{grupo_capa_id}/", response_model=str)
async def eliminar(
        grupo_capa_id: str,
        grupo_capa_servicio: GrupoCapaServicio = Depends(GrupoCapaServicio),
        usuario_registrado: UsuarioRegistradoModelo = Depends(obtener_usuario_registrado)) -> str:
    return await grupo_capa_servicio.eliminar(grupo_capa_id, usuario_registrado.id)
