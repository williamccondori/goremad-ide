from abc import abstractmethod  # noqa
from typing import Optional

from app.dominio.entidades.programacion_entidad import ProgramacionEntidad


class IProgramacionRepositorio:
    """
    Interfaz de repositorio de la programacion de una tarea.
    """

    @abstractmethod
    async def contar(self, filtros: Optional[dict] = None) -> int:
        """
        Cuenta la cantidad de programaciones que cumplen con los filtros.
        Args:
            filtros (Optional[dict], optional): Filtros para la consulta. Defaults to None.
        Returns:
            int: Cantidad de programaciones que cumplen con los filtros.
        """
        pass

    @abstractmethod
    async def obtener_todos(self, filtros: Optional[dict] = None) -> list[ProgramacionEntidad]:
        """
        Obtiene todas las programaciones que cumplen con los filtros.
        Args:
            filtros (Optional[dict], optional): Filtros para la consulta. Defaults to None.
        Returns:
            list[ProgramacionEntidad]: Lista de programaciones que cumplen con los filtros.
        """
        pass

    @abstractmethod
    async def obtener_por_id(self, programacion_id: str) -> ProgramacionEntidad:
        """
        Obtiene una programacion por su identificador.
        Args:
            programacion_id (str): Identificador de la programacion.
        Returns:
            ProgramacionEntidad: Programacion con el identificador especificado.
        """
        pass

    @abstractmethod
    async def verificar_existencia(self, programacion_id: str) -> bool:
        """
        Verifica si existe una programacion con el identificador especificado.
        Args:
            programacion_id (str): Identificador de la programacion.
        Returns:
            bool: True si existe una programacion con el identificador especificado, False en caso contrario.
        """
        pass

    @abstractmethod
    async def crear(self, programacion: ProgramacionEntidad) -> str:
        """
        Crea una programacion.
        Args:
            programacion (ProgramacionEntidad): Programacion a crear.
        Returns:
            str: Identificador de la programacion creada.
        """
        pass

    @abstractmethod
    async def actualizar(self, programacion_id: str, programacion: ProgramacionEntidad) -> str:
        """
        Actualiza una programacion.
        Args:
            programacion_id (str): Identificador de la programacion a actualizar.
            programacion (ProgramacionEntidad): Programacion con los datos actualizados.
        Returns:
            str: Identificador de la programacion actualizada.
        """
        pass

    @abstractmethod
    async def eliminar(self, programacion_id: str, usuario_auditoria_id: str) -> str:
        """
        Elimina una programacion.
        Args:
            programacion_id (str): Identificador de la programacion a eliminar.
            usuario_auditoria_id (str): Identificador del usuario que realiza la eliminación.
        Returns:
            str: Identificador de la programacion eliminada.
        """
        pass

    @abstractmethod
    async def obtener_por_filtros(self, filtros: Optional[dict] = None) -> Optional[ProgramacionEntidad]:
        """
        Obtiene una programacion por los filtros especificados.
        Args:
            filtros (Optional[dict], optional): Filtros para la consulta. Defaults to None.
        Returns:
            Optional[ProgramacionEntidad]: Programacion que cumple con los filtros especificados.
        """
        pass

    @abstractmethod
    async def verificar_existencia_por_filtros(self, filtros: Optional[dict] = None) -> bool:
        """
        Verifica si existe una programacion que cumple con los filtros especificados.
        Args:
            filtros (Optional[dict], optional): Filtros para la consulta. Defaults to None.
        Returns:
            bool: True si existe una programacion que cumple con los filtros especificados, False en caso contrario.
        """
        pass
