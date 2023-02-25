from typing import Optional

from bson import ObjectId
from pymongo.results import InsertOneResult, UpdateResult
from starlette import status

from app.dominio.entidades.publicacion_entidad import PublicacionEntidad
from app.dominio.excepciones.aplicacion_exception import AplicacionException
from app.dominio.repositorios.publicacion_repositorio import IPublicacionRepositorio
from app.infraestructura.mongo_db.contextos.geogoremad_contexto import Publicaciones


class PublicacionRepositorio(IPublicacionRepositorio):
    """
    Repositorio de publicaciones.
    """

    async def contar(self, filtros: Optional[dict] = None) -> int:
        return Publicaciones.count_documents(filtros or {})

    async def obtener_todos(self, filtros: Optional[dict] = None) -> list[PublicacionEntidad]:
        documentos = Publicaciones.find(filtros or {})
        respuesta = []
        for documento in documentos:
            identificador: str = str(documento["_id"])
            del documento["_id"]
            documento["id"] = identificador
            respuesta.append(PublicacionEntidad(**documento))
        return respuesta

    async def obtener_por_id(self, publicacion_id: str) -> PublicacionEntidad:
        documento = Publicaciones.find_one({"_id": ObjectId(publicacion_id)})
        if not documento:
            raise AplicacionException("No se encontró la publicación", status.HTTP_404_NOT_FOUND)
        identificador: str = str(documento["_id"])
        del documento["_id"]
        documento["id"] = identificador
        return PublicacionEntidad(**documento)

    async def verificar_existencia(self, publicacion_id: str) -> bool:
        numero_elementos: int = Publicaciones.count_documents({"_id": ObjectId(publicacion_id)})
        return numero_elementos > 0

    async def crear(self, publicacion: PublicacionEntidad) -> str:
        documento: dict = publicacion.dict()
        del documento["id"]
        resultado: InsertOneResult = Publicaciones.insert_one(documento)
        return str(resultado.inserted_id)

    async def actualizar(self, publicacion_id: str, publicacion: PublicacionEntidad) -> str:
        documento: dict = publicacion.dict()
        del documento["id"]
        resultado: UpdateResult = Publicaciones.update_one({"_id": ObjectId(publicacion_id)}, {"$set": documento})
        return str(publicacion_id if resultado.modified_count > 0 else None)

    async def eliminar(self, publicacion_id: str, usuario_auditoria_id: str) -> str:
        publicacion: PublicacionEntidad = await self.obtener_por_id(publicacion_id)
        publicacion.estado = False
        publicacion.registrar_actualizacion(usuario_auditoria_id)
        return await self.actualizar(publicacion_id, publicacion)

    async def obtener_por_filtros(self, filtros: Optional[dict] = None) -> Optional[PublicacionEntidad]:
        documento = Publicaciones.find_one(filtros or {})
        if not documento:
            return None
        identificador: str = str(documento["_id"])
        del documento["_id"]
        documento["id"] = identificador
        return PublicacionEntidad(**documento)

    async def verificar_existencia_por_filtros(self, filtros: Optional[dict] = None) -> bool:
        numero_elementos: int = Publicaciones.count_documents(filtros or {})
        return numero_elementos > 0
