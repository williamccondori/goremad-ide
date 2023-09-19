from typing import TypeVar, Generic, Optional, List
from abc import ABC, abstractmethod

T = TypeVar("T")


class IBaseRepositorio(ABC, Generic[T]):
    @abstractmethod
    async def contar(self, filtros: Optional[dict] = None) -> int:
        pass

    @abstractmethod
    async def obtener_todos(self, filtros: Optional[dict] = None) -> List[T]:
        pass

    @abstractmethod
    async def obtener_por_id(self, entidad_id: str) -> T:
        pass

    @abstractmethod
    async def verificar_existencia(self, entidad_id: str) -> bool:
        pass

    @abstractmethod
    async def crear(self, entidad: T) -> str:
        pass

    @abstractmethod
    async def actualizar(self, entidad_id: str, entidad: T) -> str:
        pass

    @abstractmethod
    async def eliminar(self, entidad_id: str) -> str:
        pass
