from fastapi import APIRouter, Depends

from app.aplicacion.dtos.visor.obtener_informacion_objeto_geografico_response import \
    ObtenerInformacionObjetoGeograficoResponse
from app.aplicacion.servicios.visor.objeto_geografico_servicio import ObjetoGeograficoServicio

objeto_geografico_controller = APIRouter()


@objeto_geografico_controller.get("/{objeto_geografico_id}/informacion/",
                                  response_model=ObtenerInformacionObjetoGeograficoResponse)
async def obtener_geometria(
        objeto_geografico_id: str,
        incluir_propiedades: bool = False,
        objeto_geografico_servicio: ObjetoGeograficoServicio = Depends()) -> ObtenerInformacionObjetoGeograficoResponse:
    return await objeto_geografico_servicio.obtener_informacion_objeto_geografico(objeto_geografico_id,
                                                                                  incluir_propiedades)
