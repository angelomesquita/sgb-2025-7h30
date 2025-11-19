import os

from abc import ABC, abstractmethod
from typing import Generic, List, TypeVar

T = TypeVar("T")

"""
BaseDao is an abstract generic class that provides common persistence operations
for saving and loading objects from a text file.

This class serves as a base for specific DAO (Data Access Object) implementations,
such as EmployeeDao and CustomerDao, avoiding code duplication by centralizing
the file handling logic.

Type Parameters:
    T: The type of the object handled by the DAO (e.g, Customer, Employee)
    
Class Attributes:
    _FILE_PATH (str): Path to the file where the data will be stored.
                      This must be define in subclasses.
                      
Class Methods:
    save_all(items: List[T]) -> None:
        Saves all objects from the provided list into the file defined by `_FILE_PATH`.
        Each object is converted to a string representation using the `_serialize` method.
        
    load_all() -> List[T]:
        Load all objects from the file defined by `_FILE_PATH` and returns them as a list.
        Each line in the file is converted back to an object using the `_deserialize` method.
        If the file does not exist, it returns an empty list.
        
Abstract Methods:
     _serialize(item: T) -> str:
        Converts an object into a string for saving to the file.
        Must be implemented by the subclass to define the serialization format.
        
     _deserialize(data: str) -> T:
        Converts a string read from the file back int an object
        Must be implemented by the subclass to define the deserialization format.
"""


class BaseDao(ABC, Generic[T]):

    _FILE_PATH: str

    @classmethod
    def save_all(cls, items: List[T]) -> None:
        with open(cls._FILE_PATH, "w", encoding="utf-8") as file:
            for item in items:
                file.write(cls._serialize(item) + "\n")

    @classmethod
    def load_all(cls) -> List[T]:
        if not os.path.exists(cls._FILE_PATH):
            return []

        items: List[T] = []
        with open(cls._FILE_PATH, "r", encoding="utf-8") as file:
            for line in file:
                item = cls._deserialize(line.strip())
                items.append(item)

        return items

    @staticmethod
    @abstractmethod
    def _serialize(item: T) -> str:
        pass

    @staticmethod
    @abstractmethod
    def _deserialize(data: str) -> T:
        pass
