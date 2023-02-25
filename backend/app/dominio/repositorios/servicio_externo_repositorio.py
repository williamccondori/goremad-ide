from abc import abstractmethod  # noqa
from typing import Optional

from app.dominio.entidades.servicio_externo_entidad import ServicioExternoEntidad


class IServicioExternoRepositorio:
    """
    Interfaz de repositorio de servicios externos.
    """

    @abstractmethod
    async def contar(self, filtros: Optional[dict] = None) -> int:
        """
        Cuenta la cantidad de servicios externos que cumplen con los filtros.
        Args:
            filtros (Optional[dict], optional): Filtros para la consulta. Defaults to None.
        Returns:
            int: Cantidad de servicios externos que cumplen con los filtros.
        """
        pass

    @abstractmethod
    async def obtener_todos(self, filtros: Optional[dict] = None) -> list[ServicioExternoEntidad]:
        """
        Obtiene todos los servicios externos que cumplen con los filtros.
        Args:
            filtros (Optional[dict], optional): Filtros para la consulta. Defaults to None.
        Returns:
            list[ServicioExternoEntidad]: Lista de servicios externos que cumplen con los filtros.
        """
        pass

    @abstractmethod
    async def obtener_por_id(self, servicio_externo_id: str) -> ServicioExternoEntidad:
        """
        Obtiene un servicio externo por su identificador.
        Args:
            servicio_externo_id (str): Identificador del servicio externo.
        Returns:
            ServicioExternoEntidad: Servicio externo con el identificador especificado.
        """
        pass

    @abstractmethod
    async def verificar_existencia(self, servicio_externo_id: str) -> bool:
        """
        Verifica si existe un servicio externo con el identificador especificado.
        Args:
            servicio_externo_id (str): Identificador del servicio externo.
        Returns:
            bool: True si existe un servicio externo con el identificador especificado, False en caso contrario.
        """
        pass

    @abstractmethod
    async def crear(self, servicio_externo: ServicioExternoEntidad) -> str:
        """
        Crea un servicio externo.
        Args:
            servicio_externo (ServicioExternoEntidad): Servicio externo a crear.
        Returns:
            str: Identificador del servicio externo creado.
        """
        pass

    @abstractmethod
    async def actualizar(self, servicio_externo_id: str, servicio_externo: ServicioExternoEntidad) -> str:
        """
        Actualiza un servicio externo.
        Args:
            servicio_externo_id (str): Identificador del servicio externo a actualizar.
            servicio_externo (ServicioExternoEntidad): Servicio externo con los datos actualizados.
        Returns:
            str: Identificador del servicio externo actualizado.
        """
        pass

    @abstractmethod
    async def eliminar(self, servicio_externo_id: str, usuario_auditoria_id: str) -> str:
        """
        Elimina un servicio externo.
        Args:
            servicio_externo_id (str): Identificador del servicio externo a eliminar.
            usuario_auditoria_id (str): Identificador del usuario que realiza la eliminación.
        Returns:
            str: Identificador del servicio externo eliminado.
        """
        pass

    @abstractmethod
    async def obtener_por_filtros(self, filtros: Optional[dict] = None) -> Optional[ServicioExternoEntidad]:
        """
        Obtiene un servicio externo por los filtros especificados.
        Args:
            filtros (Optional[dict], optional): Filtros para la consulta. Defaults to None.
        Returns:
            Optional[ServicioExternoEntidad]: Servicio externo que cumple con los filtros especificados.
        """
        pass

    @abstractmethod
    async def verificar_existencia_por_filtros(self, filtros: Optional[dict] = None) -> bool:
        """
        Verifica si existe un servicio externo que cumpla con los filtros especificados.
        Args:
            filtros (Optional[dict], optional): Filtros para la consulta. Defaults to None.
        Returns:
            bool: True si existe un servicio externo que cumpla con los filtros especificados, False en caso contrario.
        """
        pass
