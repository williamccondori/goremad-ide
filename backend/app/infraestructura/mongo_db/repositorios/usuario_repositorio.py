from typing import Optional

from bson import ObjectId
from pymongo.results import InsertOneResult, UpdateResult
from starlette import status

from app.dominio.entidades.usuario_entidad import UsuarioEntidad
from app.dominio.excepciones.aplicacion_exception import AplicacionException
from app.dominio.repositorios.usuario_repositorio import IUsuarioRepositorio
from app.infraestructura.mongo_db.contextos.geogoremad_contexto import Usuarios


class UsuarioRepositorio(IUsuarioRepositorio):
    """
    Repositorio de usuarios.
    """

    async def contar(self, filtros: Optional[dict] = None) -> int:
        return Usuarios.count_documents(filtros or {})

    async def obtener_todos(self, filtros: Optional[dict] = None) -> list[UsuarioEntidad]:
        documentos = Usuarios.find(filtros or {})
        respuesta = []
        for documento in documentos:
            identificador: str = str(documento["_id"])
            del documento["_id"]
            documento["id"] = identificador
            respuesta.append(UsuarioEntidad(**documento))
        return respuesta

    async def obtener_por_id(self, usuario_id: str) -> UsuarioEntidad:
        documento = Usuarios.find_one({"_id": ObjectId(usuario_id)})
        if not documento:
            raise AplicacionException("No se encontró el usuario", status.HTTP_404_NOT_FOUND)
        identificador: str = str(documento["_id"])
        del documento["_id"]
        documento["id"] = identificador
        return UsuarioEntidad(**documento)

    async def verificar_existencia(self, usuario_id: str) -> bool:
        numero_elementos: int = Usuarios.count_documents({"_id": ObjectId(usuario_id)})
        return numero_elementos > 0

    async def crear(self, usuario: UsuarioEntidad) -> str:
        documento: dict = usuario.dict()
        del documento["id"]
        resultado: InsertOneResult = Usuarios.insert_one(documento)
        return str(resultado.inserted_id)

    async def actualizar(self, usuario_id: str, usuario: UsuarioEntidad) -> str:
        documento: dict = usuario.dict()
        del documento["id"]
        resultado: UpdateResult = Usuarios.update_one({"_id": ObjectId(usuario_id)}, {"$set": documento})
        return str(usuario_id if resultado.modified_count > 0 else None)

    async def eliminar(self, usuario_id: str, usuario_auditoria_id: str) -> str:
        usuario: UsuarioEntidad = await self.obtener_por_id(usuario_id)
        usuario.estado = False
        usuario.registrar_actualizacion(usuario_auditoria_id)
        return await self.actualizar(usuario_id, usuario)

    async def obtener_por_filtros(self, filtros: Optional[dict] = None) -> Optional[UsuarioEntidad]:
        documento = Usuarios.find_one(filtros or {})
        if not documento:
            return None
        identificador: str = str(documento["_id"])
        del documento["_id"]
        documento["id"] = identificador
        return UsuarioEntidad(**documento)

    async def verificar_existencia_por_filtros(self, filtros: Optional[dict] = None) -> bool:
        numero_elementos: int = Usuarios.count_documents(filtros or {})
        return numero_elementos > 0
