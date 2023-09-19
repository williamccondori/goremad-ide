from abc import ABC, abstractmethod
from typing import List, TypeVar, Optional, Union, Generic

T = TypeVar("T")


class IBaseRepositorio(ABC, Generic[T]):
    """
    Interfaz para definir un repositorio base que maneja operaciones comunes
    en una base de datos.

    Los métodos descritos en esta interfaz son necesarios para realizar
    operaciones CRUD básicas.
    """

    @abstractmethod
    async def contar(self, filtros: Optional[dict] = None) -> int:
        """
        Contar el número de documentos que cumplen con ciertos filtros.

        :param filtros: Diccionario de condiciones para filtrar los documentos.
        :return: Número de documentos que cumplen con los filtros.
        """
        pass

    @abstractmethod
    async def obtener_todos(self, filtros: Optional[dict] = None) -> List[T]:
        """
        Obtener todos los documentos que cumplen con ciertos filtros.

        :param filtros: Diccionario de condiciones para filtrar los documentos.
        :return: Lista de entidades que cumplen con los filtros.
        """
        pass

    @abstractmethod
    async def obtener_por_id(self, id_entidad: str) -> T:
        """
        Obtener una entidad específica por su Identificador.

        :param id_entidad: Identificador del documento a recuperar.
        :return: Entidad correspondiente al Identificador dado.
        """
        pass

    @abstractmethod
    async def verificar_existencia(self, id_entidad: str) -> bool:
        """
        Verificar si existe un documento con el Identificador especificado.

        :param id_entidad: Identificador del documento a verificar.
        :return: Verdadero si el documento existe, falso en caso contrario.
        """
        pass

    @abstractmethod
    async def crear(self, entidad: T) -> str:
        """
        Crear una nueva entidad en la base de datos.

        :param entidad: Objeto de la entidad a crear.
        :return: Identificador del nuevo documento creado.
        """
        pass

    @abstractmethod
    async def actualizar(self, id_entidad: str, entidad: T) -> Union[str, None]:
        """
        Actualizar un documento existente en la base de datos.

        :param id_entidad: Identificador del documento a actualizar.
        :param entidad: Objeto de la entidad con los nuevos datos.
        :return: Identificador del documento actualizado o None si la actualización falla.
        """
        pass

    @abstractmethod
    async def eliminar(self, id_entidad: str, usuario_auditoria_id: str) -> str:
        """
        Eliminar (o marcar como inactivo) un documento específico por su Identificador.

        :param id_entidad: Identificador del documento a eliminar.
        :param usuario_auditoria_id: Identificador del usuario que está realizando la acción de eliminación.
        :return: Identificador del documento eliminado.
        """
        pass

    @abstractmethod
    async def obtener_por_filtros(self, filtros: Optional[dict] = None) -> Optional[T]:
        """
        Obtener un documento que cumple con ciertos filtros.

        :param filtros: Diccionario de condiciones para filtrar los documentos.
        :return: Entidad que cumple con los filtros o None si no se encuentra.
        """
        pass

    @abstractmethod
    async def verificar_existencia_por_filtros(self, filtros: Optional[dict] = None) -> bool:
        """
        Verificar si existe un documento que cumple con ciertos filtros.

        :param filtros: Diccionario de condiciones para filtrar los documentos.
        :return: Verdadero si el documento existe, falso en caso contrario.
        """
        pass
