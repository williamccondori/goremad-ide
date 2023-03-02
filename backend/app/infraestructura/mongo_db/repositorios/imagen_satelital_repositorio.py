from typing import Optional

from bson import ObjectId
from pymongo.results import InsertOneResult, UpdateResult
from starlette import status

from app.dominio.entidades.imagen_satelital_entidad import ImagenSatelitalEntidad
from app.dominio.excepciones.aplicacion_exception import AplicacionException
from app.dominio.repositorios.imagen_satelital_repositorio import IImagenSatelitalRepositorio
from app.infraestructura.mongo_db.contextos.geogoremad_contexto import ImagenesSatelitales


class ImagenSatelitalRepositorio(IImagenSatelitalRepositorio):
    """
    Repositorio de imagenes satelitales.
    """

    async def contar(self, filtros: Optional[dict] = None) -> int:
        return ImagenesSatelitales.count_documents(filtros or {})

    async def obtener_todos(self, filtros: Optional[dict] = None) -> list[ImagenSatelitalEntidad]:
        documentos = ImagenesSatelitales.find(filtros or {})
        respuesta = []
        for documento in documentos:
            identificador: str = str(documento["_id"])
            del documento["_id"]
            documento["id"] = identificador
            respuesta.append(ImagenSatelitalEntidad(**documento))
        return respuesta

    async def obtener_por_id(self, imagen_satelital_id: str) -> ImagenSatelitalEntidad:
        documento = ImagenesSatelitales.find_one({"_id": ObjectId(imagen_satelital_id)})
        if not documento:
            raise AplicacionException("No se encontró la programación", status.HTTP_404_NOT_FOUND)
        identificador: str = str(documento["_id"])
        del documento["_id"]
        documento["id"] = identificador
        return ImagenSatelitalEntidad(**documento)

    async def verificar_existencia(self, imagen_satelital_id: str) -> bool:
        numero_elementos: int = ImagenesSatelitales.count_documents({"_id": ObjectId(imagen_satelital_id)})
        return numero_elementos > 0

    async def crear(self, imagen_satelital: ImagenSatelitalEntidad) -> str:
        documento: dict = imagen_satelital.dict()
        del documento["id"]
        resultado: InsertOneResult = ImagenesSatelitales.insert_one(documento)
        return str(resultado.inserted_id)

    async def actualizar(self, imagen_satelital_id: str, imagen_satelital: ImagenSatelitalEntidad) -> str:
        documento: dict = imagen_satelital.dict()
        del documento["id"]
        resultado: UpdateResult = ImagenesSatelitales.update_one({"_id": ObjectId(imagen_satelital_id)},
                                                                 {"$set": documento})
        return str(imagen_satelital_id if resultado.modified_count > 0 else None)

    async def eliminar(self, imagen_satelital_id: str, usuario_auditoria_id: str) -> str:
        imagen_satelital: ImagenSatelitalEntidad = await self.obtener_por_id(imagen_satelital_id)
        imagen_satelital.estado = False
        imagen_satelital.registrar_actualizacion(usuario_auditoria_id)
        return await self.actualizar(imagen_satelital_id, imagen_satelital)

    async def obtener_por_filtros(self, filtros: Optional[dict] = None) -> Optional[ImagenSatelitalEntidad]:
        documento = ImagenesSatelitales.find_one(filtros or {})
        if not documento:
            return None
        identificador: str = str(documento["_id"])
        del documento["_id"]
        documento["id"] = identificador
        return ImagenSatelitalEntidad(**documento)

    async def verificar_existencia_por_filtros(self, filtros: Optional[dict] = None) -> bool:
        numero_elementos: int = ImagenesSatelitales.count_documents(filtros or {})
        return numero_elementos > 0
