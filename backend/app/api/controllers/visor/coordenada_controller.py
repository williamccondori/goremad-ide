from fastapi import APIRouter, Depends

from app.aplicacion.dtos.visor.obtener_coordenada_request import ObtenerCoordenadaRequest
from app.aplicacion.dtos.visor.obtener_coordenada_response import ObtenerCoordenadaResponse
from app.aplicacion.servicios.visor.coordenada_servicio import CoordenadaServicio

coordenada_controller = APIRouter()


@coordenada_controller.get("/", response_model=ObtenerCoordenadaResponse)
async def obtener_coordenadas(
        request: ObtenerCoordenadaRequest = Depends(),
        coordenada_servicio: CoordenadaServicio = Depends(CoordenadaServicio)) -> ObtenerCoordenadaResponse:
    """
    Obtiene las coordenadas de un punto en un sistema de coordenadas dado.
    Args:
        request (ObtenerCoordenadaRequest): Objeto con los parámetros de la petición.
        coordenada_servicio (CoordenadaServicio): Servicio de coordenadas.
    Returns:
        ObtenerCoordenadaResponse: Informacion de las coordenadas.
    """
    return await coordenada_servicio.obtener_coordenadas(request)
