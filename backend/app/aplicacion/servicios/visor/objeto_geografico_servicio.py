import json
from typing import List

import geopandas as gpd
import psycopg2
from fastapi import Depends
from psycopg2.extras import RealDictCursor
from shapely import wkt
from sqlalchemy.engine import make_url
from starlette import status

from app.aplicacion.dtos.visor.obtener_geojson_response import ORIGEN_POSTGRESQL, ESTILO_PREDETERMINADO
from app.aplicacion.dtos.visor.obtener_geometria_objeto_geografico_response import \
    ObtenerGeometriaObjetoGeograficoResponse
from app.aplicacion.parseadores.base_modelo import BaseModelo
from app.dependencies import registrar_repo_objeto_geografico, registrar_repo_objeto_geografico_geometria
from app.dominio.entidades.objeto_geografico_entidad import ObjetoGeograficoEntidad
from app.dominio.excepciones.aplicacion_exception import AplicacionException
from app.dominio.repositorios.base_repositorio import IBaseRepositorio
from app.settings import settings


class ColumnaObjetoGeograficoModelo(BaseModelo):
    columnas: List[str]
    alias: dict


class GeometriaObjetoGeograficoModelo(BaseModelo):
    crs: str
    geometrias: List[dict]


class ObjetoGeograficoServicio:

    def __init__(self,
                 objeto_geografico_repositorio: IBaseRepositorio = Depends(registrar_repo_objeto_geografico),
                 objeto_geografico_geometria_repositorio: IBaseRepositorio = Depends(
                     registrar_repo_objeto_geografico_geometria)):
        self._objeto_geografico_repositorio = objeto_geografico_repositorio
        self._objeto_geografico_informacion_repositorio = objeto_geografico_geometria_repositorio

    async def obtener_objeto_geografico_por_id(self, objeto_geografico_id: str) -> ObjetoGeograficoEntidad:
        objeto_geografico: ObjetoGeograficoEntidad = await self._objeto_geografico_repositorio.obtener_por_id(
            objeto_geografico_id)
        if not objeto_geografico.esta_habilitado:
            raise AplicacionException("El objeto geográfico no está habilitado")
        return objeto_geografico

    @staticmethod
    async def obtener_cursor(nombre_base_datos: str):
        url = make_url(settings.CADENA_CONEXION_POSTGIS)

        try:
            conn = psycopg2.connect(
                host=url.host,
                port=url.port,
                dbname=nombre_base_datos,
                user=url.username,
                password=url.password
            )
            cur = conn.cursor(cursor_factory=RealDictCursor)  # Para obtener los datos como diccionario.
        except Exception:
            raise AplicacionException("No se pudo conectar a la base de datos", status.HTTP_500_INTERNAL_SERVER_ERROR)

        return cur, conn

    async def obtener_geometrias_desde_postgis(self, nombre_base_datos: str, nombre_esquema: str,
                                               nombre_tabla: str) -> GeometriaObjetoGeograficoModelo:
        cur, conn = await self.obtener_cursor(nombre_base_datos)

        # Consulta de las columnas.

        consulta_columnas = f"""
            SELECT column_name FROM information_schema.columns
            WHERE table_name = '{nombre_tabla}' AND table_schema = '{nombre_esquema}';
        """
        cur.execute(consulta_columnas)
        columnas: list[dict] = cur.fetchall()

        # Consulta de la geometria.

        columna_id: str = columnas[0]["column_name"]
        columnas_para_consulta: list[str] = [f'"{columna_id}"', 'ST_AsText("geom") AS "geom"']

        consulta_datos = f"""
                    SELECT {", ".join(columnas_para_consulta)} FROM "{nombre_esquema}"."{nombre_tabla}";
                """
        cur.execute(consulta_datos)
        resultado_datos = cur.fetchall()
        datos = [dict(resultado) for resultado in resultado_datos]

        consulta_crs = f"""
            SELECT Find_SRID('{nombre_esquema}', '{nombre_tabla}', 'geom');
        """
        cur.execute(consulta_crs)
        resultado_crs = cur.fetchone()
        crs = f"EPSG:{resultado_crs['find_srid']}"

        cur.close()
        conn.close()

        return GeometriaObjetoGeograficoModelo(
            crs=crs,
            geometrias=datos
        )

    async def obtener_geometria(self, objeto_geografico_id: str) -> ObtenerGeometriaObjetoGeograficoResponse:
        objeto_geografico: ObjetoGeograficoEntidad = await self.obtener_objeto_geografico_por_id(objeto_geografico_id)

        # Estlos.

        try:
            estilo_renderizado = json.loads(objeto_geografico.estilo)
            estilo = json.dumps(estilo_renderizado)
        except TypeError:
            estilo = json.dumps(ESTILO_PREDETERMINADO)

        geometrias_objeto_geografico = await self.obtener_geometrias_desde_postgis(
            objeto_geografico.nombre_base_datos,
            objeto_geografico.nombre_esquema,
            objeto_geografico.nombre_tabla
        )

        # Geometrias.

        for geom in geometrias_objeto_geografico.geometrias:
            geom["geom"] = wkt.loads(geom["geom"])

        gdf = gpd.GeoDataFrame(geometrias_objeto_geografico.geometrias, geometry="geom",
                               crs=geometrias_objeto_geografico.crs)
        gdf = gdf.to_crs("EPSG:4326")
        bounding_box = gdf.total_bounds.tolist()

        return ObtenerGeometriaObjetoGeograficoResponse(
            id=objeto_geografico.id,
            origen=ORIGEN_POSTGRESQL,
            nombre=objeto_geografico.nombre,
            descripcion=objeto_geografico.descripcion,
            estilo=estilo,
            geometria=gdf.to_json(),
            cuadro_delimitador=bounding_box,
            codigo=objeto_geografico.codigo,
        )

    async def obtener_alias_columnas(self, nombre_base_datos: str, nombre_esquema: str, nombre_tabla) -> dict:

        cur, conn = await self.obtener_cursor(nombre_base_datos)

        # Consulta de comentarios y columnas.

        consulta_columnas_comentarios = f"""
                            SELECT column_name, pgd.description
                            FROM information_schema.columns AS cols
                            LEFT JOIN pg_catalog.pg_description AS pgd
                            ON (
                                pgd.objoid = (
                                    SELECT oid FROM pg_catalog.pg_class 
                                    WHERE relname = '{nombre_tabla}' 
                                    AND relnamespace = (SELECT oid FROM pg_catalog.pg_namespace 
                                                        WHERE nspname = '{nombre_esquema}')
                                )
                                AND pgd.objsubid = cols.ordinal_position
                            )
                            WHERE table_name = '{nombre_tabla}' 
                            AND table_schema = '{nombre_esquema}';
                        """
        cur.execute(consulta_columnas_comentarios)
        columnas_comentarios: list[dict] = cur.fetchall()

        alias = {}
        for columna_comentario in columnas_comentarios:
            nueva_propiedad = columna_comentario["description"]
            nueva_propiedad = nueva_propiedad.replace("\"", "")  # Eliminar comillas dobles.
            nueva_propiedad = nueva_propiedad.strip()  # Eliminar espacios en blanco.

            alias[columna_comentario["column_name"]] = nueva_propiedad
        return alias

    async def obtener_propiedades(self, objeto_geografico_id: str, registro_id: str) -> dict:
        objeto_geografico: ObjetoGeograficoEntidad = await self.obtener_objeto_geografico_por_id(objeto_geografico_id)

        alias_catalogo = await self.obtener_alias_columnas(objeto_geografico.nombre_base_datos,
                                                           objeto_geografico.nombre_esquema,
                                                           objeto_geografico.nombre_tabla)

        # Consulta de las columas.

        if alias_catalogo == {}:
            raise AplicacionException("No se encontraron columnas con comentarios",
                                      status.HTTP_500_INTERNAL_SERVER_ERROR)
        alias_catalogo.pop("geom")  # Eliminar la columna geom.

        # Consulta del registro.

        cur, conn = await self.obtener_cursor(objeto_geografico.nombre_base_datos)

        columna_id = list(alias_catalogo.keys())[0]
        columnas_para_consultar = [f'"{columna}"' for columna in alias_catalogo.keys()]
        consulta_registro = f"""
            SELECT {", ".join(columnas_para_consultar)} FROM 
            "{objeto_geografico.nombre_esquema}"."{objeto_geografico.nombre_tabla}"
            WHERE "{columna_id}" = '{registro_id}';
        """

        cur.execute(consulta_registro)
        resultado_registro = cur.fetchone()
        registro = dict(resultado_registro)

        return {alias_catalogo[columna]: registro[columna] for columna in alias_catalogo.keys()}

    async def obtener_informaciones(self, objeto_geografico_id: str) -> dict:
        objeto_geografico: ObjetoGeograficoEntidad = await self.obtener_objeto_geografico_por_id(objeto_geografico_id)

        alias_catalogo = await self.obtener_alias_columnas(objeto_geografico.nombre_base_datos,
                                                           objeto_geografico.nombre_esquema,
                                                           objeto_geografico.nombre_tabla)

        # Consulta de las columas.

        if alias_catalogo == {}:
            raise AplicacionException("No se encontraron columnas con comentarios",
                                      status.HTTP_500_INTERNAL_SERVER_ERROR)
        alias_catalogo.pop("geom")  # Eliminar la columna geom.

        columnas: List[str] = list(alias_catalogo.keys())
        alias: dict = alias_catalogo

        # Consulta del registro.

        cur, conn = await self.obtener_cursor(objeto_geografico.nombre_base_datos)

        columnas_para_consultar = [f'"{columna}"' for columna in alias_catalogo.keys()]
        consulta_registro = f"""
                    SELECT {", ".join(columnas_para_consultar)} FROM 
                    "{objeto_geografico.nombre_esquema}"."{objeto_geografico.nombre_tabla}";
                """
        cur.execute(consulta_registro)
        resultado_registro = cur.fetchall()

        registros = []
        for registro in resultado_registro:
            registros.append({columna: registro[columna] for columna in alias_catalogo.keys()})

        return {
            "columnas": columnas,
            "alias": alias,
            "registros": registros,
            "codigo": objeto_geografico.codigo,
            "nombre": objeto_geografico.nombre,
            "descripcion": objeto_geografico.descripcion,
            "estilo": objeto_geografico.estilo
        }
