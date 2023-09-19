from typing import TypeVar, Generic, Optional, List
from abc import ABC, abstractmethod

T = TypeVar("T")


class IBaseRepositorio(ABC, Generic[T]):
    """
    Interfaz base para repositorios.
    Define métodos CRUD básicos para interactuar con cualquier entidad de tipo T.
    """

    @abstractmethod
    async def contar(self, filtros: Optional[dict] = None) -> int:
        """
        Cuenta el número de documentos que coinciden con los filtros dados.

        Parámetros:
            filtros (dict, opcional): Un diccionario que contiene los criterios de búsqueda.

        Devuelve:
            int: El número de documentos que coinciden con los filtros.
        """
        pass

    @abstractmethod
    async def obtener_todos(self, filtros: Optional[dict] = None) -> List[T]:
        """
        Obtiene todos los documentos que coinciden con los filtros dados.

        Parámetros:
            filtros (dict, opcional): Un diccionario que contiene los criterios de búsqueda.

        Devuelve:
            List[T]: Una lista de objetos de tipo T que coinciden con los filtros.
        """
        pass

    @abstractmethod
    async def obtener_por_id(self, id_entidad: str) -> T:
        """
        Obtiene un documento por su identificador único.

        Parámetros:
            id_entidad (str): El identificador único del documento.

        Devuelve:
            T: Un objeto de tipo T que tiene el identificador dado.

        Lanza:
            ApplicationException: Si el documento con el identificador dado no se encuentra.
        """
        pass

    @abstractmethod
    async def verificar_existencia(self, id_entidad: str) -> bool:
        """
        Verifica si existe un documento con el identificador único dado.

        Parámetros:
            id_entidad (str): El identificador único del documento.

        Devuelve:
            bool: Verdadero si el documento existe, falso de lo contrario.
        """
        pass

    @abstractmethod
    async def crear(self, entidad: T) -> str:
        """
        Crea un nuevo documento basado en la entidad dada.

        Parámetros:
            entidad (T): El objeto que se va a crear.

        Devuelve:
            str: El identificador único del documento creado.
        """
        pass

    @abstractmethod
    async def actualizar(self, id_entidad: str, entidad: T) -> str:
        """
        Actualiza un documento existente con los nuevos datos de la entidad dada.

        Parámetros:
            id_entidad (str): El identificador único del documento a actualizar.
            entidad (T): El nuevo objeto con los datos actualizados.

        Devuelve:
            str: El identificador único del documento actualizado.

        Lanza:
            ApplicationException: Si el documento con el identificador dado no se encuentra.
        """
        pass

    @abstractmethod
    async def eliminar(self, id_entidad: str) -> str:
        """
        Elimina un documento por su identificador único. La eliminación podría ser lógica o física dependiendo de la implementación.

        Parámetros:
            id_entidad (str): El identificador único del documento a eliminar.

        Devuelve:
            str: El identificador único del documento eliminado.

        Lanza:
            ApplicationException: Si el documento con el identificador dado no se encuentra.
        """
        pass
