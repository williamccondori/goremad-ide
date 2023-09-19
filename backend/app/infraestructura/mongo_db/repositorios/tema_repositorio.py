from typing import Optional

from bson import ObjectId
from pymongo.results import InsertOneResult, UpdateResult
from starlette import status

from app.dominio.entidades.tema_entidad import (
    TemaEntidad,
)
from app.dominio.excepciones.aplicacion_exception import AplicacionException
from app.dominio.repositorios.tema_repositorio import (
    ITemaRepositorio,
)
from app.infraestructura.mongo_db.contextos.geogoremad_contexto import (
    Temas,
)


class TemaRepositorio(ITemaRepositorio):
    """
    Repositorio de temas.
    """

    async def contar(self, filtros: Optional[dict] = None) -> int:
        """
        Cuenta los temas que cumplen con los filtros dados.
        """
        return Temas.count_documents(filtros or {})

    async def obtener_todos(self, filtros: Optional[dict] = None) -> list[TemaEntidad]:
        """
        Obtiene todos los temas que cumplen con los filtros dados.
        """
        documentos = Temas.find(filtros or {})
        respuesta = []
        for documento in documentos:
            identificador: str = str(documento["_id"])
            del documento["_id"]
            documento["id"] = identificador
            respuesta.append(TemaEntidad(**documento))
        return respuesta

    async def obtener_por_id(self, tema_id: str) -> TemaEntidad:
        """
        Obtiene un tema por su identificador único.
        """
        documento = Temas.find_one({"_id": ObjectId(tema_id)})
        if not documento:
            raise AplicacionException(
                "No se encontró el tema", status.HTTP_404_NOT_FOUND
            )
        identificador: str = str(documento["_id"])
        del documento["_id"]
        documento["id"] = identificador
        return TemaEntidad(**documento)

    async def crear(self, tema: TemaEntidad) -> str:
        """
        Crea un nuevo tema.
        """
        documento: dict = tema.dict()
        del documento["id"]
        resultado: InsertOneResult = Temas.insert_one(documento)
        return str(resultado.inserted_id)

    async def actualizar(self, tema_id: str, tema: TemaEntidad) -> str:
        """
        Actualiza un tema existente por su identificador único.
        """
        documento: dict = tema.dict()
        del documento["id"]
        resultado: UpdateResult = Temas.update_one(
            {"_id": ObjectId(tema_id)}, {"$set": documento}
        )
        return str(tema_id if resultado.modified_count > 0 else None)

    async def eliminar(self, tema_id: str, usuario_auditoria_id: str) -> str:
        """
        Elimina un tema (cambia su estado a 'False').
        """
        tema: TemaEntidad = await self.obtener_por_id(tema_id)
        tema.estado = False
        tema.registrar_actualizacion(usuario_auditoria_id)
        return await self.actualizar(tema_id, tema)

    async def obtener_por_filtros(
        self, filtros: Optional[dict] = None
    ) -> Optional[TemaEntidad]:
        """
        Obtiene un tema basado en los filtros dados.
        """
        documento = Temas.find_one(filtros or {})
        if not documento:
            return None
        identificador: str = str(documento["_id"])
        del documento["_id"]
        documento["id"] = identificador
        return TemaEntidad(**documento)
