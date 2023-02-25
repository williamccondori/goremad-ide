from app.aplicacion.dtos.visor.obtener_features_web_map_service_request import ObtenerFeaturesWebMapServiceRequest
from app.aplicacion.dtos.visor.obtener_features_web_map_service_response import ObtenerFeaturesWebMapServiceResponse, \
    FeatureWebMapServiceResponse
from app.aplicacion.dtos.visor.obtener_informacion_web_map_service_request import ObtenerInformacionWebMapServiceRequest
from app.aplicacion.dtos.visor.obtener_informacion_web_map_service_response import CapaResponse, \
    ObtenerInformacionWebMapServiceResponse
from app.aplicacion.utilidades.wms import ResultadoInformacionFeatureModelo, \
    InformacionWebMapServiceModelo, obtener_informacion_wms, obtener_features


class WebMapServiceServicio:
    """
    Clase que contiene los servicios de consulta de servicios web de mapas.
    """

    @staticmethod
    def ____mapear_informacion_web_map_service(resultado: InformacionWebMapServiceModelo) \
            -> ObtenerInformacionWebMapServiceResponse:
        """
        Mapea la informacion del resultado de la consulta de informacion al modelo de respuesta.
        Args:
            resultado (InformacionWebMapServiceModelo): Resultado de la consulta de informacion.
        Returns:
            ObtenerInformacionWebMapServiceResponse: Modelo de respuesta.
        """

        return ObtenerInformacionWebMapServiceResponse(
            url=resultado.url,
            nombre=resultado.nombre,
            titulo=resultado.titulo,
            version=resultado.version,
            descripcion=resultado.descripcion,
            palabras_clave=[],
            operaciones=resultado.operaciones,
            capas=[CapaResponse(
                nombre=capa.nombre,
                titulo=capa.titulo,
            ) for capa in resultado.capas]
        )

    @staticmethod
    def __mapear_features_web_map_service(resultados: list[ResultadoInformacionFeatureModelo]) \
            -> list[ObtenerFeaturesWebMapServiceResponse]:
        """
        Mapea la informacion del resultado de la consulta de features al modelo de respuesta.
        Args:
            resultados (list[ResultadoInformacionFeatureModelo]): Resultado de la consulta de features.
        Returns:
            list[ObtenerFeaturesWebMapServiceResponse]: Modelo de respuesta.
        """

        return [ObtenerFeaturesWebMapServiceResponse(
            informacion=[FeatureWebMapServiceResponse(
                clave=feature.clave,
                valor=feature.valor,
            ) for feature in resultado.informacion]
        ) for resultado in resultados]

    async def obtener_informacion(self, request: ObtenerInformacionWebMapServiceRequest) \
            -> ObtenerInformacionWebMapServiceResponse:
        """
        Obtiene la informacion de un servicio web de mapas.
        Args:
            request (ObtenerInformacionWebMapServiceRequest): Parametros de la consulta.
        Returns:
            ObtenerInformacionWebMapServiceResponse: Informacion del servicio web de mapas.
        """

        resultado: InformacionWebMapServiceModelo = obtener_informacion_wms(request.url)
        return self.____mapear_informacion_web_map_service(resultado)

    async def obtener_features(self, request: ObtenerFeaturesWebMapServiceRequest) \
            -> list[ObtenerFeaturesWebMapServiceResponse]:
        """
        Obtiene la informacion de los features de un servicio web de mapas.
        Args:
            request (ObtenerFeaturesWebMapServiceRequest): Parametros de la consulta.
        Returns:
            list[ObtenerFeaturesWebMapServiceResponse]: Informacion de los features del servicio web de mapas.
        """

        resultados: list[ResultadoInformacionFeatureModelo] = obtener_features(
            request.url,
            request.x,
            request.y,
            request.width,
            request.height,
            request.bounding_box,
            request.layers
        )
        return self.__mapear_features_web_map_service(resultados)
