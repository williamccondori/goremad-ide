from typing import Optional

from bson import ObjectId
from pymongo.results import InsertOneResult, UpdateResult
from starlette import status

from app.dominio.entidades.columna_objeto_geografico_entidad import (
    ColumnaObjetoGeograficoEntidad,
)  # Asume que existe
from app.dominio.excepciones.aplicacion_exception import AplicacionException
from app.dominio.repositorios.columna_objeto_geografico_repositorio import (
    IColumnaObjetoGeograficoRepositorio,
)  # Asume que existe
from app.infraestructura.mongo_db.contextos.geogoremad_contexto import (
    ColumnasObjetoGeografico,
)  # Asume que existe


class ColumnaObjetoGeograficoRepositorio(IColumnaObjetoGeograficoRepositorio):
    """
    Repositorio de columnas de objetos geográficos.
    """

    async def contar(self, filtros: Optional[dict] = None) -> int:
        return ColumnasObjetoGeografico.count_documents(filtros or {})

    async def obtener_todos(
        self, filtros: Optional[dict] = None
    ) -> list[ColumnaObjetoGeograficoEntidad]:
        documentos = ColumnasObjetoGeografico.find(filtros or {})
        respuesta = []
        for documento in documentos:
            identificador: str = str(documento["_id"])
            del documento["_id"]
            documento["id"] = identificador
            respuesta.append(ColumnaObjetoGeograficoEntidad(**documento))
        return respuesta

    async def obtener_por_id(
        self, columna_objeto_geografico_id: str
    ) -> ColumnaObjetoGeograficoEntidad:
        documento = ColumnasObjetoGeografico.find_one(
            {"_id": ObjectId(columna_objeto_geografico_id)}
        )
        if not documento:
            raise AplicacionException(
                "No se encontró la columna de objeto geográfico",
                status.HTTP_404_NOT_FOUND,
            )
        identificador: str = str(documento["_id"])
        del documento["_id"]
        documento["id"] = identificador
        return ColumnaObjetoGeograficoEntidad(**documento)

    async def crear(
        self, columna_objeto_geografico: ColumnaObjetoGeograficoEntidad
    ) -> str:
        documento: dict = columna_objeto_geografico.dict()
        del documento["id"]
        resultado: InsertOneResult = ColumnasObjetoGeografico.insert_one(documento)
        return str(resultado.inserted_id)

    async def actualizar(
        self,
        columna_objeto_geografico_id: str,
        columna_objeto_geografico: ColumnaObjetoGeograficoEntidad,
    ) -> str:
        documento: dict = columna_objeto_geografico.dict()
        del documento["id"]
        resultado: UpdateResult = ColumnasObjetoGeografico.update_one(
            {"_id": ObjectId(columna_objeto_geografico_id)}, {"$set": documento}
        )
        return str(
            columna_objeto_geografico_id if resultado.modified_count > 0 else None
        )

    async def eliminar(
        self, columna_objeto_geografico_id: str, usuario_auditoria_id: str
    ) -> str:
        columna_objeto_geografico: ColumnaObjetoGeograficoEntidad = (
            await self.obtener_por_id(columna_objeto_geografico_id)
        )
        columna_objeto_geografico.estado = False
        columna_objeto_geografico.registrar_actualizacion(usuario_auditoria_id)
        return await self.actualizar(
            columna_objeto_geografico_id, columna_objeto_geografico
        )

    async def obtener_por_filtros(
        self, filtros: Optional[dict] = None
    ) -> Optional[ColumnaObjetoGeograficoEntidad]:
        documento = ColumnasObjetoGeografico.find_one(filtros or {})
        if not documento:
            return None
        identificador: str = str(documento["_id"])
        del documento["_id"]
        documento["id"] = identificador
        return ColumnaObjetoGeograficoEntidad(**documento)
