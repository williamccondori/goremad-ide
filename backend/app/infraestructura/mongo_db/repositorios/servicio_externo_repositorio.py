from typing import Optional

from bson import ObjectId
from pymongo.results import InsertOneResult, UpdateResult
from starlette import status

from app.dominio.entidades.servicio_externo_entidad import ServicioExternoEntidad
from app.dominio.excepciones.aplicacion_exception import AplicacionException
from app.dominio.repositorios.servicio_externo_repositorio import IServicioExternoRepositorio
from app.infraestructura.mongo_db.contextos.geogoremad_contexto import ServiciosExternos


class ServicioExternoRepositorio(IServicioExternoRepositorio):
    """
    Repositorio de servicios externos.
    """

    async def contar(self, filtros: Optional[dict] = None) -> int:
        return ServiciosExternos.count_documents(filtros or {})

    async def obtener_todos(self, filtros: Optional[dict] = None) -> list[ServicioExternoEntidad]:
        documentos = ServiciosExternos.find(filtros or {})
        respuesta = []
        for documento in documentos:
            identificador: str = str(documento["_id"])
            del documento["_id"]
            documento["id"] = identificador
            respuesta.append(ServicioExternoEntidad(**documento))
        return respuesta

    async def obtener_por_id(self, servicio_externo_id: str) -> ServicioExternoEntidad:
        documento = ServiciosExternos.find_one({"_id": ObjectId(servicio_externo_id)})
        if not documento:
            raise AplicacionException("No se encontró el servicio externo", status.HTTP_404_NOT_FOUND)
        identificador: str = str(documento["_id"])
        del documento["_id"]
        documento["id"] = identificador
        return ServicioExternoEntidad(**documento)

    async def verificar_existencia(self, servicio_externo_id: str) -> bool:
        numero_elementos: int = ServiciosExternos.count_documents({"_id": ObjectId(servicio_externo_id)})
        return numero_elementos > 0

    async def crear(self, servicio_externo: ServicioExternoEntidad) -> str:
        documento: dict = servicio_externo.dict()
        del documento["id"]
        resultado: InsertOneResult = ServiciosExternos.insert_one(documento)
        return str(resultado.inserted_id)

    async def actualizar(self, servicio_externo_id: str, servicio_externo: ServicioExternoEntidad) -> str:
        documento: dict = servicio_externo.dict()
        del documento["id"]
        resultado: UpdateResult = ServiciosExternos.update_one({"_id": ObjectId(servicio_externo_id)},
                                                               {"$set": documento})
        return str(servicio_externo_id if resultado.modified_count > 0 else None)

    async def eliminar(self, servicio_externo_id: str, usuario_auditoria_id: str) -> str:
        servicio_externo: ServicioExternoEntidad = await self.obtener_por_id(servicio_externo_id)
        servicio_externo.estado = False
        servicio_externo.registrar_actualizacion(usuario_auditoria_id)
        return await self.actualizar(servicio_externo_id, servicio_externo)

    async def obtener_por_filtros(self, filtros: Optional[dict] = None) -> Optional[ServicioExternoEntidad]:
        documento = ServiciosExternos.find_one(filtros or {})
        if not documento:
            return None
        identificador: str = str(documento["_id"])
        del documento["_id"]
        documento["id"] = identificador
        return ServicioExternoEntidad(**documento)

    async def verificar_existencia_por_filtros(self, filtros: Optional[dict] = None) -> bool:
        numero_elementos: int = ServiciosExternos.count_documents(filtros or {})
        return numero_elementos > 0
