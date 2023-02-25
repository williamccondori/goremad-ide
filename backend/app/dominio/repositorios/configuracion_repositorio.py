from abc import abstractmethod
from typing import Optional

from app.dominio.entidades.configuracion_entidad import ConfiguracionEntidad


class IConfiguracionRepositorio:
    """
    Interfaz de repositorio de configuraciones.
    """

    @abstractmethod
    async def contar(self, filtros: Optional[dict] = None) -> int:
        """
        Cuenta la cantidad de configuraciones que cumplen con los filtros.
        Args:
            filtros (Optional[dict], optional): Filtros para la consulta. Defaults to None.
        Returns:
            int: Cantidad de configuraciones que cumplen con los filtros.
        """
        pass

    @abstractmethod
    async def obtener_todos(self, filtros: Optional[dict] = None) -> list[ConfiguracionEntidad]:
        """
        Obtiene todas las configuraciones que cumplen con los filtros.
        Args:
            filtros (Optional[dict], optional): Filtros para la consulta. Defaults to None.
        Returns:
            list[ConfiguracionEntidad]: Lista de configuraciones que cumplen con los filtros.
        """
        pass

    @abstractmethod
    async def obtener_por_id(self, servicio_externo_id: str) -> ConfiguracionEntidad:
        """
        Obtiene una configuracion por su identificador.
        Args:
            servicio_externo_id (str): Identificador de la configuracion.
        Returns:
            ConfiguracionEntidad: Configuracion con el identificador especificado.
        """
        pass

    @abstractmethod
    async def verificar_existencia(self, servicio_externo_id: str) -> bool:
        """
        Verifica si existe una configuracion con el identificador especificado.
        Args:
            servicio_externo_id (str): Identificador de la configuracion.
        Returns:
            bool: True si existe una configuracion con el identificador especificado, False en caso contrario.
        """
        pass

    @abstractmethod
    async def crear(self, servicio_externo: ConfiguracionEntidad) -> str:
        """
        Crea una configuracion.
        Args:
            servicio_externo (ConfiguracionEntidad): Configuracion a crear.
        Returns:
            str: Identificador de la configuracion creada.
        """
        pass

    @abstractmethod
    async def actualizar(self, servicio_externo_id: str, servicio_externo: ConfiguracionEntidad) -> str:
        """
        Actualiza una configuracion.
        Args:
            servicio_externo_id (str): Identificador de la configuracion a actualizar.
            servicio_externo (ConfiguracionEntidad): Configuracion a actualizar.
        Returns:
            str: Identificador de la configuracion actualizada.
        """
        pass

    @abstractmethod
    async def eliminar(self, servicio_externo_id: str, usuario_auditoria_id: str) -> str:
        """
        Elimina una configuracion.
        Args:
            servicio_externo_id (str): Identificador de la configuracion a eliminar.
            usuario_auditoria_id (str): Identificador del usuario que realiza la eliminacion.
        Returns:
            str: Identificador de la configuracion eliminada.
        """
        pass

    @abstractmethod
    async def obtener_por_filtros(self, filtros: Optional[dict] = None) -> Optional[ConfiguracionEntidad]:
        """
        Obtiene una configuracion por los filtros especificados.
        Args:
            filtros (Optional[dict], optional): Filtros para la consulta. Defaults to None.
        Returns:
            Optional[ConfiguracionEntidad]: Configuracion que cumple con los filtros especificados.
        """
        pass

    @abstractmethod
    async def verificar_existencia_por_filtros(self, filtros: Optional[dict] = None) -> bool:
        """
        Verifica si existe una configuracion que cumpla con los filtros especificados.
        Args:
            filtros (Optional[dict], optional): Filtros para la consulta. Defaults to None.
        Returns:
            bool: True si existe una configuracion que cumpla con los filtros especificados, False en caso contrario.
        """
        pass

    @abstractmethod
    async def crear_multiple(self, configuraciones: list[ConfiguracionEntidad]) -> list[str]:
        """
        Crea multiples configuraciones.
        Args:
            configuraciones (list[ConfiguracionEntidad]): Lista de configuraciones a crear.
        Returns:
            list[str]: Lista de identificadores de las configuraciones creadas.
        """
        pass

    @abstractmethod
    async def obtener_valor_por_clave(self, clave: str) -> str:
        """
        Obtiene el valor de una configuracion por su clave.
        Args:
            clave (str): Clave de la configuracion.
        Returns:
            str: Valor de la configuracion.
        """
        pass
