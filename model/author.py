from dataclasses import dataclass


@dataclass
class Author:

    def __init__(self, author_id: str, name: str, deleted: bool = False):
        self._author_id = author_id
        self._name = name
        self._deleted = deleted

    @property
    def author_id(self) -> str:
        return self._author_id

    @author_id.setter
    def author_id(self, value: str) -> None:
        self._author_id = value

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        self._name = value

    @property
    def deleted(self) -> bool:
        return self._deleted

    @deleted.setter
    def deleted(self, value: str) -> None:
        self._deleted = value

    def __str__(self):
        return f"ID: {self.author_id} - Name: {self.name}"
