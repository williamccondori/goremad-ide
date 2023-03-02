from typing import Optional

from bson import ObjectId
from pymongo.results import InsertOneResult, UpdateResult
from starlette import status

from app.dominio.entidades.programacion_entidad import ProgramacionEntidad
from app.dominio.excepciones.aplicacion_exception import AplicacionException
from app.dominio.repositorios.programacion_repositorio import IProgramacionRepositorio
from app.infraestructura.mongo_db.contextos.geogoremad_contexto import Programaciones


class ProgramacionRepositorio(IProgramacionRepositorio):
    """
    Repositorio de programacion de tareas.
    """

    async def contar(self, filtros: Optional[dict] = None) -> int:
        return Programaciones.count_documents(filtros or {})

    async def obtener_todos(self, filtros: Optional[dict] = None) -> list[ProgramacionEntidad]:
        documentos = Programaciones.find(filtros or {})
        respuesta = []
        for documento in documentos:
            identificador: str = str(documento["_id"])
            del documento["_id"]
            documento["id"] = identificador
            respuesta.append(ProgramacionEntidad(**documento))
        return respuesta

    async def obtener_por_id(self, programacion_id: str) -> ProgramacionEntidad:
        documento = Programaciones.find_one({"_id": ObjectId(programacion_id)})
        if not documento:
            raise AplicacionException("No se encontró la programación", status.HTTP_404_NOT_FOUND)
        identificador: str = str(documento["_id"])
        del documento["_id"]
        documento["id"] = identificador
        return ProgramacionEntidad(**documento)

    async def verificar_existencia(self, programacion_id: str) -> bool:
        numero_elementos: int = Programaciones.count_documents({"_id": ObjectId(programacion_id)})
        return numero_elementos > 0

    async def crear(self, programacion: ProgramacionEntidad) -> str:
        documento: dict = programacion.dict()
        del documento["id"]
        resultado: InsertOneResult = Programaciones.insert_one(documento)
        return str(resultado.inserted_id)

    async def actualizar(self, programacion_id: str, programacion: ProgramacionEntidad) -> str:
        documento: dict = programacion.dict()
        del documento["id"]
        resultado: UpdateResult = Programaciones.update_one({"_id": ObjectId(programacion_id)}, {"$set": documento})
        return str(programacion_id if resultado.modified_count > 0 else None)

    async def eliminar(self, programacion_id: str, usuario_auditoria_id: str) -> str:
        programacion: ProgramacionEntidad = await self.obtener_por_id(programacion_id)
        programacion.estado = False
        programacion.registrar_actualizacion(usuario_auditoria_id)
        return await self.actualizar(programacion_id, programacion)

    async def obtener_por_filtros(self, filtros: Optional[dict] = None) -> Optional[ProgramacionEntidad]:
        documento = Programaciones.find_one(filtros or {})
        if not documento:
            return None
        identificador: str = str(documento["_id"])
        del documento["_id"]
        documento["id"] = identificador
        return ProgramacionEntidad(**documento)

    async def verificar_existencia_por_filtros(self, filtros: Optional[dict] = None) -> bool:
        numero_elementos: int = Programaciones.count_documents(filtros or {})
        return numero_elementos > 0
