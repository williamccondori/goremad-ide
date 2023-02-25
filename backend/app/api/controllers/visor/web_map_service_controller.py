from fastapi import APIRouter, Depends

from app.aplicacion.dtos.visor.obtener_features_web_map_service_request import ObtenerFeaturesWebMapServiceRequest
from app.aplicacion.dtos.visor.obtener_features_web_map_service_response import ObtenerFeaturesWebMapServiceResponse
from app.aplicacion.dtos.visor.obtener_informacion_web_map_service_request import ObtenerInformacionWebMapServiceRequest
from app.aplicacion.dtos.visor.obtener_informacion_web_map_service_response import \
    ObtenerInformacionWebMapServiceResponse
from app.aplicacion.servicios.visor.web_map_service_servicio import WebMapServiceServicio

web_map_service_controller = APIRouter()


@web_map_service_controller.get("/", response_model=ObtenerInformacionWebMapServiceResponse)
async def obtener_informacion(
        request: ObtenerInformacionWebMapServiceRequest = Depends(),
        web_map_service_servicio: WebMapServiceServicio = Depends(WebMapServiceServicio)) \
        -> ObtenerInformacionWebMapServiceResponse:
    """
    Obtiene la informacion de un servicio web de mapas.
    Args:
        request (ObtenerInformacionWebMapServiceRequest): Parametros de la consulta.
        web_map_service_servicio (WebMapServiceServicio): Servicio para la consulta de los servicios web de mapas.
    Returns:
        ObtenerInformacionWebMapServiceResponse: Informacion del servicio web de mapas.
    """

    return await web_map_service_servicio.obtener_informacion(request)


@web_map_service_controller.get("/features/", response_model=list[ObtenerFeaturesWebMapServiceResponse])
async def obtener_features(
        request: ObtenerFeaturesWebMapServiceRequest = Depends(),
        web_map_service_servicio: WebMapServiceServicio = Depends(WebMapServiceServicio)) \
        -> list[ObtenerFeaturesWebMapServiceResponse]:
    """
    Obtiene la informacion de los features de un servicio web de mapas.
    Args:
        request (ObtenerFeaturesWebMapServiceRequest): Parametros de la consulta.
        web_map_service_servicio (WebMapServiceServicio): Servicio para la consulta de los servicios web de mapas.
    Returns:
        list[ObtenerFeaturesWebMapServiceResponse]: Informacion de los features del servicio web de mapas.
    """

    return await web_map_service_servicio.obtener_features(request)
