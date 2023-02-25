from abc import abstractmethod  # noqa
from typing import Optional

from app.dominio.entidades.publicacion_entidad import PublicacionEntidad


class IPublicacionRepositorio:
    """
    Interfaz de repositorio de publicaciones.
    """

    @abstractmethod
    async def contar(self, filtros: Optional[dict] = None) -> int:
        """
        Cuenta la cantidad de publicaciones que cumplen con los filtros.
        Args:
            filtros (Optional[dict], optional): Filtros para la consulta. Defaults to None.
        Returns:
            int: Cantidad de publicaciones que cumplen con los filtros.
        """
        pass

    @abstractmethod
    async def obtener_todos(self, filtros: Optional[dict] = None) -> list[PublicacionEntidad]:
        """
        Obtiene todas las publicaciones que cumplen con los filtros.
        Args:
            filtros (Optional[dict], optional): Filtros para la consulta. Defaults to None.
        Returns:
            list[PublicacionEntidad]: Lista de publicaciones que cumplen con los filtros.
        """
        pass

    @abstractmethod
    async def obtener_por_id(self, publicacion_id: str) -> PublicacionEntidad:
        """
        Obtiene una publicacion por su identificador.
        Args:
            publicacion_id (str): Identificador de la publicacion.
        Returns:
            PublicacionEntidad: Publicación con el identificador especificado.
        """
        pass

    @abstractmethod
    async def verificar_existencia(self, publicacion_id: str) -> bool:
        """
        Verifica si existe una publicacion con el identificador especificado.
        Args:
            publicacion_id (str): Identificador de la publicacion.
        Returns:
            bool: True si existe una publicacion con el identificador especificado, False en caso contrario.
        """
        pass

    @abstractmethod
    async def crear(self, publicacion: PublicacionEntidad) -> str:
        """
        Crea una publicacion.
        Args:
            publicacion (PublicacionEntidad): Publicacion a crear.
        Returns:
            str: Identificador de la publicacion creada.
        """
        pass

    @abstractmethod
    async def actualizar(self, publicacion_id: str, publicacion: PublicacionEntidad) -> str:
        """
        Actualiza una publicacion.
        Args:
            publicacion_id (str): Identificador de la publicacion.
            publicacion (PublicacionEntidad): Publicacion a actualizar.
        Returns:
            str: Identificador de la publicacion actualizada.
        """
        pass

    @abstractmethod
    async def eliminar(self, publicacion_id: str, usuario_auditoria_id: str) -> str:
        """
        Elimina una publicacion.
        Args:
            publicacion_id (str): Identificador de la publicacion.
            usuario_auditoria_id (str): Identificador del usuario que realiza la eliminación.
        Returns:
            str: Identificador de la publicacion eliminada.
        """
        pass

    @abstractmethod
    async def obtener_por_filtros(self, filtros: Optional[dict] = None) -> Optional[PublicacionEntidad]:
        """
        Obtiene una publicacion por los filtros especificados.
        Args:
            filtros (Optional[dict], optional): Filtros para la consulta. Defaults to None.
        Returns:
            Optional[PublicacionEntidad]: Publicacion que cumple con los filtros especificados.
        """
        pass

    @abstractmethod
    async def verificar_existencia_por_filtros(self, filtros: Optional[dict] = None) -> bool:
        """
        Verifica si existe una publicacion que cumpla con los filtros especificados.
        Args:
            filtros (Optional[dict], optional): Filtros para la consulta. Defaults to None.
        Returns:
            bool: True si existe una publicacion que cumpla con los filtros especificados, False en caso contrario.
        """
        pass
