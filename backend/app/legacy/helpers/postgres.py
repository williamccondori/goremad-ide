import math
import random

from sqlalchemy import create_engine

from exceptions import ApplicationException
from settings import settings

ESQUEMAS_RESERVADOS: list[str] = ['information_schema', 'pg_catalog', 'pg_toast', 'public', 'cron', 'topology']

TIPO_COLUMNAS_SIN_TAMANIO_FIJO: list[str] = ['geometry', 'text', 'integer', 'smallint', 'bigint', 'double precision',
                                             'boolean',
                                             'date', 'timestamp', 'timestamp with time zone',
                                             'timestamp without time zone']

IDENTIFICADOR_BASE_DATOS_FORESTAL: str = 'forestal'
IDENTIFICADOR_BASE_DATOS_PRODUCCION_FUNDAMENTALES: str = 'produccion_fundamentales'
IDENTIFICADOR_BASE_DATOS_PRODUCCION_FORESTAL: str = 'produccion_forestal'
IDENTIFICADOR_BASE_DATOS_DISTRIBUCION: str = 'distribucion'

PREFIJO_VISTA: str = 'Vista_'


def obtener_cadena_conexion_base_datos_forestal() -> str:
    return f"postgresql://{settings.FOREST_DATABASE_USER}:{settings.FOREST_DATABASE_PASSWORD}@" \
           f"{settings.FOREST_DATABASE_HOST}:{settings.FOREST_DATABASE_PORT}/" \
           f"{settings.FOREST_DATABASE_NAME}"


def obtener_cadena_conexion_base_datos_produccion_fundamentales() -> str:
    return f"postgresql://{settings.BASE_DATOS_PRODUCCION_FUNDAMENTALES_USUARIO}:" \
           f"{settings.BASE_DATOS_PRODUCCION_FUNDAMENTALES_PASSWORD}" \
           f"@{settings.BASE_DATOS_PRODUCCION_FUNDAMENTALES_HOST}" \
           f":{settings.BASE_DATOS_PRODUCCION_FUNDAMENTALES_PUERTO}" \
           f"/{settings.BASE_DATOS_PRODUCCION_FUNDAMENTALES_NOMBRE}"


def obtener_cadena_conexion_base_datos_produccion_forestal() -> str:
    return f"postgresql://{settings.PRODUCTION_FOREST_DATABASE_USER}:{settings.PRODUCTION_FOREST_DATABASE_PASSWORD}@" \
           f"{settings.PRODUCTION_FOREST_DATABASE_HOST}:{settings.PRODUCTION_FOREST_DATABASE_PORT}/" \
           f"{settings.PRODUCTION_FOREST_DATABASE_NAME}"


def obtener_cadena_conexion_base_datos_distribucion() -> str:
    return f"postgresql://{settings.DISTRIBUTION_DATABASE_USER}:{settings.DISTRIBUTION_DATABASE_PASSWORD}@" \
           f"{settings.DISTRIBUTION_DATABASE_HOST}:{settings.DISTRIBUTION_DATABASE_PORT}/" \
           f"{settings.DISTRIBUTION_DATABASE_NAME}"


def obtener_cadena_conexion_base_datos(
        identificador_base_datos: str
) -> str:
    if identificador_base_datos == IDENTIFICADOR_BASE_DATOS_FORESTAL:
        return obtener_cadena_conexion_base_datos_forestal()
    elif identificador_base_datos == IDENTIFICADOR_BASE_DATOS_PRODUCCION_FUNDAMENTALES:
        return obtener_cadena_conexion_base_datos_produccion_fundamentales()
    elif identificador_base_datos == IDENTIFICADOR_BASE_DATOS_PRODUCCION_FORESTAL:
        return obtener_cadena_conexion_base_datos_produccion_forestal()
    elif identificador_base_datos == IDENTIFICADOR_BASE_DATOS_DISTRIBUCION:
        return obtener_cadena_conexion_base_datos_distribucion()
    else:
        raise ApplicationException("El identificador de la base de datos no es válido")


def obtener_esquemas(
        identificador_base_datos: str
) -> list[dict]:
    engine = create_engine(obtener_cadena_conexion_base_datos(identificador_base_datos))

    resultados = engine.execute(
        f"select schema_name from information_schema.schemata where schema_name not in {tuple(ESQUEMAS_RESERVADOS)};"
    ).fetchall()

    engine.dispose()

    return [dict(elemento) for elemento in resultados]


def obtener_tablas(
        identificador_base_datos: str,
        nombre_esquema: str
) -> list[dict]:
    engine = create_engine(obtener_cadena_conexion_base_datos(identificador_base_datos))

    resultados = engine.execute(
        f"select table_name, table_schema from information_schema.tables where table_schema = '{nombre_esquema}';"
    ).fetchall()

    engine.dispose()

    return [dict(elemento) for elemento in resultados]


def existe_esquema(
        identificador_base_datos: str,
        nombre_esquema: str
) -> bool:
    engine = create_engine(obtener_cadena_conexion_base_datos(identificador_base_datos))

    resultados = engine.execute(
        f"select count(*) from information_schema.schemata where schema_name = '{nombre_esquema}';"
    ).fetchall()

    engine.dispose()

    return resultados[0][0] > 0


def obtener_columna_descripcion(
        identificador_base_datos: str,
        nombre_esquema: str,
        nombre_tabla: str
) -> str:
    posibles_descripciones = [
        'descripcion',
        'etiqueta',
        'valor',
    ]
    script_consulta = f"select column_name from information_schema.columns where table_schema = '{nombre_esquema}' " \
                      f"and table_name = '{nombre_tabla}' and lower(column_name) in {tuple(posibles_descripciones)};"
    engine = create_engine(obtener_cadena_conexion_base_datos(identificador_base_datos))

    resultados = engine.execute(script_consulta).fetchall()

    engine.dispose()

    return resultados[0][0] if resultados else None


def obtener_columnas_desde_tabla(
        identificador_base_datos: str,
        nombre_esquema: str,
        nombre_tabla: str,
        incluir_llaves_foraneas: bool = False
) -> tuple[list[dict], list[dict]]:
    engine = create_engine(obtener_cadena_conexion_base_datos(identificador_base_datos))
    resultados = engine.execute(
        f"""
        select 
          co.ordinal_position as column_order, 
          co.column_name, 
          case when co.udt_name = 'geometry' then (
            co.udt_name || '(' || gc.type || ',' || gc.srid || ')'
          ) else co.data_type end as column_type, 
          case when co.is_nullable = 'YES' then true else false end as column_nullable, 
          col_description(
            (
              '"' || co.table_schema || '"."' || co.table_name || '"'
            ):: regclass :: oid, 
            ordinal_position
          ) as column_description, 
          case when co.character_maximum_length is null then co.numeric_precision :: text || 
          case when co.numeric_scale = 0 then '' else (',' || co.numeric_scale :: text) 
          end else co.character_maximum_length :: text end as column_size 
        from 
          information_schema.columns as co 
          left join geometry_columns AS gc on (
            co.table_schema = gc.f_table_schema 
            and co.table_name = gc.f_table_name 
            and co.column_name = gc.f_geometry_column
          ) 
        where 
          co.table_schema = '{nombre_esquema}' 
          and co.table_name = '{nombre_tabla}';
        """
    ).fetchall()
    columnas = [dict(elemento) for elemento in resultados]

    # Consulta de llaves foráneas
    llaves_foraneas = []
    if incluir_llaves_foraneas:
        resultados = engine.execute(
            f"""
            select 
              tc.constraint_name, 
              kcu.column_name, 
              ccu.table_schema as foreign_table_schema, 
              ccu.table_name as foreign_table_name, 
              ccu.column_name as foreign_column_name 
            from 
              information_schema.table_constraints as tc 
              join information_schema.key_column_usage as kcu on tc.constraint_name = kcu.constraint_name 
              join information_schema.constraint_column_usage as ccu on ccu.constraint_name = tc.constraint_name 
            where 
              constraint_type = 'FOREIGN KEY' 
              and tc.table_schema = '{nombre_esquema}' 
              and tc.table_name = '{nombre_tabla}'
            """
        )
        llaves_foraneas = [dict(elemento) for elemento in resultados]

    engine.dispose()

    return columnas, llaves_foraneas


def generar_script_creacion_tabla(
        definicion_columnas: list[dict],
        nombre_tabla: str,
        nombre_esquema: str,
        incluir_eliminacion_tabla: bool = True,
        nombres_llaves_foraneas: list[str] = None
) -> str:
    nombres_llaves_foraneas = nombres_llaves_foraneas or []

    columnas = []
    comentarios_columna = []

    for definicion_columna in definicion_columnas:
        nombre_columna: str = definicion_columna["column_name"]
        if nombre_columna == "id":
            columnas.append(f""""{nombre_columna}" serial not null primary key""")
        else:
            # Se realiza el tratamiento del tipo de columna
            tipo_columna = definicion_columna["column_type"]
            if nombre_columna in nombres_llaves_foraneas:
                tipo_columna = "text"

            # Se realiza el tratamiento de aceptación de datos nulos de la columna
            columna_nula = ""
            if not definicion_columna["column_nullable"]:
                columna_nula = " not null"

            # Se realiza el tratamiento del tamaño de la columna
            tamanio_columna = definicion_columna["column_size"]
            if tipo_columna in TIPO_COLUMNAS_SIN_TAMANIO_FIJO:
                tamanio_columna = None
            tamanio_columna = f""" ({tamanio_columna})""" if tamanio_columna else ""

            columnas.append(f""""{nombre_columna}" {tipo_columna}{tamanio_columna}{columna_nula}""")

        # Se agregan los comentarios para cada columna
        descripcion_columna = definicion_columna['column_description']
        if descripcion_columna:
            comentarios_columna.append(
                f"""comment on column "{nombre_esquema}"."{nombre_tabla}" is '{descripcion_columna}';""")

    script_creacion = f"""create table "{nombre_esquema}"."{nombre_tabla}" ({', '.join(columnas)});{' '.join(comentarios_columna)}"""

    if incluir_eliminacion_tabla:
        script_creacion = f"""drop table if exists "{nombre_esquema}"."{nombre_tabla}" cascade; {script_creacion}"""

    return script_creacion


def generar_script_creacion_vista(
        definicion_columnas: list,
        nombre_tabla: str,
        nombre_esquema: str
) -> str:
    asignaciones = []
    for definicion_columna in definicion_columnas:
        nombre_columna = definicion_columna["column_name"]
        if nombre_columna == "id" or nombre_columna == "geom":
            asignaciones.append(f'"{nombre_columna}" as "{nombre_columna}"')
        else:
            asignaciones.append(f'"{nombre_columna}" as "{nombre_columna.upper()}"')
    return f"""create or replace view "{nombre_esquema}"."{PREFIJO_VISTA}{nombre_tabla}" as select {', '.join(asignaciones)} from "{nombre_esquema}"."{nombre_tabla}";"""


def generar_script_consulta_tabla(
        nombre_tabla: str,
        nombre_esquema: str,
        nombres_columna: list[str] = None
) -> str:
    if not nombres_columna:
        nombres_columna = ["*"]
    return f"""select {", ".join(nombres_columna)} from "{nombre_esquema}"."{nombre_tabla}";"""


def generar_script_consulta_tabla_con_relaciones(
        identificador_base_datos: str,
        nombre_tabla: str,
        nombre_esquema: str,
        nombres_columna: list[str] = None,
        definicion_llaves_foraneas: list[dict] = None,
        columna_descripcion=None
):
    if not nombres_columna:
        nombres_columna = ["*"]
    definicion_llaves_foraneas = definicion_llaves_foraneas or []

    joins = []
    alias_columna = []
    for nombre_columna in nombres_columna:
        definicion_relacion = next(
            (definicion_llave_foranea for definicion_llave_foranea in definicion_llaves_foraneas if
             definicion_llave_foranea["column_name"] == nombre_columna), None)

        if definicion_relacion:
            nombre_tabla_foranea = definicion_relacion["foreign_table_name"]
            nombre_esquema_foraneo = definicion_relacion["foreign_table_schema"]
            identificador = 'join' + str(math.floor(random.random() * 1000000))

            if not columna_descripcion:
                columna_descripcion = obtener_columna_descripcion(
                    identificador_base_datos=identificador_base_datos,
                    nombre_esquema=nombre_esquema_foraneo,
                    nombre_tabla=nombre_tabla_foranea
                ) or definicion_relacion['foreign_column_name']

            alias_columna.append(f'{identificador}."{columna_descripcion}" as "{nombre_columna}"')

            joins.append(
                f'left join "{nombre_esquema_foraneo}"."{nombre_tabla_foranea}" as '
                f'{identificador} on root."{definicion_relacion["column_name"]}" = '
                f'{identificador}."{definicion_relacion["foreign_column_name"]}"')
        else:
            alias_columna.append(f'root."{nombre_columna}" as "{nombre_columna}"')

    return f"""select {','.join(alias_columna)} from "{nombre_esquema}"."{nombre_tabla}" as root {' '.join(joins)}"""
