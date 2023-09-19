from fastapi import APIRouter, Depends

from app.aplicacion.dtos.administrador.actualizar_objeto_geografico_request import ActualizarObjetoGeograficoRequest
from app.aplicacion.dtos.administrador.crear_objeto_geografico_request import CrearObjetoGeograficoRequest
from app.aplicacion.dtos.administrador.obtener_por_id_objeto_geografico_response import \
    ObtenerPorIdObjetoGeograficoResponse
from app.aplicacion.dtos.administrador.obtener_todos_objeto_geografico_response import \
    ObtenerTodosObjetoGeograficoResponse
from app.aplicacion.servicios.administrador.objeto_geografico_servicio import ObjetoGeograficoServicio
from app.infraestructura.oauth_2.autorizador import obtener_usuario_registrado
from app.infraestructura.oauth_2.modelos.usuario_registrado_modelo import UsuarioRegistradoModelo

objeto_geografico_controller = APIRouter()


@objeto_geografico_controller.get("/", response_model=list[ObtenerTodosObjetoGeograficoResponse])
async def obtener_todos(
        objeto_geografico_servicio: ObjetoGeograficoServicio = Depends(ObjetoGeograficoServicio),
        _: UsuarioRegistradoModelo = Depends(obtener_usuario_registrado)) -> list[ObtenerTodosObjetoGeograficoResponse]:
    return await objeto_geografico_servicio.obtener_todos()


@objeto_geografico_controller.get("/{objeto_geografico_id}/", response_model=ObtenerPorIdObjetoGeograficoResponse)
async def obtener_por_id(
        objeto_geografico_id: str,
        objeto_geografico_servicio: ObjetoGeograficoServicio = Depends(ObjetoGeograficoServicio),
        _: UsuarioRegistradoModelo = Depends(obtener_usuario_registrado)) -> ObtenerPorIdObjetoGeograficoResponse:
    return await objeto_geografico_servicio.obtener_por_id(objeto_geografico_id)


@objeto_geografico_controller.post("/", response_model=str)
async def crear(
        request: CrearObjetoGeograficoRequest,
        objeto_geografico_servicio: ObjetoGeograficoServicio = Depends(ObjetoGeograficoServicio),
        usuario_registrado: UsuarioRegistradoModelo = Depends(obtener_usuario_registrado)) -> str:
    return await objeto_geografico_servicio.crear(request, usuario_registrado.id)


@objeto_geografico_controller.put("/{objeto_geografico_id}/", response_model=str)
async def actualizar(
        objeto_geografico_id: str,
        request: ActualizarObjetoGeograficoRequest,
        objeto_geografico_servicio: ObjetoGeograficoServicio = Depends(ObjetoGeograficoServicio),
        usuario_registrado: UsuarioRegistradoModelo = Depends(obtener_usuario_registrado)) -> str:
    return await objeto_geografico_servicio.actualizar(objeto_geografico_id, request, usuario_registrado.id)


@objeto_geografico_controller.delete("/{objeto_geografico_id}/", response_model=str)
async def eliminar(
        objeto_geografico_id: str,
        objeto_geografico_servicio: ObjetoGeograficoServicio = Depends(ObjetoGeograficoServicio),
        usuario_registrado: UsuarioRegistradoModelo = Depends(obtener_usuario_registrado)) -> str:
    return await objeto_geografico_servicio.eliminar(objeto_geografico_id, usuario_registrado.id)
