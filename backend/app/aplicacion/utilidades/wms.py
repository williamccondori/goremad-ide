import numpy as np
import pandas as pd
from pandas import DataFrame
from pydantic import BaseModel, HttpUrl

from app.aplicacion.utilidades.constantes import CADENA_VACIA, SISTEMA_COORDENADAS, FORMATO_SALIDA_CARACTERISTICAS
from app.aplicacion.utilidades.ogc_reader import WebMapService111, web_map_service
from app.dominio.excepciones.aplicacion_exception import AplicacionException


class CapaModelo(BaseModel):
    """
    Modelo de datos para una capa de un servicio WMS.
    """
    nombre: str
    titulo: str
    cuadro_delimitador: list[float]


class InformacionWebMapServiceModelo(BaseModel):
    """
    Modelo de datos para la informacion de un servicio WMS.
    """
    url: str
    nombre: str
    titulo: str
    descripcion: str
    version: str
    palabras_clave: list[str] = []
    operaciones: list[str] = []
    capas: list[CapaModelo]


class InformacionFeatureModelo(BaseModel):
    """
    Modelo de datos para la informacion de un feature de un servicio WMS.
    """
    clave: str
    valor: str


class ResultadoInformacionFeatureModelo(BaseModel):
    """
    Modelo de datos para el resultado de la informacion de un feature de un servicio WMS.
    """
    informacion: list[InformacionFeatureModelo]


def __obtener_url_base(url: HttpUrl) -> HttpUrl:
    """
    Obtiene la URL base de un servicio externo.
    Incluye validaciones de protocolo y omision de parametros de consulta.
    Args:
        url: URL del servicio.
    Returns:
        URL base del servicio.
    """
    url_base: str = url.strip()
    url_base: str = url_base.split('?')[0]
    return HttpUrl(url_base, scheme=url.scheme)


def __obtener_datos_desde_dataframe(data_frames: list[DataFrame], es_geoserver: bool) -> \
        list[ResultadoInformacionFeatureModelo]:
    """
    Obtiene los datos de una consulta a partir de una lista de dataframes.
    Args:
        data_frames: Lista de dataframes.
        es_geoserver: Indica si el servicio es de Geoserver.
    Returns:
        Lista de resultados de la consulta.
    """
    resultados: list[ResultadoInformacionFeatureModelo] = []
    for data_frame in data_frames:
        if not es_geoserver:
            # En algunos casos la estructura de la tabla es diferente, especialmente en los servicios de ArcGIS,
            # en esos casos, se transpone la tabla para obtener los datos de la consulta.
            # Si tiene un mas de un registro y dos columnas, se transpone la tabla.
            if data_frame.shape[0] > 1 and data_frame.shape[1] == 2:
                data_frame = data_frame.set_index(data_frame.columns[0])  # Se realiza la correccion de indices.
                data_frame = data_frame.transpose()
        # Se transforman los nombres de las columnas a mayusculas.
        # Transformar las columnas a cadena de texto.
        data_frame.columns = data_frame.columns.astype(str)
        data_frame.columns = data_frame.columns.str.upper()

        # Se eliminan las columnas que no se deben mostrar.
        columnas_a_ignorar = ["ID", "FID", "GUID", "GID", "OBJECTID", "SHAPE"]
        data_frame = data_frame.drop(columns=columnas_a_ignorar, errors='ignore')
        # Se eliminan las columnas que no se deben mostrar.
        columnas_areas = [
            "SHAPE.AREA", "SHAPE.STAREA", "ST_AREASHAPE", "SHAPE.STAREASHAPE"
        ]
        columnas_perimetros = [
            "SHAPE.LEN", "SHAPE.STLENGTH", "ST_LENGTHSHAPE", "SHAPE.STLENGTHSHAPE"
        ]
        data_frame = data_frame.drop(columns=columnas_areas, errors='ignore')
        data_frame = data_frame.drop(columns=columnas_perimetros, errors='ignore')
        # Si esta vacio, se devuelve un resultado vacio.
        if data_frame.empty:
            return []
        # Se reemplazan los valores nulos por cadenas vacias.
        data_frame = data_frame.replace({np.nan: None})
        data_frame = data_frame.replace({pd.NaT: None})
        data_frame = data_frame.replace({"Null": None})
        data_frame = data_frame.fillna(CADENA_VACIA)
        # Trasformar los valores de las columnas a cadena de texto.
        data_frame = data_frame.astype(str)
        # Se convierte el dataframe a un diccionario.
        diccionario: dict = data_frame.to_dict(orient='records')[0]
        resultados.append(ResultadoInformacionFeatureModelo(
            informacion=[InformacionFeatureModelo(
                clave=clave,  # Representa el nombre de la columna.
                valor=valor,  # Representa el valor de la columna.
            ) for clave, valor in diccionario.items()]
        ))

    return resultados


def obtener_informacion_wms(url: HttpUrl) -> InformacionWebMapServiceModelo:
    """
    Obtiene la información de un servicio WMS.
    Args:
        url: URL del servicio.
    Returns:
        Información del servicio WMS.
    """
    try:
        # Se obtiene la URL base del servicio.
        url_base: HttpUrl = __obtener_url_base(url)
        # Se realiza la consulta al servicio (Se emplea wrapper para omitir la compronacion de certificados).
        wms: WebMapService111 = web_map_service(url_base)
        if not wms:
            raise Exception()
    except Exception as excepcion:
        raise AplicacionException("No se ha podido conectar con el servicio externo") from excepcion
    # Se obtiene la informacion relacionada a las capas.
    capas: list[CapaModelo] = []
    capas_encontradas = wms.contents
    for capa in capas_encontradas:
        informacion_capa = capas_encontradas[capa]

        # Si no es queryable, no se agrega a la lista de capas.
        if not informacion_capa.queryable == 1:
            continue
        # Si tiene hijos, no se agrega a la lista de capas.
        if len(list(informacion_capa.layers)) > 0:
            continue

        cuadro_delimitador: list[float] = []
        if informacion_capa.boundingBox:
            cuadro_delimitador = [
                float(informacion_capa.boundingBox[0]),
                float(informacion_capa.boundingBox[1]),
                float(informacion_capa.boundingBox[2]),
                float(informacion_capa.boundingBox[3])
            ]
        capas.append(
            CapaModelo(
                nombre=capa,
                titulo=informacion_capa.title or CADENA_VACIA,
                cuadro_delimitador=cuadro_delimitador
            )
        )
    # Se obtiene la informacion relacionada a las operaciones.
    operaciones: list[str] = [operacion.name for operacion in wms.operations]
    return InformacionWebMapServiceModelo(
        url=url_base,
        nombre=wms.identification.type or CADENA_VACIA,
        titulo=wms.identification.title or CADENA_VACIA,
        version=wms.identification.version or CADENA_VACIA,
        descripcion=wms.identification.abstract or CADENA_VACIA,
        palabras_clave=wms.identification.keywords or [],
        operaciones=operaciones,
        capas=capas
    )


def obtener_features(url: HttpUrl, x: int, y: int, width: int, height: int, bounding_box: str, layers: str) \
        -> list[ResultadoInformacionFeatureModelo]:
    """
    Obtiene la información de un servicio WMS (GetFeatureInfo).
    Args:
        url: URL del servicio.
        x: Coordenada X.
        y: Coordenada Y.
        width: Ancho de la imagen.
        height: Alto de la imagen.
        bounding_box: Bounding box.
        layers: Capas.
    Returns:
        Información del servicio.
    """
    try:
        # Se obtiene la URL base del servicio.
        url_base: HttpUrl = __obtener_url_base(url)
        # Se realiza la consulta al servicio (Se emplea wrapper para omitir la compronacion de certificados).
        wms: WebMapService111 = web_map_service(url_base)
        if not wms:
            raise Exception()
    except Exception as excepcion:
        print(excepcion)
        return []
    # Se realiza el tratamiento de los parametros de entrada.
    bounding_box: list[str] = bounding_box.split(',')
    bbox = tuple(float(i) for i in bounding_box)
    capas: list[str] = str(layers).split(',')
    # Se realiza la consulta de las caracteristicas desde la instancia del servicio.
    # Mas informacion:
    # https://webhelp.esri.com/arcims/9.3/General/mergedProjects/wms_connect/wms_connector/get_featureinfo.htm
    # https://docs.geoserver.org/2.22.x/en/user/services/wms/reference.html#getfeatureinfo
    feature_info = wms.getfeatureinfo(
        # Sistema de coordenadas.
        srs=SISTEMA_COORDENADAS,
        # Punto de consulta.
        xy=(x, y),
        # Tamanio original del mapa.
        size=(width, height),
        # Formato de salida (Se emplea HTML por restricciones de compatibilidad).
        info_format=FORMATO_SALIDA_CARACTERISTICAS,
        # Cuadro delimitador del mapa.
        bbox=bbox,
        # Lista de capas intervinientes en la consulta.
        layers=capas,
        # Lista de capas consideradas en la consulta.
        query_layers=capas
    )
    # Se obtiene el resulta y se decodifican los bytes a texto.
    resultado: bytes = feature_info.read()
    resultado_texto = resultado.decode('utf-8')
    # Se obtiene la tabla de caracteristicas desde el resultado de la consulta.
    try:
        # Se emplea pandas para obtener la tabla de caracteristicas.
        # En caso que no se obtengan resultados, este emitira una excepcion de tipo ValueError.
        tablas: list[DataFrame] = pd.read_html(resultado_texto)
    except ValueError:
        # Si se obtiene una excepcion de tipo ValueError, se retorna una lista vacia al no haber resultados.
        return []
    # Se verifica si el servicio es de tipo GeoServer a traves de la URL base.
    es_geoserver: bool = url_base.lower().find('geoserver') != -1
    # Se obtiene la informacion de las caracteristicas.
    return __obtener_datos_desde_dataframe(tablas, es_geoserver)


def obtener_url_leyenda(url: str, nombre_capa: str) -> str:
    """
    Obtiene la URL de la leyenda de una capa.
    Args:
        url: URL del servicio.
        nombre_capa: Nombre de la capa.
    Returns:
        URL de la leyenda de la capa.
    """
    return f"{url}/wms?service=WMS&version=1.1.1&layer={nombre_capa}&request=GetLegendGraphic&format=image/png"
