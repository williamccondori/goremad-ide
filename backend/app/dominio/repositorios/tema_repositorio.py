from abc import abstractmethod  # noqa
from typing import Optional

from app.dominio.entidades.tema_entidad import TemaEntidad


class ITemaRepositorio:
    """
    Interfaz del repositorio de temas.
    """

    @abstractmethod
    async def contar(self, filtros: Optional[dict] = None) -> int:
        """
        Cuenta la cantidad de temas que cumplen con los filtros especificados.

        Args:
            filtros (Optional[dict], optional): Filtros para la consulta. Defaults to None.

        Returns:
            int: Cantidad de temas que cumplen con los filtros.
        """
        pass

    @abstractmethod
    async def obtener_todos(self, filtros: Optional[dict] = None) -> list[TemaEntidad]:
        """
        Obtiene todos los temas que cumplen con los filtros especificados.

        Args:
            filtros (Optional[dict], optional): Filtros para la consulta. Defaults to None.

        Returns:
            list[TemaEntidad]: Lista de temas que cumplen con los filtros.
        """
        pass

    @abstractmethod
    async def obtener_por_id(self, tema_id: str) -> TemaEntidad:
        """
        Obtiene un tema por su identificador.

        Args:
            tema_id (str): Identificador del tema.

        Returns:
            TemaEntidad: Tema con el identificador especificado.
        """
        pass

    @abstractmethod
    async def verificar_existencia(self, tema_id: str) -> bool:
        """
        Verifica si existe un tema con el identificador especificado.

        Args:
            tema_id (str): Identificador del tema.

        Returns:
            bool: True si existe un tema con el identificador especificado, False en caso contrario.
        """
        pass

    @abstractmethod
    async def crear(self, tema: TemaEntidad) -> str:
        """
        Crea un tema.

        Args:
            tema (TemaEntidad): Tema a crear.

        Returns:
            str: Identificador del tema creado.
        """
        pass

    @abstractmethod
    async def actualizar(self, tema_id: str, tema: TemaEntidad) -> str:
        """
        Actualiza un tema.

        Args:
            tema_id (str): Identificador del tema a actualizar.
            tema (TemaEntidad): Tema con los datos actualizados.

        Returns:
            str: Identificador del tema actualizado.
        """
        pass

    @abstractmethod
    async def eliminar(self, tema_id: str, usuario_auditoria_id: str) -> str:
        """
        Elimina un tema.

        Args:
            tema_id (str): Identificador del tema a eliminar.
            usuario_auditoria_id (str): Identificador del usuario que realiza la eliminación.

        Returns:
            str: Identificador del tema eliminado.
        """
        pass

    @abstractmethod
    async def obtener_por_filtros(
        self, filtros: Optional[dict] = None
    ) -> Optional[TemaEntidad]:
        """
        Obtiene un tema por los filtros especificados.

        Args:
            filtros (Optional[dict], optional): Filtros para la consulta. Defaults to None.

        Returns:
            Optional[TemaEntidad]: Tema que cumple con los filtros especificados, None si no se encuentra ninguno.
        """
        pass

    @abstractmethod
    async def verificar_existencia_por_filtros(
        self, filtros: Optional[dict] = None
    ) -> bool:
        """
        Verifica si existe un tema que cumpla con los filtros especificados.

        Args:
            filtros (Optional[dict], optional): Filtros para la consulta. Defaults to None.

        Returns:
            bool: True si existe un tema que cumple con los filtros especificados, False en caso contrario.
        """
        pass
