from abc import abstractmethod  # noqa
from typing import Optional, List

from app.dominio.entidades.grupo_entidad import (
    GrupoEntidad,
)


class IGrupoRepositorio:
    """
    Interfaz del repositorio de grupos.
    """

    @abstractmethod
    async def contar(self, filtros: Optional[dict] = None) -> int:
        """
        Cuenta la cantidad de grupos que cumplen con los filtros especificados.

        Args:
            filtros (Optional[dict], optional): Filtros para la consulta. Defaults to None.

        Returns:
            int: Cantidad de grupos que cumplen con los filtros.
        """
        pass

    @abstractmethod
    async def obtener_todos(self, filtros: Optional[dict] = None) -> List[GrupoEntidad]:
        """
        Obtiene todos los grupos que cumplen con los filtros especificados.

        Args:
            filtros (Optional[dict], optional): Filtros para la consulta. Defaults to None.

        Returns:
            List[GrupoEntidad]: Lista de grupos que cumplen con los filtros.
        """
        pass

    @abstractmethod
    async def obtener_por_id(self, grupo_id: str) -> GrupoEntidad:
        """
        Obtiene un grupo por su identificador.

        Args:
            grupo_id (str): Identificador del grupo.

        Returns:
            GrupoEntidad: Grupo con el identificador especificado.
        """
        pass

    @abstractmethod
    async def verificar_existencia(self, grupo_id: str) -> bool:
        """
        Verifica si existe un grupo con el identificador especificado.

        Args:
            grupo_id (str): Identificador del grupo.

        Returns:
            bool: True si existe un grupo con el identificador especificado, False en caso contrario.
        """
        pass

    @abstractmethod
    async def crear(self, grupo: GrupoEntidad) -> str:
        """
        Crea un grupo.

        Args:
            grupo (GrupoEntidad): Grupo a crear.

        Returns:
            str: Identificador del grupo creado.
        """
        pass

    @abstractmethod
    async def actualizar(self, grupo_id: str, grupo: GrupoEntidad) -> str:
        """
        Actualiza un grupo.

        Args:
            grupo_id (str): Identificador del grupo a actualizar.
            grupo (GrupoEntidad): Grupo con los datos actualizados.

        Returns:
            str: Identificador del grupo actualizado.
        """
        pass

    @abstractmethod
    async def eliminar(self, grupo_id: str) -> str:
        """
        Elimina un grupo.

        Args:
            grupo_id (str): Identificador del grupo a eliminar.

        Returns:
            str: Identificador del grupo eliminado.
        """
        pass
