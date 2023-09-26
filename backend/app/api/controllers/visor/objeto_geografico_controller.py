from fastapi import APIRouter, Depends

from app.aplicacion.dtos.visor.obtener_geometria_objeto_geografico_response import \
    ObtenerGeometriaObjetoGeograficoResponse
from app.aplicacion.servicios.visor.objeto_geografico_servicio import ObjetoGeograficoServicio

objeto_geografico_controller = APIRouter()


@objeto_geografico_controller.get("/{objeto_geografico_id}/geometrias/",
                                  response_model=ObtenerGeometriaObjetoGeograficoResponse)
async def obtener_geometria(
        objeto_geografico_id: str,
        objeto_geografico_servicio: ObjetoGeograficoServicio = Depends()) -> ObtenerGeometriaObjetoGeograficoResponse:
    return await objeto_geografico_servicio.obtener_geometria(objeto_geografico_id)


@objeto_geografico_controller.get("/{objeto_geografico_id}/propiedades/", response_model=dict)
async def obtener_geometria(
        objeto_geografico_id: str,
        registro_id: str,
        objeto_geografico_servicio: ObjetoGeograficoServicio = Depends()) -> dict:
    return await objeto_geografico_servicio.obtener_propiedades(objeto_geografico_id, registro_id)
