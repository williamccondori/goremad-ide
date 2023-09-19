from typing import Optional

from bson import ObjectId
from pymongo.results import InsertOneResult, UpdateResult
from starlette import status

from app.dominio.entidades.catalogo_entidad import (
    CatalogoEntidad,
)
from app.dominio.excepciones.aplicacion_exception import AplicacionException
from app.dominio.repositorios.catalogo_repositorio import (
    ICatalogoRepositorio,
)
from app.infraestructura.mongo_db.contextos.geogoremad_contexto import (
    Catalogos,
)


class CatalogoRepositorio(ICatalogoRepositorio):
    """
    Repositorio de catálogos.
    """

    async def contar(self, filtros: Optional[dict] = None) -> int:
        """
        Cuenta los catálogos que cumplen con los filtros dados.
        """
        return Catalogos.count_documents(filtros or {})

    async def obtener_todos(
        self, filtros: Optional[dict] = None
    ) -> list[CatalogoEntidad]:
        """
        Obtiene todos los catálogos que cumplen con los filtros dados.
        """
        documentos = Catalogos.find(filtros or {})
        respuesta = []
        for documento in documentos:
            identificador: str = str(documento["_id"])
            del documento["_id"]
            documento["id"] = identificador
            respuesta.append(CatalogoEntidad(**documento))
        return respuesta

    async def obtener_por_id(self, catalogo_id: str) -> CatalogoEntidad:
        """
        Obtiene un catálogo por su identificador único.
        """
        documento = Catalogos.find_one({"_id": ObjectId(catalogo_id)})
        if not documento:
            raise AplicacionException(
                "No se encontró el catálogo", status.HTTP_404_NOT_FOUND
            )
        identificador: str = str(documento["_id"])
        del documento["_id"]
        documento["id"] = identificador
        return CatalogoEntidad(**documento)

    async def crear(self, catalogo: CatalogoEntidad) -> str:
        """
        Crea un nuevo catálogo.
        """
        documento: dict = catalogo.dict()
        del documento["id"]
        resultado: InsertOneResult = Catalogos.insert_one(documento)
        return str(resultado.inserted_id)

    async def actualizar(self, catalogo_id: str, catalogo: CatalogoEntidad) -> str:
        """
        Actualiza un catálogo existente por su identificador único.
        """
        documento: dict = catalogo.dict()
        del documento["id"]
        resultado: UpdateResult = Catalogos.update_one(
            {"_id": ObjectId(catalogo_id)}, {"$set": documento}
        )
        return str(catalogo_id if resultado.modified_count > 0 else None)

    async def eliminar(self, catalogo_id: str, usuario_auditoria_id: str) -> str:
        """
        Elimina un catálogo (cambia su estado a 'False').
        """
        catalogo: CatalogoEntidad = await self.obtener_por_id(catalogo_id)
        catalogo.estado = False
        catalogo.registrar_actualizacion(usuario_auditoria_id)
        return await self.actualizar(catalogo_id, catalogo)

    async def obtener_por_filtros(
        self, filtros: Optional[dict] = None
    ) -> Optional[CatalogoEntidad]:
        """
        Obtiene un catálogo basado en los filtros dados.
        """
        documento = Catalogos.find_one(filtros or {})
        if not documento:
            return None
        identificador: str = str(documento["_id"])
        del documento["_id"]
        documento["id"] = identificador
        return CatalogoEntidad(**documento)
