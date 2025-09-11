from model.author import Author
from model.publisher import Publisher


class Book:

    def __init__(self, isbn: str, title: str, author: Author, publisher: Publisher, year: int, deleted: bool = False):
        self._isbn = isbn
        self._title = title
        self._author = author
        self._publisher = publisher
        self._year = year
        self._deleted = deleted

    @property
    def isbn(self) -> str:
        return self._isbn

    @isbn.setter
    def isbn(self, value: str) -> None:
        self._isbn = value

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, value: str) -> None:
        self._title = value

    @property
    def author(self) -> Author:
        return self._author

    @author.setter
    def author(self, value: str) -> None:
        self._author = value

    @property
    def publisher(self) -> Publisher:
        return self._publisher

    @publisher.setter
    def publisher(self, value: str) -> None:
        self._publisher = value

    @property
    def year(self) -> int:
        return self._year

    @year.setter
    def year(self, value: int) -> None:
        self._year = value

    def __str__(self):
        return f"ISBN: {self.isbn}, Title: {self.title}, Author: {self.author.name}, Publisher: {self.publisher.legal_name}, Year: {self.year}"
