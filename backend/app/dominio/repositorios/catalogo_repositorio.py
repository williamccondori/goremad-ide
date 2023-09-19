from abc import abstractmethod  # noqa
from typing import Optional, List

from app.dominio.entidades.catalogo_entidad import (
    CatalogoEntidad,
)


class ICatalogoRepositorio:
    """
    Interfaz de repositorio de catálogos.
    """

    @abstractmethod
    async def contar(self, filtros: Optional[dict] = None) -> int:
        """
        Cuenta la cantidad de catálogos que cumplen con los filtros especificados.

        Args:
            filtros (Optional[dict], optional): Filtros para la consulta. Defaults to None.

        Returns:
            int: Cantidad de catálogos que cumplen con los filtros.
        """
        pass

    @abstractmethod
    async def obtener_todos(
        self, filtros: Optional[dict] = None
    ) -> List[CatalogoEntidad]:
        """
        Obtiene todos los catálogos que cumplen con los filtros especificados.

        Args:
            filtros (Optional[dict], optional): Filtros para la consulta. Defaults to None.

        Returns:
            List[CatalogoEntidad]: Lista de catálogos que cumplen con los filtros.
        """
        pass

    @abstractmethod
    async def obtener_por_id(self, catalogo_id: str) -> CatalogoEntidad:
        """
        Obtiene un catálogo por su identificador.

        Args:
            catalogo_id (str): Identificador del catálogo.

        Returns:
            CatalogoEntidad: Catálogo con el identificador especificado.
        """
        pass

    @abstractmethod
    async def verificar_existencia(self, catalogo_id: str) -> bool:
        """
        Verifica si existe un catálogo con el identificador especificado.

        Args:
            catalogo_id (str): Identificador del catálogo.

        Returns:
            bool: True si existe un catálogo con el identificador especificado, False en caso contrario.
        """
        pass

    @abstractmethod
    async def crear(self, catalogo: CatalogoEntidad) -> str:
        """
        Crea un catálogo.

        Args:
            catalogo (CatalogoEntidad): Catálogo a crear.

        Returns:
            str: Identificador del catálogo creado.
        """
        pass

    @abstractmethod
    async def actualizar(self, catalogo_id: str, catalogo: CatalogoEntidad) -> str:
        """
        Actualiza un catálogo.

        Args:
            catalogo_id (str): Identificador del catálogo a actualizar.
            catalogo (CatalogoEntidad): Catálogo con los datos actualizados.

        Returns:
            str: Identificador del catálogo actualizado.
        """
        pass

    @abstractmethod
    async def eliminar(self, catalogo_id: str) -> str:
        """
        Elimina un catálogo.

        Args:
            catalogo_id (str): Identificador del catálogo a eliminar.

        Returns:
            str: Identificador del catálogo eliminado.
        """
        pass
