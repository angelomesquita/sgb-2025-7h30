from typing import Optional, Iterable

from model.base_dao import BaseDao, T
from model.book import Book
from repository.author_repository import AuthorRepository
from repository.publisher_repository import PublisherRepository


class BookDao(BaseDao[Book]):

    @classmethod
    def create_table(cls) -> None:
        with cls._get_connection() as connection:
            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS books (
                    isbn TEXT PRIMARY KEY,
                    title TEXT NOT NULL,
                    author_id TEXT NOT NULL,
                    publisher_id TEXT NOT NULL,
                    year INTEGER NOT NULL,
                    quantity TEXT NOT NULL,
                    deleted INTEGER NOT NULL DEFAULT 0,
                    FOREIGN KEY (author_id) REFERENCES authors(author_id),
                    FOREIGN KEY (publisher_id) REFERENCES publishers(publisher_id)
                )
                """
            )
            connection.commit()

    @classmethod
    def save(cls, item: T) -> None:
        pass

    @classmethod
    def get_all(cls) -> Iterable[T]:
        pass

    @classmethod
    def get_by_id(cls, item_id: str, deleted: int = 0) -> Optional[T]:
        pass

    @classmethod
    def delete(cls, item_id: str) -> None:
        pass
