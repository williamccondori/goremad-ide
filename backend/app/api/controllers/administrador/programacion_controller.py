from typing import Optional

from fastapi import APIRouter, Depends

from app.aplicacion.dtos.administrador.obtener_actual_programacion_reponse import ObtenerActualProgramacionResponse
from app.aplicacion.dtos.administrador.obtener_actual_programacion_request import ObtenerActualProgramacionRequest
from app.aplicacion.dtos.administrador.obtener_todo_programacion_response import ObtenerTodoProgramacionResponse
from app.aplicacion.servicios.administrador.programacion_servicio import ProgramacionServicio
from app.infraestructura.oauth_2.autorizador import obtener_usuario_registrado
from app.infraestructura.oauth_2.modelos.usuario_registrado_modelo import UsuarioRegistradoModelo

programacion_controller = APIRouter()


@programacion_controller.get("/", response_model=list[ObtenerTodoProgramacionResponse])
async def obtener_todos(
        programacion_servicio: ProgramacionServicio = Depends(ProgramacionServicio),
        _: UsuarioRegistradoModelo = Depends(obtener_usuario_registrado)) -> list[ObtenerTodoProgramacionResponse]:
    return await programacion_servicio.obtener_todos()


@programacion_controller.get("/actuales/", response_model=Optional[ObtenerActualProgramacionResponse])
async def obtener_actual(
        request: ObtenerActualProgramacionRequest = Depends(),
        programacion_servicio: ProgramacionServicio = Depends(ProgramacionServicio),
        _: UsuarioRegistradoModelo = Depends(obtener_usuario_registrado)
) -> Optional[ObtenerActualProgramacionResponse]:
    return await programacion_servicio.obtener_actual(request)
