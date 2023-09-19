from typing import Optional

from bson import ObjectId
from pymongo.results import InsertOneResult, UpdateResult
from starlette import status

from app.dominio.entidades.grupo_entidad import (
    GrupoEntidad,
)
from app.dominio.excepciones.aplicacion_exception import AplicacionException
from app.dominio.repositorios.grupo_repositorio import (
    IGrupoRepositorio,
)
from app.infraestructura.mongo_db.contextos.geogoremad_contexto import (
    Grupos,
)


class GrupoRepositorio(IGrupoRepositorio):
    """
    Repositorio de grupos.
    """

    async def contar(self, filtros: Optional[dict] = None) -> int:
        """
        Cuenta los grupos que cumplen con los filtros dados.
        """
        return Grupos.count_documents(filtros or {})

    async def obtener_todos(self, filtros: Optional[dict] = None) -> list[GrupoEntidad]:
        """
        Obtiene todos los grupos que cumplen con los filtros dados.
        """
        documentos = Grupos.find(filtros or {})
        respuesta = []
        for documento in documentos:
            identificador: str = str(documento["_id"])
            del documento["_id"]
            documento["id"] = identificador
            respuesta.append(GrupoEntidad(**documento))
        return respuesta

    async def obtener_por_id(self, grupo_id: str) -> GrupoEntidad:
        """
        Obtiene un grupo por su identificador único.
        """
        documento = Grupos.find_one({"_id": ObjectId(grupo_id)})
        if not documento:
            raise AplicacionException(
                "No se encontró el grupo", status.HTTP_404_NOT_FOUND
            )
        identificador: str = str(documento["_id"])
        del documento["_id"]
        documento["id"] = identificador
        return GrupoEntidad(**documento)

    async def crear(self, grupo: GrupoEntidad) -> str:
        """
        Crea un nuevo grupo.
        """
        documento: dict = grupo.dict()
        del documento["id"]
        resultado: InsertOneResult = Grupos.insert_one(documento)
        return str(resultado.inserted_id)

    async def actualizar(self, grupo_id: str, grupo: GrupoEntidad) -> str:
        """
        Actualiza un grupo existente por su identificador único.
        """
        documento: dict = grupo.dict()
        del documento["id"]
        resultado: UpdateResult = Grupos.update_one(
            {"_id": ObjectId(grupo_id)}, {"$set": documento}
        )
        return str(grupo_id if resultado.modified_count > 0 else None)

    async def eliminar(self, grupo_id: str, usuario_auditoria_id: str) -> str:
        """
        Elimina un grupo (cambia su estado a 'False').
        """
        grupo: GrupoEntidad = await self.obtener_por_id(grupo_id)
        grupo.estado = False
        grupo.registrar_actualizacion(usuario_auditoria_id)
        return await self.actualizar(grupo_id, grupo)

    async def obtener_por_filtros(
        self, filtros: Optional[dict] = None
    ) -> Optional[GrupoEntidad]:
        """
        Obtiene un grupo basado en los filtros dados.
        """
        documento = Grupos.find_one(filtros or {})
        if not documento:
            return None
        identificador: str = str(documento["_id"])
        del documento["_id"]
        documento["id"] = identificador
        return GrupoEntidad(**documento)
