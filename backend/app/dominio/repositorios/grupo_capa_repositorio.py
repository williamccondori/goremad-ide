from abc import abstractmethod  # noqa
from typing import Optional

from app.dominio.entidades.grupo_capa_entidad import GrupoCapaEntidad


class IGrupoCapaRepositorio:
    """
    Interfaz de repositorio de grupos de capas.
    """

    @abstractmethod
    async def contar(self, filtros: Optional[dict] = None) -> int:
        """
        Cuenta la cantidad de grupos de capas que cumplen con los filtros.
        Args:
            filtros (Optional[dict], optional): Filtros para la consulta. Defaults to None.
        Returns:
            int: Cantidad de grupos de capas que cumplen con los filtros.
        """
        pass

    @abstractmethod
    async def obtener_todos(self, filtros: Optional[dict] = None) -> list[GrupoCapaEntidad]:
        """
        Obtiene todos los grupos de capas que cumplen con los filtros.
        Args:
            filtros (Optional[dict], optional): Filtros para la consulta. Defaults to None.
        Returns:
            list[GrupoCapaEntidad]: Lista de grupos de capas que cumplen con los filtros.
        """
        pass

    @abstractmethod
    async def obtener_por_id(self, grupo_capa_id: str) -> GrupoCapaEntidad:
        """
        Obtiene un grupo de capas por su identificador.
        Args:
            grupo_capa_id (str): Identificador del grupo de capas.
        Returns:
            GrupoCapaEntidad: Grupo de capas con el identificador especificado.
        """
        pass

    @abstractmethod
    async def verificar_existencia(self, grupo_capa_id: str) -> bool:
        """
        Verifica si existe un grupo de capas con el identificador especificado.
        Args:
            grupo_capa_id (str): Identificador del grupo de capas.
        Returns:
            bool: True si existe un grupo de capas con el identificador especificado, False en caso contrario.
        """
        pass

    @abstractmethod
    async def crear(self, grupo_capa: GrupoCapaEntidad) -> str:
        """
        Crea un grupo de capas.
        Args:
            grupo_capa (GrupoCapaEntidad): Grupo de capas a crear.
        Returns:
            str: Identificador del grupo de capas creado.
        """
        pass

    @abstractmethod
    async def actualizar(self, grupo_capa_id: str, grupo_capa: GrupoCapaEntidad) -> str:
        """
        Actualiza un grupo de capas.
        Args:
            grupo_capa_id (str): Identificador del grupo de capas a actualizar.
            grupo_capa (GrupoCapaEntidad): Grupo de capas con los datos actualizados.
        Returns:
            str: Identificador del grupo de capas actualizado.
        """
        pass

    @abstractmethod
    async def eliminar(self, grupo_capa_id: str, usuario_auditoria_id: str) -> str:
        """
        Elimina un grupo de capas.
        Args:
            grupo_capa_id (str): Identificador del grupo de capas a eliminar.
            usuario_auditoria_id (str): Identificador del usuario que realiza la eliminación.
        Returns:
            str: Identificador del grupo de capas eliminado.
        """
        pass

    @abstractmethod
    async def obtener_por_filtros(self, filtros: Optional[dict] = None) -> Optional[GrupoCapaEntidad]:
        """
        Obtiene un grupo de capas por los filtros especificados.
        Args:
            filtros (Optional[dict], optional): Filtros para la consulta. Defaults to None.
        Returns:
            Optional[GrupoCapaEntidad]: Grupo de capas que cumple con los filtros especificados.
        """
        pass

    @abstractmethod
    async def verificar_existencia_por_filtros(self, filtros: Optional[dict] = None) -> bool:
        """
        Verifica si existe un grupo de capas que cumpla con los filtros especificados.
        Args:
            filtros (Optional[dict], optional): Filtros para la consulta. Defaults to None.
        Returns:
            bool: True si existe un grupo de capas que cumpla con los filtros especificados, False en caso contrario.
        """
        pass
