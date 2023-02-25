from typing import Optional

from bson import ObjectId
from pymongo.results import InsertOneResult, UpdateResult
from starlette import status

from app.dominio.entidades.grupo_capa_entidad import GrupoCapaEntidad
from app.dominio.excepciones.aplicacion_exception import AplicacionException
from app.dominio.repositorios.grupo_capa_repositorio import IGrupoCapaRepositorio
from app.infraestructura.mongo_db.contextos.geogoremad_contexto import GruposCapas


class GrupoCapaRepositorio(IGrupoCapaRepositorio):
    """
    Repositorio de grupos de capas.
    """

    async def contar(self, filtros: Optional[dict] = None) -> int:
        return GruposCapas.count_documents(filtros or {})

    async def obtener_todos(self, filtros: Optional[dict] = None) -> list[GrupoCapaEntidad]:
        documentos = GruposCapas.find(filtros or {})
        respuesta = []
        for documento in documentos:
            identificador: str = str(documento["_id"])
            del documento["_id"]
            documento["id"] = identificador
            respuesta.append(GrupoCapaEntidad(**documento))
        return respuesta

    async def obtener_por_id(self, grupo_capa_id: str) -> GrupoCapaEntidad:
        documento = GruposCapas.find_one({"_id": ObjectId(grupo_capa_id)})
        if not documento:
            raise AplicacionException("No se encontró el grupo de capas", status.HTTP_404_NOT_FOUND)
        identificador: str = str(documento["_id"])
        del documento["_id"]
        documento["id"] = identificador
        return GrupoCapaEntidad(**documento)

    async def verificar_existencia(self, grupo_capa_id: str) -> bool:
        numero_elementos: int = GruposCapas.count_documents({"_id": ObjectId(grupo_capa_id)})
        return numero_elementos > 0

    async def crear(self, grupo_capa: GrupoCapaEntidad) -> str:
        documento: dict = grupo_capa.dict()
        del documento["id"]
        resultado: InsertOneResult = GruposCapas.insert_one(documento)
        return str(resultado.inserted_id)

    async def actualizar(self, grupo_capa_id: str, grupo_capa: GrupoCapaEntidad) -> str:
        documento: dict = grupo_capa.dict()
        del documento["id"]
        resultado: UpdateResult = GruposCapas.update_one({"_id": ObjectId(grupo_capa_id)}, {"$set": documento})
        return str(grupo_capa_id if resultado.modified_count > 0 else None)

    async def eliminar(self, grupo_capa_id: str, grupo_capa_auditoria_id: str) -> str:
        grupo_capa: GrupoCapaEntidad = await self.obtener_por_id(grupo_capa_id)
        grupo_capa.estado = False
        grupo_capa.registrar_actualizacion(grupo_capa_auditoria_id)
        return await self.actualizar(grupo_capa_id, grupo_capa)

    async def obtener_por_filtros(self, filtros: Optional[dict] = None) -> Optional[GrupoCapaEntidad]:
        documento = GruposCapas.find_one(filtros or {})
        if not documento:
            return None
        identificador: str = str(documento["_id"])
        del documento["_id"]
        documento["id"] = identificador
        return GrupoCapaEntidad(**documento)

    async def verificar_existencia_por_filtros(self, filtros: Optional[dict] = None) -> bool:
        numero_elementos: int = GruposCapas.count_documents(filtros or {})
        return numero_elementos > 0
