from fastapi import APIRouter, Depends

from app.aplicacion.dtos.visor.obtener_ubicacion_request import ObtenerUbicacionRequest
from app.aplicacion.dtos.visor.obtener_ubicacion_response import ObtenerUbicacionResponse
from app.aplicacion.servicios.visor.ubicacion_servicio import UbicacionServicio

ubicacion_controller = APIRouter()


@ubicacion_controller.get("/", response_model=list[ObtenerUbicacionResponse])
async def obtener_todos(
        request: ObtenerUbicacionRequest = Depends(),
        ubicacion_servicio: UbicacionServicio = Depends(UbicacionServicio)) -> list[ObtenerUbicacionResponse]:
    """
    Obtiene todas las ubicaciones que coincidan con el nombre de la ubicacion.
    Args:
        request: Datos de la peticion.
        ubicacion_servicio: Servicio para la consulta de ubicaciones.
    Returns:
        Lista de ubicaciones que coincidan con el nombre de la ubicacion.
    """
    return await ubicacion_servicio.obtener_todos(request)
