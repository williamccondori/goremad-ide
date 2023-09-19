from abc import abstractmethod  # noqa
from typing import Optional, List

from app.dominio.entidades.objeto_geografico_entidad import (
    ObjetoGeograficoEntidad,
)


class IObjetoGeograficoRepositorio:
    """
    Interfaz de repositorio de objetos geográficos.
    """

    @abstractmethod
    async def contar(self, filtros: Optional[dict] = None) -> int:
        """
        Cuenta la cantidad de objetos geográficos que cumplen con los filtros especificados.

        Args:
            filtros (Optional[dict], optional): Filtros para la consulta. Defaults to None.

        Returns:
            int: Cantidad de objetos geográficos que cumplen con los filtros.
        """
        pass

    @abstractmethod
    async def obtener_todos(
        self, filtros: Optional[dict] = None
    ) -> List[ObjetoGeograficoEntidad]:
        """
        Obtiene todos los objetos geográficos que cumplen con los filtros especificados.

        Args:
            filtros (Optional[dict], optional): Filtros para la consulta. Defaults to None.

        Returns:
            List[ObjetoGeograficoEntidad]: Lista de objetos geográficos que cumplen con los filtros.
        """
        pass

    @abstractmethod
    async def obtener_por_id(
        self, objeto_geografico_id: str
    ) -> ObjetoGeograficoEntidad:
        """
        Obtiene un objeto geográfico por su identificador.

        Args:
            objeto_geografico_id (str): Identificador del objeto geográfico.

        Returns:
            ObjetoGeograficoEntidad: Objeto geográfico con el identificador especificado.
        """
        pass

    @abstractmethod
    async def verificar_existencia(self, objeto_geografico_id: str) -> bool:
        """
        Verifica si existe un objeto geográfico con el identificador especificado.

        Args:
            objeto_geografico_id (str): Identificador del objeto geográfico.

        Returns:
            bool: True si existe un objeto geográfico con el identificador especificado, False en caso contrario.
        """
        pass

    @abstractmethod
    async def crear(self, objeto_geografico: ObjetoGeograficoEntidad) -> str:
        """
        Crea un objeto geográfico.

        Args:
            objeto_geografico (ObjetoGeograficoEntidad): Objeto geográfico a crear.

        Returns:
            str: Identificador del objeto geográfico creado.
        """
        pass

    @abstractmethod
    async def actualizar(
        self, objeto_geografico_id: str, objeto_geografico: ObjetoGeograficoEntidad
    ) -> str:
        """
        Actualiza un objeto geográfico.

        Args:
            objeto_geografico_id (str): Identificador del objeto geográfico a actualizar.
            objeto_geografico (ObjetoGeograficoEntidad): Objeto geográfico con los datos actualizados.

        Returns:
            str: Identificador del objeto geográfico actualizado.
        """
        pass

    @abstractmethod
    async def eliminar(self, objeto_geografico_id: str) -> str:
        """
        Elimina un objeto geográfico.

        Args:
            objeto_geografico_id (str): Identificador del objeto geográfico a eliminar.

        Returns:
            str: Identificador del objeto geográfico eliminado.
        """
        pass
