from app.aplicacion.dtos.visor.obtener_features_web_map_service_request import (
    ObtenerFeaturesWebMapServiceRequest,
)
from app.aplicacion.dtos.visor.obtener_features_web_map_service_response import (
    ObtenerFeaturesWebMapServiceResponse,
    FeatureWebMapServiceResponse,
)
from app.aplicacion.dtos.visor.obtener_informacion_web_map_service_request import (
    ObtenerInformacionWebMapServiceRequest,
)
from app.aplicacion.dtos.visor.obtener_informacion_web_map_service_response import (
    CapaResponse,
    ObtenerInformacionWebMapServiceResponse,
)
from app.aplicacion.utilidades.wms import (
    ResultadoInformacionFeatureModelo,
    InformacionWebMapServiceModelo,
    obtener_informacion_wms,
    obtener_feature,
)


class WebMapServiceServicio:
    @staticmethod
    def ____mapear_informacion_web_map_service(
        resultado: InformacionWebMapServiceModelo,
    ) -> ObtenerInformacionWebMapServiceResponse:
        return ObtenerInformacionWebMapServiceResponse(
            url=resultado.url,
            nombre=resultado.nombre,
            titulo=resultado.titulo,
            version=resultado.version,
            descripcion=resultado.descripcion,
            palabras_clave=[],
            operaciones=resultado.operaciones,
            capas=[
                CapaResponse(
                    nombre=capa.nombre,
                    titulo=capa.titulo,
                )
                for capa in resultado.capas
            ],
        )

    @staticmethod
    def __mapear_features_web_map_service(
        resultados: list[ResultadoInformacionFeatureModelo],
    ) -> list[ObtenerFeaturesWebMapServiceResponse]:
        return [
            ObtenerFeaturesWebMapServiceResponse(
                informacion=[
                    FeatureWebMapServiceResponse(
                        clave=feature.clave,
                        valor=feature.valor,
                    )
                    for feature in resultado.informacion
                ]
            )
            for resultado in resultados
        ]

    async def obtener_informacion(
        self, request: ObtenerInformacionWebMapServiceRequest
    ) -> ObtenerInformacionWebMapServiceResponse:
        resultado: InformacionWebMapServiceModelo = obtener_informacion_wms(request.url)
        return self.____mapear_informacion_web_map_service(resultado)

    async def obtener_features(
        self, request: ObtenerFeaturesWebMapServiceRequest
    ) -> list[ObtenerFeaturesWebMapServiceResponse]:
        resultados: list[ResultadoInformacionFeatureModelo] = obtener_feature(
            request.url,
            request.x,
            request.y,
            request.width,
            request.height,
            request.bounding_box,
            request.layers,
        )
        return self.__mapear_features_web_map_service(resultados)
