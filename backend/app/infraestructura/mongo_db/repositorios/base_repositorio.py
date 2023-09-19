from bson import ObjectId
from pymongo.collection import Collection
from pymongo.results import InsertOneResult, UpdateResult
from starlette import status
from typing import Type, TypeVar, List, Optional
from app.dominio.excepciones import (
    aplicacion_exception,
)

from app.dominio.repositorios.base_repositorio import (
    IBaseRepositorio,
)

T = TypeVar("T")


class BaseRepositorio(IBaseRepositorio[T]):
    def __init__(self, coleccion_mongo: Collection, clase_entidad: Type[T]):
        self.coleccion = coleccion_mongo
        self.clase_entidad = clase_entidad

    async def contar(self, filtros: Optional[dict] = None) -> int:
        return self.coleccion.count_documents(filtros or {})

    async def obtener_todos(self, filtros: Optional[dict] = None) -> List[T]:
        documentos = self.coleccion.find(filtros or {})
        respuesta = []
        for documento in documentos:
            identificador = str(documento["_id"])
            del documento["_id"]
            documento["id"] = identificador
            respuesta.append(self.clase_entidad(**documento))
        return respuesta

    async def obtener_por_id(self, id_entidad: str) -> T:
        documento = self.coleccion.find_one({"_id": ObjectId(id_entidad)})
        if not documento:
            raise aplicacion_exception(
                "Entidad no encontrada", status.HTTP_404_NOT_FOUND
            )
        identificador = str(documento["_id"])
        del documento["_id"]
        documento["id"] = identificador
        return self.clase_entidad(**documento)

    async def verificar_existencia(self, id_entidad: str) -> bool:
        num_elementos = self.coleccion.count_documents({"_id": ObjectId(id_entidad)})
        return num_elementos > 0

    async def crear(self, entidad: T) -> str:
        documento = entidad.dict()
        del documento["id"]
        resultado: InsertOneResult = self.coleccion.insert_one(documento)
        return str(resultado.inserted_id)

    async def actualizar(self, id_entidad: str, entidad: T) -> str:
        documento = entidad.dict()
        del documento["id"]
        resultado: UpdateResult = self.coleccion.update_one(
            {"_id": ObjectId(id_entidad)}, {"$set": documento}
        )
        return str(id_entidad if resultado.modified_count > 0 else None)

    async def eliminar(self, id_entidad: str) -> str:
        entidad: T = await self.obtener_por_id(id_entidad)
        entidad.state = False
        return await self.actualizar(id_entidad, entidad)
