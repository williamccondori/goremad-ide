from app.aplicacion.parseadores.base_modelo import BaseModelo


class FeatureWebMapServiceResponse(BaseModelo):
    """
    Modelo de respuesta para obtener features de un servicio web map service.
    Propiedades clave y valor que representan las propiedades de un feature.
    Attributes:
        clave (str): Clave de la propiedad.
        valor (str): Valor de la propiedad.
    """

    clave: str
    valor: str


class ObtenerFeaturesWebMapServiceResponse(BaseModelo):
    """
    Modelo de respuesta para obtener features de un servicio web map service.
    Attributes:
        informacion (list[FeatureWebMapServiceResponse]): Lista de propiedades de los features.
    """

    informacion: list[FeatureWebMapServiceResponse] = []
