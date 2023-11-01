from typing import Optional

from fastapi import Depends

from app.aplicacion.dtos.visor.capa_response import CapaResponse
from app.aplicacion.dtos.visor.obtener_inicial_response import (
    ObtenerInicialResponse,
    CapaBaseResponse,
    EstructuraCapaResponse,
)
from app.aplicacion.utilidades.wms import obtener_url_leyenda
from app.dependencies import registrar_repo_capa_base, registrar_repo_tema, registrar_repo_catalogo, \
    registrar_repo_grupo, registrar_repo_objeto_geografico
from app.dominio.entidades.capa_base_entidad import CapaBaseEntidad
from app.dominio.entidades.compartido.base_entidad import ESTADO_ACTIVO
from app.dominio.entidades.grupo_capa_entidad import GrupoCapaEntidad
from app.dominio.entidades.servicio_externo_entidad import ServicioExternoEntidad
from app.dominio.excepciones.aplicacion_exception import AplicacionException
from app.dominio.repositorios.base_repositorio import IBaseRepositorio
from app.dominio.repositorios.configuracion_repositorio import IConfiguracionRepositorio
from app.dominio.repositorios.grupo_capa_repositorio import IGrupoCapaRepositorio
from app.dominio.repositorios.servicio_externo_repositorio import (
    IServicioExternoRepositorio,
)
from app.infraestructura.mongo_db.repositorios.configuracion_repositorio import (
    ConfiguracionRepositorio,
)
from app.infraestructura.mongo_db.repositorios.grupo_capa_repositorio import (
    GrupoCapaRepositorio,
)
from app.infraestructura.mongo_db.repositorios.servicio_externo_repositorio import (
    ServicioExternoRepositorio,
)


class InicialServicio:
    def __init__(
            self,
            capa_base_repositorio: IBaseRepositorio = Depends(registrar_repo_capa_base),
            grupo_capa_repositorio: IGrupoCapaRepositorio = Depends(GrupoCapaRepositorio),
            servicio_externo_repositorio: IServicioExternoRepositorio = Depends(
                ServicioExternoRepositorio
            ),
            configuracion_repositorio: IConfiguracionRepositorio = Depends(
                ConfiguracionRepositorio
            ),
            catalogo_repositorio: IBaseRepositorio = Depends(registrar_repo_catalogo),
            tema_repositorio: IBaseRepositorio = Depends(registrar_repo_tema),
            grupo_repositorio: IBaseRepositorio = Depends(registrar_repo_grupo),
            obejto_geografico_repositorio: IBaseRepositorio = Depends(registrar_repo_objeto_geografico),
    ):
        self._capa_base_repositorio = capa_base_repositorio
        self._grupo_capa_repositorio = grupo_capa_repositorio
        self._servicio_externo_repositorio = servicio_externo_repositorio
        self._configuracion_repositorio = configuracion_repositorio
        self._catalogo_repositorio = catalogo_repositorio
        self._tema_repositorio = tema_repositorio
        self._grupo_repositorio = grupo_repositorio
        self._obejto_geografico_repositorio = obejto_geografico_repositorio

    async def __obtener_hijos(
            self, grupo_capa_id: str, grupos_capas: list[GrupoCapaEntidad]
    ) -> list[EstructuraCapaResponse]:
        hijos: list[EstructuraCapaResponse] = []
        for grupo_capa in grupos_capas:
            if grupo_capa.grupo_capa_id == grupo_capa_id:
                hijos.append(
                    EstructuraCapaResponse(
                        id=grupo_capa.id,
                        label=grupo_capa.nombre,
                        children=await self.__obtener_hijos(
                            grupo_capa.id, grupos_capas
                        ),
                    )
                )
        hijos.extend(
            await self.__obtener_servicios_externos(grupo_capa_id=grupo_capa_id)
        )
        return hijos

    async def __obtener_estructura_grupos_capas(
            self, grupos_capas: list[GrupoCapaEntidad]
    ) -> list[EstructuraCapaResponse]:
        raices: list[EstructuraCapaResponse] = []
        for grupo_capa in grupos_capas:
            if not grupo_capa.grupo_capa_id:
                raices.append(
                    EstructuraCapaResponse(
                        id=grupo_capa.id,
                        label=grupo_capa.nombre,
                        children=await self.__obtener_hijos(
                            grupo_capa.id, grupos_capas
                        ),
                    )
                )
        raices.extend(await self.__obtener_servicios_externos(None))
        return raices

    async def __obtener_servicios_externos(
            self, grupo_capa_id: Optional[str]
    ) -> list[EstructuraCapaResponse]:
        servicios_externos: list[
            ServicioExternoEntidad
        ] = await self._servicio_externo_repositorio.obtener_todos(
            {
                "estado": ESTADO_ACTIVO,
                "esta_habilitado": True,
                "grupo_capa_id": grupo_capa_id,
            }
        )
        return [
            EstructuraCapaResponse(
                id=servicio_externo.id,
                label=servicio_externo.nombre,
                children=[
                    EstructuraCapaResponse(
                        id=f"{servicio_externo.id}__{capa.nombre}",
                        label=capa.titulo,
                        children=[],
                        es_grupo=False,
                    )
                    for capa in servicio_externo.capas
                ],
            )
            for servicio_externo in servicios_externos
        ]

    async def obtener_inicial(self) -> ObtenerInicialResponse:
        # Se obtienen las capas base.
        capas_base: list[
            CapaBaseEntidad
        ] = await self._capa_base_repositorio.obtener_todos(
            {"estado": ESTADO_ACTIVO, "esta_habilitado": True}
        )
        if len(capas_base) == 0:
            raise AplicacionException("No se encontraron capas bases activas")
        # Se obtienen los servicios externos.
        servicios_externos: list[
            ServicioExternoEntidad
        ] = await self._servicio_externo_repositorio.obtener_todos(
            {"estado": ESTADO_ACTIVO, "esta_habilitado": True}
        )
        servicios_externos_con_capas: list[CapaResponse] = []
        for servicio_externo in servicios_externos:
            for capa in servicio_externo.capas:
                url_leyenda: str = obtener_url_leyenda(
                    servicio_externo.url, capa.nombre
                )
                servicios_externos_con_capas.append(
                    CapaResponse(
                        id=f"{servicio_externo.id}__{capa.nombre}",
                        servicio_id=servicio_externo.id,
                        servicio_titulo=servicio_externo.nombre,
                        nombre=capa.nombre,
                        titulo=capa.titulo,
                        url=self.__obtener_url(servicio_externo.url, servicio_externo.filtros),
                        url_query=servicio_externo.url,
                        filtros=servicio_externo.filtros,
                        url_leyenda=url_leyenda,
                        atribucion=servicio_externo.atribucion,
                        cuadro_delimitador=capa.cuadro_delimitador,
                        grupo_capa_id=servicio_externo.grupo_capa_id,
                        transparencia=1,
                    )
                )
        # Creación de la estructura de capas y grupos de capas
        grupos_capas: list[
            GrupoCapaEntidad
        ] = await self._grupo_capa_repositorio.obtener_todos(
            {"estado": ESTADO_ACTIVO, "esta_habilitado": True}
        )
        elementos_no_agrupados: list[
            EstructuraCapaResponse
        ] = await self.__obtener_estructura_grupos_capas(grupos_capas)
        estructura: EstructuraCapaResponse = EstructuraCapaResponse(
            id="root", label="Todos los elementos", children=elementos_no_agrupados
        )
        # Consulta de las configuraciones iniciales
        capa_base_incial_id: str = (
            await self._configuracion_repositorio.obtener_valor_por_clave(
                clave="capa_base_incial_id"
            )
        )
        capa_base_incial_id = (
            capa_base_incial_id if capa_base_incial_id else capas_base[0].id
        )
        latitud_inicial: float = float(
            await self._configuracion_repositorio.obtener_valor_por_clave(
                clave="latitud_inicial"
            )
        )
        longitud_inicial: float = float(
            await self._configuracion_repositorio.obtener_valor_por_clave(
                clave="longitud_inicial"
            )
        )
        zoom_inicial: int = int(
            await self._configuracion_repositorio.obtener_valor_por_clave(
                clave="zoom_inicial"
            )
        )
        capas_activas_id: str = (
            await self._configuracion_repositorio.obtener_valor_por_clave(
                clave="servicios_externos_activos"
            )
        )
        capas_activas: list[str] = (
            capas_activas_id.split(",") if capas_activas_id else []
        )

        # Se obtiene la estructura de objetos geograficos.
        estructura_objetos_geograficos: list[dict] = []
        catalogos = await self._catalogo_repositorio.obtener_todos()
        for catalogo in catalogos:
            estructura_objetos_geograficos.append({
                "id": catalogo.id,
                "nombre": catalogo.nombre,
                "temas": [{
                    "id": tema.id,
                    "nombre": f"📁 {tema.nombre}",
                    "grupos": [{
                        "id": grupo.id,
                        "nombre": f"📁 {grupo.nombre}",
                        "objetos": [{
                            "id": objeto_geografico.id,
                            "nombre": f"📄 {objeto_geografico.nombre}"
                        } for objeto_geografico in
                            await self._obejto_geografico_repositorio.obtener_todos({"grupo_id": grupo.id})]
                    } for grupo in await self._grupo_repositorio.obtener_todos({"tema_id": tema.id})]
                } for tema in await self._tema_repositorio.obtener_todos({"catalogo_id": catalogo.id})]
            })

        return ObtenerInicialResponse(
            estructura=[estructura],
            capas_base=[
                CapaBaseResponse(
                    id=capa_base.id,
                    nombre=capa_base.nombre,
                    url=capa_base.url,
                    atribucion=capa_base.atribucion,
                )
                for capa_base in capas_base
            ],
            capas_activas=capas_activas,
            servicios_externos=servicios_externos_con_capas,
            capa_base_incial_id=capa_base_incial_id,
            latitud_inicial=latitud_inicial,
            longitud_inicial=longitud_inicial,
            zoom_inicial=zoom_inicial,
            estructura_objetos_geograficos=estructura_objetos_geograficos
        )

    @staticmethod
    def __obtener_url(wms_url: str, filtros: str) -> str:
        if filtros:
            return f"{wms_url}?CQL_FILTER={filtros}"
        return wms_url
