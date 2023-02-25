from abc import abstractmethod  # noqa
from typing import Optional

from app.dominio.entidades.capa_base_entidad import CapaBaseEntidad


class ICapaBaseRepositorio:
    """
    Interfaz de repositorio de capas base.
    """

    @abstractmethod
    async def contar(self, filtros: Optional[dict] = None) -> int:
        """
        Cuenta la cantidad de capas base que cumplen con los filtros.
        Args:
            filtros (Optional[dict], optional): Filtros para la consulta. Defaults to None.
        Returns:
            int: Cantidad de capas base que cumplen con los filtros.
        """
        pass

    @abstractmethod
    async def obtener_todos(self, filtros: Optional[dict] = None) -> list[CapaBaseEntidad]:
        """
        Obtiene todas las capas base que cumplen con los filtros.
        Args:
            filtros (Optional[dict], optional): Filtros para la consulta. Defaults to None.
        Returns:
            list[CapaBaseEntidad]: Lista de capas base que cumplen con los filtros.
        """
        pass

    @abstractmethod
    async def obtener_por_id(self, capa_base_id: str) -> CapaBaseEntidad:
        """
        Obtiene una capa base por su identificador.
        Args:
            capa_base_id (str): Identificador de la capa base.
        Returns:
            CapaBaseEntidad: Capa base con el identificador especificado.
        """
        pass

    @abstractmethod
    async def verificar_existencia(self, capa_base_id: str) -> bool:
        """
        Verifica si existe una capa base con el identificador especificado.
        Args:
            capa_base_id (str): Identificador de la capa base.
        Returns:
            bool: True si existe una capa base con el identificador especificado, False en caso contrario.
        """
        pass

    @abstractmethod
    async def crear(self, capa_base: CapaBaseEntidad) -> str:
        """
        Crea una capa base.
        Args:
            capa_base (CapaBaseEntidad): Capa base a crear.
        Returns:
            str: Identificador de la capa base creada.
        """
        pass

    @abstractmethod
    async def actualizar(self, capa_base_id: str, capa_base: CapaBaseEntidad) -> str:
        """
        Actualiza una capa base.
        Args:
            capa_base_id (str): Identificador de la capa base a actualizar.
            capa_base (CapaBaseEntidad): Capa base con los datos actualizados.
        Returns:
            str: Identificador de la capa base actualizada.
        """
        pass

    @abstractmethod
    async def eliminar(self, capa_base_id: str, usuario_auditoria_id: str) -> str:
        """
        Elimina una capa base.
        Args:
            capa_base_id (str): Identificador de la capa base a eliminar.
            usuario_auditoria_id (str): Identificador del usuario que realiza la eliminación.
        Returns:
            str: Identificador de la capa base eliminada.
        """
        pass

    @abstractmethod
    async def obtener_por_filtros(self, filtros: Optional[dict] = None) -> Optional[CapaBaseEntidad]:
        """
        Obtiene una capa base por los filtros especificados.
        Args:
            filtros (Optional[dict], optional): Filtros para la consulta. Defaults to None.
        Returns:
            Optional[CapaBaseEntidad]: Capa base que cumple con los filtros especificados.
        """
        pass

    @abstractmethod
    async def verificar_existencia_por_filtros(self, filtros: Optional[dict] = None) -> bool:
        """
        Verifica si existe una capa base que cumple con los filtros especificados.
        Args:
            filtros (Optional[dict], optional): Filtros para la consulta. Defaults to None.
        Returns:
            bool: True si existe una capa base que cumple con los filtros especificados, False en caso contrario.
        """
        pass
