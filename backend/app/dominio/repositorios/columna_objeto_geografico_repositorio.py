from abc import abstractmethod  # noqa
from typing import Optional, List

from app.dominio.entidades.columna_objeto_geografico_entidad import (
    ColumnaObjetoGeograficoEntidad,
)


class IColumnaObjetoGeograficoRepositorio:
    """
    Interfaz de repositorio de columnas de objetos geográficos.
    """

    @abstractmethod
    async def contar(self, filtros: Optional[dict] = None) -> int:
        """
        Cuenta la cantidad de columnas de objetos geográficos que cumplen con los filtros especificados.

        Args:
            filtros (Optional[dict], optional): Filtros para la consulta. Defaults to None.

        Returns:
            int: Cantidad de columnas de objetos geográficos que cumplen con los filtros.
        """
        pass

    @abstractmethod
    async def obtener_todos(
        self, filtros: Optional[dict] = None
    ) -> List[ColumnaObjetoGeograficoEntidad]:
        """
        Obtiene todos las columnas de objetos geográficos que cumplen con los filtros especificados.

        Args:
            filtros (Optional[dict], optional): Filtros para la consulta. Defaults to None.

        Returns:
            List[ColumnaObjetoGeograficoEntidad]: Lista de columnas de objetos geográficos que cumplen con los filtros.
        """
        pass

    @abstractmethod
    async def obtener_por_id(
        self, columna_objeto_geografico_id: str
    ) -> ColumnaObjetoGeograficoEntidad:
        """
        Obtiene una columna de objeto geográfico por su identificador.

        Args:
            columna_objeto_geografico_id (str): Identificador de la columna de objeto geográfico.

        Returns:
            ColumnaObjetoGeograficoEntidad: Columna de objeto geográfico con el identificador especificado.
        """
        pass

    @abstractmethod
    async def verificar_existencia(self, columna_objeto_geografico_id: str) -> bool:
        """
        Verifica si existe una columna de objeto geográfico con el identificador especificado.

        Args:
            columna_objeto_geografico_id (str): Identificador de la columna de objeto geográfico.

        Returns:
            bool: True si existe una columna de objeto geográfico con el identificador especificado, False en caso contrario.
        """
        pass

    @abstractmethod
    async def crear(
        self, columna_objeto_geografico: ColumnaObjetoGeograficoEntidad
    ) -> str:
        """
        Crea una columna de objeto geográfico.

        Args:
            columna_objeto_geografico (ColumnaObjetoGeograficoEntidad): Columna de objeto geográfico a crear.

        Returns:
            str: Identificador de la columna de objeto geográfico creado.
        """
        pass

    @abstractmethod
    async def actualizar(
        self,
        columna_objeto_geografico_id: str,
        columna_objeto_geografico: ColumnaObjetoGeograficoEntidad,
    ) -> str:
        """
        Actualiza una columna de objeto geográfico.

        Args:
            columna_objeto_geografico_id (str): Identificador de la columna de objeto geográfico a actualizar.
            columna_objeto_geografico (ColumnaObjetoGeograficoEntidad): Columna de objeto geográfico con los datos actualizados.

        Returns:
            str: Identificador de la columna de objeto geográfico actualizado.
        """
        pass

    @abstractmethod
    async def eliminar(self, columna_objeto_geografico_id: str) -> str:
        """
        Elimina una columna de objeto geográfico.

        Args:
            columna_objeto_geografico_id (str): Identificador de la columna de objeto geográfico a eliminar.

        Returns:
            str: Identificador de la columna de objeto geográfico eliminado.
        """
        pass
