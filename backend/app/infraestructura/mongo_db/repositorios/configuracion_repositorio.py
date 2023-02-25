from typing import Optional

from bson import ObjectId
from pymongo.results import UpdateResult, InsertManyResult, InsertOneResult
from starlette import status

from app.dominio.entidades.configuracion_entidad import ConfiguracionEntidad
from app.dominio.excepciones.aplicacion_exception import AplicacionException
from app.dominio.repositorios.configuracion_repositorio import IConfiguracionRepositorio
from app.infraestructura.mongo_db.contextos.geogoremad_contexto import Configuraciones


class ConfiguracionRepositorio(IConfiguracionRepositorio):
    """
    Repositorio de configuraciones.
    """

    async def contar(self, filtros: Optional[dict] = None) -> int:
        return Configuraciones.count_documents(filtros or {})

    async def obtener_todos(self, filtros: Optional[dict] = None) -> list[ConfiguracionEntidad]:
        documentos = Configuraciones.find(filtros or {})
        respuesta = []
        for documento in documentos:
            identificador: str = str(documento["_id"])
            del documento["_id"]
            documento["id"] = identificador
            respuesta.append(ConfiguracionEntidad(**documento))
        return respuesta

    async def obtener_por_id(self, configuracion_id: str) -> ConfiguracionEntidad:
        documento = Configuraciones.find_one({"_id": ObjectId(configuracion_id)})
        if not documento:
            raise AplicacionException("No se encontró la configuración", status.HTTP_404_NOT_FOUND)
        identificador: str = str(documento["_id"])
        del documento["_id"]
        documento["id"] = identificador
        return ConfiguracionEntidad(**documento)

    async def verificar_existencia(self, configuracion_id: str) -> bool:
        numero_elementos: int = Configuraciones.count_documents({"_id": ObjectId(configuracion_id)})
        return numero_elementos > 0

    async def crear(self, configuracion: ConfiguracionEntidad) -> str:
        documento: dict = configuracion.dict()
        del documento["id"]
        resultado: InsertOneResult = Configuraciones.insert_one(documento)
        return str(resultado.inserted_id)

    async def actualizar(self, configuracion_id: str, configuracion: ConfiguracionEntidad) -> str:
        documento: dict = configuracion.dict()
        del documento["id"]
        resultado: UpdateResult = Configuraciones.update_one({"_id": ObjectId(configuracion_id)}, {"$set": documento})
        return str(configuracion_id if resultado.modified_count > 0 else None)

    async def eliminar(self, configuracion_id: str, usuario_auditoria_id: str) -> str:
        configuracion: ConfiguracionEntidad = await self.obtener_por_id(configuracion_id)
        configuracion.estado = False
        configuracion.registrar_actualizacion(usuario_auditoria_id)
        return await self.actualizar(configuracion_id, configuracion)

    async def obtener_por_filtros(self, filtros: Optional[dict] = None) -> Optional[ConfiguracionEntidad]:
        documento = Configuraciones.find_one(filtros or {})
        if not documento:
            return None
        identificador: str = str(documento["_id"])
        del documento["_id"]
        documento["id"] = identificador
        return ConfiguracionEntidad(**documento)

    async def verificar_existencia_por_filtros(self, filtros: Optional[dict] = None) -> bool:
        numero_elementos: int = Configuraciones.count_documents(filtros or {})
        return numero_elementos > 0

    async def crear_multiple(self, configuraciones: list[ConfiguracionEntidad]) -> list[str]:
        documentos: list[dict] = []
        for configuracion in configuraciones:
            documento: dict = configuracion.dict()
            del documento["id"]
            documentos.append(documento)
        resultado: InsertManyResult = Configuraciones.insert_many(documentos)
        return [str(identificador) for identificador in resultado.inserted_ids]

    async def obtener_valor_por_clave(self, clave: str) -> str:
        documento = Configuraciones.find_one({"nombre": clave})
        if not documento:
            raise AplicacionException("No se encontró la configuración", status.HTTP_404_NOT_FOUND)
        return documento["valor"]
