from datetime import datetime
from typing import Type, TypeVar, List, Optional, Union

from bson import ObjectId
from pymongo.collection import Collection
from pymongo.results import InsertOneResult, UpdateResult
from starlette import status

from app.dominio.excepciones.aplicacion_exception import AplicacionException
from app.dominio.repositorios.base_repositorio import IBaseRepositorio

T = TypeVar("T")


class BaseRepositorio(IBaseRepositorio[T]):
    def __init__(self, coleccion_mongo: Collection, clase_entidad: Type[T]):
        self.coleccion = coleccion_mongo
        self.clase_entidad = clase_entidad

    async def contar(self, filtros: Optional[dict] = None) -> int:
        filtros_aplicados: dict = filtros or {}
        filtros_aplicados["estado"] = True
        return self.coleccion.count_documents(filtros_aplicados)

    async def obtener_todos(self, filtros: Optional[dict] = None) -> List[T]:
        filtros_aplicados: dict = filtros or {}
        filtros_aplicados["estado"] = True
        documentos = self.coleccion.find(filtros_aplicados)
        respuesta = []
        for documento in documentos:
            identificador: str = str(documento["_id"])
            del documento["_id"]
            documento["id"] = identificador
            respuesta.append(self.clase_entidad(**documento))
        return respuesta

    async def obtener_por_id(self, id_entidad: str) -> T:
        documento: dict = self.coleccion.find_one({"_id": ObjectId(id_entidad), "estado": True})
        if not documento:
            raise AplicacionException("No se encontró la entidad", status.HTTP_404_NOT_FOUND)
        identificador: str = str(documento["_id"])
        del documento["_id"]
        documento["id"] = identificador
        return self.clase_entidad(**documento)

    async def verificar_existencia(self, id_entidad: str) -> bool:
        return self.coleccion.count_documents({"_id": ObjectId(id_entidad), "estado": True}) > 0

    async def crear(self, entidad: T) -> str:
        documento = entidad.dict(exclude={"id"})
        resultado: InsertOneResult = self.coleccion.insert_one(documento)
        return str(resultado.inserted_id)

    async def actualizar(self, id_entidad: str, entidad: T) -> Union[str, None]:
        documento = entidad.dict(exclude={"id"})
        resultado: UpdateResult = self.coleccion.update_one({"_id": ObjectId(id_entidad)}, {"$set": documento})
        return id_entidad if resultado.modified_count > 0 else None

    async def eliminar(self, id_entidad: str, usuario_auditoria_id: str) -> str:
        entidad = await self.obtener_por_id(id_entidad)
        entidad.estado = False
        entidad.usuario_modificacion = usuario_auditoria_id
        entidad.fecha_modificacion = datetime.now()
        return await self.actualizar(id_entidad, entidad)

    async def obtener_por_filtros(self, filtros: Optional[dict] = None) -> Optional[T]:
        filtros_aplicados: dict = filtros or {}
        filtros_aplicados["estado"] = True
        documento: dict = self.coleccion.find_one(filtros_aplicados)
        if not documento:
            return None
        identificador: str = str(documento["_id"])
        del documento["_id"]
        documento["id"] = identificador
        return self.clase_entidad(**documento)

    async def verificar_existencia_por_filtros(self, filtros: Optional[dict] = None) -> bool:
        filtros_aplicados: dict = filtros or {}
        filtros_aplicados["estado"] = True
        return self.coleccion.count_documents(filtros_aplicados) > 0
