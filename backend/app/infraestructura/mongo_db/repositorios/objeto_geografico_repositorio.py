from typing import Optional

from bson import ObjectId
from pymongo.results import InsertOneResult, UpdateResult
from starlette import status

from app.dominio.entidades.objeto_geografico_entidad import (
    ObjetoGeograficoEntidad,
)
from app.dominio.excepciones.aplicacion_exception import AplicacionException
from app.dominio.repositorios.objeto_geografico_repositorio import (
    IObjetoGeograficoRepositorio,
)
from app.infraestructura.mongo_db.contextos.geogoremad_contexto import (
    ObjetosGeograficos,
)


class ObjetoGeograficoRepositorio(IObjetoGeograficoRepositorio):
    """
    Repositorio de objetos geográficos.
    """

    async def contar(self, filtros: Optional[dict] = None) -> int:
        return ObjetosGeograficos.count_documents(filtros or {})

    async def obtener_todos(
        self, filtros: Optional[dict] = None
    ) -> list[ObjetoGeograficoEntidad]:
        documentos = ObjetosGeograficos.find(filtros or {})
        respuesta = []
        for documento in documentos:
            identificador: str = str(documento["_id"])
            del documento["_id"]
            documento["id"] = identificador
            respuesta.append(ObjetoGeograficoEntidad(**documento))
        return respuesta

    async def obtener_por_id(
        self, objeto_geografico_id: str
    ) -> ObjetoGeograficoEntidad:
        documento = ObjetosGeograficos.find_one({"_id": ObjectId(objeto_geografico_id)})
        if not documento:
            raise AplicacionException(
                "No se encontró el objeto geográfico", status.HTTP_404_NOT_FOUND
            )
        identificador: str = str(documento["_id"])
        del documento["_id"]
        documento["id"] = identificador
        return ObjetoGeograficoEntidad(**documento)

    async def crear(self, objeto_geografico: ObjetoGeograficoEntidad) -> str:
        documento: dict = objeto_geografico.dict()
        del documento["id"]
        resultado: InsertOneResult = ObjetosGeograficos.insert_one(documento)
        return str(resultado.inserted_id)

    async def actualizar(
        self, objeto_geografico_id: str, objeto_geografico: ObjetoGeograficoEntidad
    ) -> str:
        documento: dict = objeto_geografico.dict()
        del documento["id"]
        resultado: UpdateResult = ObjetosGeograficos.update_one(
            {"_id": ObjectId(objeto_geografico_id)}, {"$set": documento}
        )
        return str(objeto_geografico_id if resultado.modified_count > 0 else None)

    async def eliminar(
        self, objeto_geografico_id: str, usuario_auditoria_id: str
    ) -> str:
        objeto_geografico: ObjetoGeograficoEntidad = await self.obtener_por_id(
            objeto_geografico_id
        )
        objeto_geografico.estado = False
        objeto_geografico.registrar_actualizacion(usuario_auditoria_id)
        return await self.actualizar(objeto_geografico_id, objeto_geografico)

    async def obtener_por_filtros(
        self, filtros: Optional[dict] = None
    ) -> Optional[ObjetoGeograficoEntidad]:
        documento = ObjetosGeograficos.find_one(filtros or {})
        if not documento:
            return None
        identificador: str = str(documento["_id"])
        del documento["_id"]
        documento["id"] = identificador
        return ObjetoGeograficoEntidad(**documento)
