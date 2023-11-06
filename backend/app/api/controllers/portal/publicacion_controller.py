from fastapi import APIRouter, Depends

from app.aplicacion.dtos.portal.obtener_todos_publicacion_response import ObtenerTodosPublicacionResponse
from app.aplicacion.servicios.portal.publicacion_servicio import PublicacionServicio

publicacion_controller = APIRouter()


@publicacion_controller.get("/", response_model=list[ObtenerTodosPublicacionResponse])
async def obtener_todos(
        tipo_publicacion: str,
        publicacion_servicio: PublicacionServicio = Depends(PublicacionServicio)) \
        -> list[ObtenerTodosPublicacionResponse]:
    return await publicacion_servicio.obtener_todos(tipo_publicacion)
