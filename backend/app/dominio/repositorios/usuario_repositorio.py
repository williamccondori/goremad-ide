from abc import abstractmethod  # noqa
from typing import Optional

from app.dominio.entidades.usuario_entidad import UsuarioEntidad


class IUsuarioRepositorio:
    """
    Interfaz de repositorio de usuarios.
    """
    @abstractmethod
    async def contar(self, filtros: Optional[dict] = None) -> int:
        """
        Cuenta la cantidad de usuarios que cumplen con los filtros.
        Args:
            filtros (Optional[dict], optional): Filtros para la consulta. Defaults to None.
        Returns:
            int: Cantidad de usuarios que cumplen con los filtros.
        """
        pass

    @abstractmethod
    async def obtener_todos(self, filtros: Optional[dict] = None) -> list[UsuarioEntidad]:
        """
        Obtiene todos los usuarios que cumplen con los filtros.
        Args:
            filtros (Optional[dict], optional): Filtros para la consulta. Defaults to None.
        Returns:
            list[UsuarioEntidad]: Lista de usuarios que cumplen con los filtros.
        """
        pass

    @abstractmethod
    async def obtener_por_id(self, usuario_id: str) -> UsuarioEntidad:
        """
        Obtiene un usuario por su identificador.
        Args:
            usuario_id (str): Identificador del usuario.
        Returns:
            UsuarioEntidad: Usuario con el identificador especificado.
        """
        pass

    @abstractmethod
    async def verificar_existencia(self, usuario_id: str) -> bool:
        """
        Verifica si existe un usuario con el identificador especificado.
        Args:
            usuario_id (str): Identificador del usuario.
        Returns:
            bool: True si existe un usuario con el identificador especificado, False en caso contrario.
        """
        pass

    @abstractmethod
    async def crear(self, usuario: UsuarioEntidad) -> str:
        """
        Crea un usuario.
        Args:
            usuario (UsuarioEntidad): Usuario a crear.
        Returns:
            str: Identificador del usuario creado.
        """
        pass

    @abstractmethod
    async def actualizar(self, usuario_id: str, usuario: UsuarioEntidad) -> str:
        """
        Actualiza un usuario.
        Args:
            usuario_id (str): Identificador del usuario a actualizar.
            usuario (UsuarioEntidad): Usuario a actualizar.
        Returns:
            str: Identificador del usuario actualizado.
        """
        pass

    @abstractmethod
    async def eliminar(self, usuario_id: str, usuario_auditoria_id: str) -> str:
        """
        Elimina un usuario.
        Args:
            usuario_id (str): Identificador del usuario a eliminar.
            usuario_auditoria_id (str): Identificador del usuario que realiza la eliminación.
        Returns:
            str: Identificador del usuario eliminado.
        """
        pass

    @abstractmethod
    async def obtener_por_filtros(self, filtros: Optional[dict] = None) -> Optional[UsuarioEntidad]:
        """
        Obtiene un usuario por los filtros especificados.
        Args:
            filtros (Optional[dict], optional): Filtros para la consulta. Defaults to None.
        Returns:
            Optional[UsuarioEntidad]: Usuario que cumple con los filtros especificados.
        """
        pass

    @abstractmethod
    async def verificar_existencia_por_filtros(self, filtros: Optional[dict] = None) -> bool:
        """
        Verifica si existe un usuario que cumpla con los filtros especificados.
        Args:
            filtros (Optional[dict], optional): Filtros para la consulta. Defaults to None.
        Returns:
            bool: True si existe un usuario que cumpla con los filtros especificados, False en caso contrario.
        """
        pass
