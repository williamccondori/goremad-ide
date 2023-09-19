from typing import Optional

from bson import ObjectId
from pymongo.results import InsertOneResult, UpdateResult
from starlette import status

from app.dominio.entidades.capa_base_entidad import CapaBaseEntidad
from app.dominio.excepciones.aplicacion_exception import AplicacionException
from app.dominio.repositorios.capa_base_repositorio import ICapaBaseRepositorio
from app.infraestructura.mongo_db.contextos.geogoremad_contexto import CapasBase


class CapaBaseRepositorio(ICapaBaseRepositorio):
    """
    Repositorio de capas base.
    """

    async def contar(self, filtros: Optional[dict] = None) -> int:
        """
        Cuenta los documentos que cumplen con los filtros dados.
        """
        return CapasBase.count_documents(filtros or {})

    async def obtener_todos(
        self, filtros: Optional[dict] = None
    ) -> list[CapaBaseEntidad]:
        """
        Obtiene todos los documentos que cumplen con los filtros dados.
        """
        documentos = CapasBase.find(filtros or {})
        respuesta = []
        for documento in documentos:
            identificador: str = str(documento["_id"])
            del documento["_id"]
            documento["id"] = identificador
            respuesta.append(CapaBaseEntidad(**documento))
        return respuesta

    async def obtener_por_id(self, capa_base_id: str) -> CapaBaseEntidad:
        """
        Obtiene un documento por su identificador único.
        """
        documento = CapasBase.find_one({"_id": ObjectId(capa_base_id)})
        if not documento:
            raise AplicacionException(
                "No se encontró la capa base", status.HTTP_404_NOT_FOUND
            )
        identificador: str = str(documento["_id"])
        del documento["_id"]
        documento["id"] = identificador
        return CapaBaseEntidad(**documento)

    async def verificar_existencia(self, capa_base_id: str) -> bool:
        """
        Verifica si existe un documento con el identificador dado.
        """
        numero_elementos: int = CapasBase.count_documents(
            {"_id": ObjectId(capa_base_id)}
        )
        return numero_elementos > 0

    async def crear(self, capa_base: CapaBaseEntidad) -> str:
        """
        Crea un nuevo documento.
        """
        documento: dict = capa_base.dict()
        del documento["id"]
        resultado: InsertOneResult = CapasBase.insert_one(documento)
        return str(resultado.inserted_id)

    async def actualizar(self, capa_base_id: str, capa_base: CapaBaseEntidad) -> str:
        """
        Actualiza un documento existente por su identificador único.
        """
        documento: dict = capa_base.dict()
        del documento["id"]
        resultado: UpdateResult = CapasBase.update_one(
            {"_id": ObjectId(capa_base_id)}, {"$set": documento}
        )
        return str(capa_base_id if resultado.modified_count > 0 else None)

    async def eliminar(self, capa_base_id: str, usuario_auditoria_id: str) -> str:
        """
        Elimina un documento (cambia su estado a 'False').
        """
        capa_base: CapaBaseEntidad = await self.obtener_por_id(capa_base_id)
        capa_base.estado = False
        capa_base.registrar_actualizacion(usuario_auditoria_id)
        return await self.actualizar(capa_base_id, capa_base)

    async def obtener_por_filtros(
        self, filtros: Optional[dict] = None
    ) -> Optional[CapaBaseEntidad]:
        """
        Obtiene un documento basado en los filtros dados.
        """
        documento = CapasBase.find_one(filtros or {})
        if not documento:
            return None
        identificador: str = str(documento["_id"])
        del documento["_id"]
        documento["id"] = identificador
        return CapaBaseEntidad(**documento)

    async def verificar_existencia_por_filtros(
        self, filtros: Optional[dict] = None
    ) -> bool:
        """
        Verifica si existe un documento que cumple con los filtros dados.
        """
        numero_elementos: int = CapasBase.count_documents(filtros or {})
        return numero_elementos > 0
