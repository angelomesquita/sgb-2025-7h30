from abc import ABC, abstractmethod
from typing import Generic, Iterable, Optional, TypeVar
import sqlite3

T = TypeVar('T')


class BaseDao(ABC, Generic[T]):
    _DB_NAME = 'library.db'

    @classmethod
    def _get_connection(cls) -> sqlite3.Connection:
        connection = sqlite3.connect(cls._DB_NAME)
        connection.row_factory = sqlite3.Row
        return connection

    @classmethod
    @abstractmethod
    def create_table(cls) -> None:
        pass

    @classmethod
    @abstractmethod
    def save(cls, item: T) -> None:
        pass

    @classmethod
    @abstractmethod
    def get_all(cls) -> Iterable[T]:
        pass

    @classmethod
    @abstractmethod
    def get_by_id(cls, item_id: str, deleted: int = 0) -> Optional[T]:
        pass

    @classmethod
    @abstractmethod
    def delete(cls, item_id: str) -> None:
        pass

    @classmethod
    @abstractmethod
    def truncate(cls) -> None:
        pass
