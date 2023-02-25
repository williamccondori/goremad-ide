import geopandas.io.sql
from bson import ObjectId
from fastapi import APIRouter
from geo.Geoserver import Geoserver  # noqa
from geopandas import GeoDataFrame
from pymongo.results import InsertOneResult
from sqlalchemy import create_engine
from starlette import status

from database import Capas, Publicaciones
from exceptions import ApplicationException, APIException
from app.legacy.helpers import postgres
from parser import CustomBaseModel, CustomBaseSchema
from settings import settings

PROTOCOLO_WMS = "WMS"
PROTOCOLO_WFS = "WFS"

ESPACIO_TRABAJO_WMS = "SERVICIOS_WMS"

COLUMNAS_NUMERICAS = ['integer', 'bigint', 'smallint']


class CapaEntidad(CustomBaseModel):
    publicacion_id: str
    grupo_capa_id: str | None
    nombre: str
    titulo: str
    nombre_espacio_trabajo: str
    habilitar_wms: bool = True
    habilitar_wfs: bool = True
    se_puede_descargar: bool = False
    se_puede_consultar: bool = False
    cargar_al_inicio: bool = False
    esta_habilitado: bool = True


class PublicacionEntidad(CustomBaseModel):
    identificador_base_datos_origen: str
    nombre_esquema_origen: str
    nombre_tabla_origen: str
    nombre_tabla_destino: str
    nombre_espacio_trabajo: str
    nombre_capa: str
    titulo_capa: str
    habilitar_wms: bool = True
    habilitar_wfs: bool = True


class ObtenerTodoPublicacionResponse(CustomBaseSchema):
    id: str
    identificador_base_datos_origen: str
    nombre_esquema_origen: str
    nombre_tabla_origen: str
    nombre_tabla_destino: str
    nombre_espacio_trabajo: str
    nombre_capa: str
    titulo_capa: str
    habilitar_wms: bool
    habilitar_wfs: bool
    usuario_creacion: str
    fecha_creacion: str


class CrearPublicacionRequest(CustomBaseSchema):
    # Base de datos
    identificador_base_datos_origen: str
    nombre_esquema_origen: str
    nombre_tabla_origen: str
    nombre_tabla_destino: str
    # Geoserver
    nombre_espacio_trabajo: str | None
    nombre_capa: str
    titulo_capa: str
    # Sistema
    grupo_capa_id: str | None
    habilitar_wms: bool = True
    habilitar_wfs: bool = True
    se_puede_descargar: bool = False
    se_puede_consultar: bool = False
    esta_habilitado: bool = True


def normalizar_informacion(
        dataframe: GeoDataFrame,
        definicion_columnas: list[dict],
        nombres_columnas_excluidas: list[str] = None
) -> GeoDataFrame:
    if nombres_columnas_excluidas is None:
        nombres_columnas_excluidas = []

    # Se realiza el tratamiento de columnas numéricas
    nombres_columnas_numericas = [definicion_columna['column_name'] for definicion_columna in definicion_columnas if
                                  definicion_columna['column_type'] in COLUMNAS_NUMERICAS]
    for nombre_columna_numerica in nombres_columnas_numericas:
        if nombre_columna_numerica not in nombres_columnas_excluidas:
            dataframe[nombre_columna_numerica] = dataframe[nombre_columna_numerica].astype('Int64')

    # Se realiza la normalización de los datos
    dataframe.set_crs(epsg=32719, inplace=True)
    dataframe.sort_values(by=['id'], inplace=True)
    dataframe.drop(columns=['id'], inplace=True)
    return dataframe


def publicar_a_geoserver(
        nombre_espacio_trabajo: str,
        nombre_almacen_datos: str,
        nombre_tabla: str,
        nombre_capa: str,
        titulo_capa: str
) -> None:
    geoserver = Geoserver(settings.GEOSERVER_URL, username=settings.GEOSERVER_USER,
                          password=settings.GEOSERVER_PASSWORD)

    capa_geografica = geoserver.get_layer(
        layer_name=nombre_capa,
        workspace=nombre_espacio_trabajo
    )
    if capa_geografica:
        geoserver.delete_layer(
            layer_name=nombre_capa,
            workspace=nombre_espacio_trabajo
        )

    resultado = geoserver.publish_featurestore(
        store_name=nombre_almacen_datos,
        workspace=nombre_espacio_trabajo,
        pg_table=nombre_tabla
    )
    if type(resultado) is str:
        raise ApplicationException("Ha ocurrido un error al publicar la capa geográfica")

    resultado = geoserver.edit_featuretype(
        store_name=nombre_almacen_datos,
        workspace=nombre_espacio_trabajo,
        pg_table=nombre_tabla,
        name=nombre_capa,
        title=titulo_capa
    )
    if type(resultado) is str:
        raise ApplicationException("Ha ocurrido un error al configurar la capa geográfica")


publicacion_controller = APIRouter()


@publicacion_controller.get("/", response_model=list[ObtenerTodoPublicacionResponse])
async def obtener_todo() -> list[ObtenerTodoPublicacionResponse]:
    try:
        publicaciones = Publicaciones.find({
            "is_active": True
        })

        get_all_publications_response = [
            ObtenerTodoPublicacionResponse(
                id=str(publicacion["_id"]),
                identificador_base_datos_origen=publicacion["identificador_base_datos_origen"],
                nombre_esquema_origen=publicacion["nombre_esquema_origen"],
                nombre_tabla_origen=publicacion["nombre_tabla_origen"],
                nombre_tabla_destino=publicacion["nombre_tabla_destino"],
                nombre_espacio_trabajo=publicacion["nombre_espacio_trabajo"],
                nombre_capa=publicacion["nombre_capa"],
                titulo_capa=publicacion["titulo_capa"],
                habilitar_wms=publicacion["habilitar_wms"],
                habilitar_wfs=publicacion["habilitar_wfs"],
                usuario_creacion=publicacion["created_by"],
                fecha_creacion=publicacion["created_at"].strftime("%d/%m/%Y %H:%M")
            ) for publicacion in publicaciones
        ]

        return get_all_publications_response
    except Exception as e:
        raise APIException(e)


@publicacion_controller.post("/", response_model=str)
async def crear(request: CrearPublicacionRequest) -> str:
    try:
        # Se debe habilitar al menos un servicio de publicación
        if not request.habilitar_wms and not request.habilitar_wfs:
            raise ApplicationException("Se debe habilitar al menos un servicio de publicación")

        # Validaciones de los esquemas de destino
        if not postgres.existe_esquema(postgres.IDENTIFICADOR_BASE_DATOS_DISTRIBUCION, PROTOCOLO_WMS):
            raise ApplicationException("El esquema de destino para los servicios WMS no existe")
        if not postgres.existe_esquema(postgres.IDENTIFICADOR_BASE_DATOS_DISTRIBUCION, PROTOCOLO_WFS):
            raise ApplicationException("El esquema de destino para los servicios WFS no existe")
        if request.habilitar_wfs:
            if not request.nombre_espacio_trabajo:
                raise ApplicationException(
                    "El nombre del espacio de trabajo es requerido cuando se habilita el servicio WFS")

        definicion_columnas, definicion_llaves_foraneas = postgres.obtener_columnas_desde_tabla(
            identificador_base_datos=request.identificador_base_datos_origen,
            nombre_esquema=request.nombre_esquema_origen,
            nombre_tabla=request.nombre_tabla_origen,
            incluir_llaves_foraneas=True
        )
        if len(definicion_columnas) == 0:
            raise ApplicationException("La tabla solicitada no existe", status.HTTP_404_NOT_FOUND)

        engine_base_datos_entrada = create_engine(postgres.obtener_cadena_conexion_base_datos(
            identificador_base_datos=request.identificador_base_datos_origen
        ))
        engine_base_datos_distribucion = create_engine(postgres.obtener_cadena_conexion_base_datos_distribucion())

        # Realiza la publicación para el protocolo WMS
        if request.habilitar_wms:
            nombres_llaves_foraneas: list[str] = [llave["column_name"] for llave in definicion_llaves_foraneas]

            script_para_crear_tabla: str = postgres.generar_script_creacion_tabla(
                definicion_columnas=definicion_columnas,
                nombre_tabla=request.nombre_tabla_destino,
                nombre_esquema=PROTOCOLO_WMS,
                nombres_llaves_foraneas=nombres_llaves_foraneas
            )
            script_para_crear_vista: str = postgres.generar_script_creacion_vista(
                definicion_columnas=definicion_columnas,
                nombre_tabla=request.nombre_tabla_destino,
                nombre_esquema=PROTOCOLO_WMS
            )

            # Se genera el script de consulta de datos desde la tabla de origen
            nombres_columna: list[str] = [columna["column_name"] for columna in definicion_columnas]
            script_consulta: str = postgres.generar_script_consulta_tabla_con_relaciones(
                identificador_base_datos=request.identificador_base_datos_origen,
                nombre_tabla=request.nombre_tabla_origen,
                nombre_esquema=request.nombre_esquema_origen,
                nombres_columna=nombres_columna,
                definicion_llaves_foraneas=definicion_llaves_foraneas
            )

            # Se consulta y normaliza la información desde la tabla de origen
            dataframe: GeoDataFrame = geopandas.read_postgis(
                sql=script_consulta,
                con=engine_base_datos_entrada,
                geom_col="geom"
            )
            if dataframe.empty:
                raise ApplicationException("La tabla de origen no contiene información")
            dataframe: GeoDataFrame = normalizar_informacion(
                dataframe=dataframe,
                definicion_columnas=definicion_columnas,
                nombres_columnas_excluidas=nombres_llaves_foraneas
            )

            # Se ejecuta el script de creacion de tabla y vista
            with engine_base_datos_distribucion.connect() as conexion_base_datos_distribucion:
                conexion_base_datos_distribucion.execute(script_para_crear_tabla)
                conexion_base_datos_distribucion.execute(script_para_crear_vista)

                # Se realiza la inserción de la información desde la tabla de origen
                dataframe.to_postgis(
                    name=request.nombre_tabla_destino,
                    con=conexion_base_datos_distribucion,
                    schema=PROTOCOLO_WMS,
                    if_exists="append",
                    index=False
                )

            nombre_tabla: str = postgres.PREFIJO_VISTA + request.nombre_tabla_destino

            publicar_a_geoserver(
                nombre_espacio_trabajo=ESPACIO_TRABAJO_WMS,
                nombre_almacen_datos=PROTOCOLO_WMS,
                nombre_tabla=nombre_tabla,
                nombre_capa=request.nombre_capa,
                titulo_capa=request.titulo_capa
            )

        if request.habilitar_wfs:
            script_para_crear_tabla: str = postgres.generar_script_creacion_tabla(
                definicion_columnas=definicion_columnas,
                nombre_tabla=request.nombre_tabla_destino,
                nombre_esquema=PROTOCOLO_WFS
            )

            # Se genera el script de consulta de datos desde la tabla de origen
            nombres_columna: list[str] = [columna["column_name"] for columna in definicion_columnas]
            script_consulta: str = postgres.generar_script_consulta_tabla(
                nombre_tabla=request.nombre_tabla_origen,
                nombre_esquema=request.nombre_esquema_origen,
                nombres_columna=nombres_columna
            )

            # Se consulta y normaliza la información desde la tabla de origen
            dataframe: GeoDataFrame = geopandas.read_postgis(
                sql=script_consulta,
                con=engine_base_datos_entrada,
                geom_col="geom"
            )
            if dataframe.empty:
                raise ApplicationException("La tabla de origen no contiene información")
            dataframe: GeoDataFrame = normalizar_informacion(
                dataframe=dataframe,
                definicion_columnas=definicion_columnas
            )

            # Se ejecuta el script de creacion de tabla y vista
            with engine_base_datos_distribucion.connect() as conexion_base_datos_distribucion:
                conexion_base_datos_distribucion.execute(script_para_crear_tabla)

                # Se realiza la inserción de la información desde la tabla de origen
                dataframe.to_postgis(
                    name=request.nombre_tabla_destino,
                    con=conexion_base_datos_distribucion,
                    schema=PROTOCOLO_WFS,
                    if_exists="append",
                    index=False
                )

            publicar_a_geoserver(
                nombre_espacio_trabajo=request.nombre_espacio_trabajo,
                nombre_almacen_datos=PROTOCOLO_WFS,
                nombre_tabla=request.nombre_tabla_destino,
                nombre_capa=request.nombre_capa,
                titulo_capa=request.nombre_capa
            )

        engine_base_datos_entrada.dispose()
        engine_base_datos_distribucion.dispose()

        # Se registra la información de la publicación en la base de datos del sistema
        publicacion: PublicacionEntidad = PublicacionEntidad(
            identificador_base_datos_origen=request.identificador_base_datos_origen,
            nombre_esquema_origen=request.nombre_esquema_origen,
            nombre_tabla_origen=request.nombre_tabla_origen,
            nombre_tabla_destino=request.nombre_tabla_destino,
            nombre_espacio_trabajo=request.nombre_espacio_trabajo,
            nombre_capa=request.nombre_capa,
            titulo_capa=request.titulo_capa,
            habilitar_wms=request.habilitar_wms,
            habilitar_wfs=request.habilitar_wfs,
            created_by="admin"
        )
        resultado: InsertOneResult = Publicaciones.insert_one(publicacion.dict())
        publicacion_id: ObjectId = resultado.inserted_id

        publicacion_creada = Publicaciones.find_one({'_id': publicacion_id})
        if not publicacion_creada:
            raise ApplicationException("No se ha creado el registro para la publicación",
                                       status.HTTP_406_NOT_ACCEPTABLE)

        # Se registra la información de la capa en la base de datos del sistema
        capa: CapaEntidad = CapaEntidad(
            publicacion_id=str(publicacion_id),
            grupo_capa_id=request.grupo_capa_id,
            nombre=request.nombre_capa,
            titulo=request.titulo_capa,
            nombre_espacio_trabajo=request.nombre_espacio_trabajo,
            habilitar_wms=request.habilitar_wms,
            habilitar_wfs=request.habilitar_wfs,
            se_puede_descargar=request.se_puede_descargar,
            se_puede_consultar=request.se_puede_consultar,
            esta_habilitado=request.esta_habilitado,
            created_by="admin"
        )
        resultado: InsertOneResult = Capas.insert_one(capa.dict())
        capa_creada = Capas.find_one({'_id': resultado.inserted_id})
        if not capa_creada:
            raise ApplicationException("No se ha creado el registro para la capa", status.HTTP_406_NOT_ACCEPTABLE)

        return str(publicacion_id)
    except Exception as e:
        raise APIException(e)
