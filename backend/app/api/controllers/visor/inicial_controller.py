from fastapi import APIRouter, Depends

from app.aplicacion.dtos.visor.obtener_inicial_response import ObtenerInicialResponse
from app.aplicacion.servicios.visor.inicial_servicio import InicialServicio

inicial_controller = APIRouter()


@inicial_controller.get("/", response_model=ObtenerInicialResponse)
async def obtener_inicial(
        inicial_servicio: InicialServicio = Depends(InicialServicio)) -> ObtenerInicialResponse:
    """
    Obtiene la información inicial para el visor de mapas.
    Args:
        inicial_servicio: Servicio para obtener la información inicial para el visor de mapas.
    Returns:
        Información inicial para el visor de mapas.
    """
    return await inicial_servicio.obtener_inicial()
