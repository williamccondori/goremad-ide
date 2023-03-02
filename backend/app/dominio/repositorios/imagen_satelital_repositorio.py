from abc import abstractmethod  # noqa
from typing import Optional

from app.dominio.entidades.imagen_satelital_entidad import ImagenSatelitalEntidad


class IImagenSatelitalRepositorio:
    """
    Interfaz de repositorio de imagen satelital.
    """

    @abstractmethod
    async def contar(self, filtros: Optional[dict] = None) -> int:
        """
        Cuenta la cantidad de imagenes satelitales que cumplen con los filtros.
        Args:
            filtros (Optional[dict], optional): Filtros para la consulta. Defaults to None.
        Returns:
            int: Cantidad de imagenes satelitales que cumplen con los filtros.
        """
        pass

    @abstractmethod
    async def obtener_todos(self, filtros: Optional[dict] = None) -> list[ImagenSatelitalEntidad]:
        """
        Obtiene todas las imagenes satelitales que cumplen con los filtros.
        Args:
            filtros (Optional[dict], optional): Filtros para la consulta. Defaults to None.
        Returns:
            list[ImagenSatelitalEntidad]: Lista de imagenes satelitales que cumplen con los filtros.
        """
        pass

    @abstractmethod
    async def obtener_por_id(self, imagen_satelital_id: str) -> ImagenSatelitalEntidad:
        """
        Obtiene una imagen satelital por su identificador.
        Args:
            imagen_satelital_id (str): Identificador de la imagen satelital.
        Returns:
            ImagenSatelitalEntidad: Imagen satelital con el identificador especificado.
        """
        pass

    @abstractmethod
    async def verificar_existencia(self, imagen_satelital_id: str) -> bool:
        """
        Verifica si existe una imagen satelital con el identificador especificado.
        Args:
            imagen_satelital_id (str): Identificador de la imagen satelital.
        Returns:
            bool: True si existe una imagen satelital con el identificador especificado, False en caso contrario.
        """
        pass

    @abstractmethod
    async def crear(self, programacion: ImagenSatelitalEntidad) -> str:
        """
        Crea una imagen satelital.
        Args:
            programacion (ImagenSatelitalEntidad): Imagen satelital a crear.
        Returns:
            str: Identificador de la imagen satelital creada.
        """
        pass

    @abstractmethod
    async def actualizar(self, imagen_satelital_id: str, programacion: ImagenSatelitalEntidad) -> str:
        """
        Actualiza una imagen satelital.
        Args:
            imagen_satelital_id (str): Identificador de la imagen satelital a actualizar.
            programacion (ImagenSatelitalEntidad): Imagen satelital con los datos actualizados.
        Returns:
            str: Identificador de la imagen satelital actualizada.
        """
        pass

    @abstractmethod
    async def eliminar(self, imagen_satelital_id: str, usuario_auditoria_id: str) -> str:
        """
        Elimina una imagen satelital.
        Args:
            imagen_satelital_id (str): Identificador de la imagen satelital a eliminar.
            usuario_auditoria_id (str): Identificador del usuario que elimina la imagen satelital.
        Returns:
            str: Identificador de la imagen satelital eliminada.
        """
        pass

    @abstractmethod
    async def obtener_por_filtros(self, filtros: Optional[dict] = None) -> Optional[ImagenSatelitalEntidad]:
        """
        Obtiene una imagen satelital por los filtros especificados.
        Args:
            filtros (Optional[dict], optional): Filtros para la consulta. Defaults to None.
        Returns:
            Optional[ImagenSatelitalEntidad]: Imagen satelital que cumple con los filtros especificados.
        """
        pass

    @abstractmethod
    async def verificar_existencia_por_filtros(self, filtros: Optional[dict] = None) -> bool:
        """
        Verifica si existe una imagen satelital que cumpla con los filtros especificados.
        Args:
            filtros (Optional[dict], optional): Filtros para la consulta. Defaults to None.
        Returns:
            bool: True si existe una imagen satelital que cumpla con los filtros especificados, False en caso contrario.
        """
        pass
