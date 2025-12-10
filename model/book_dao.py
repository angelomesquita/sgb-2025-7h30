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
    def save(cls, book: Book) -> None:
        with cls._get_connection() as connection:
            connection.execute(
                """
                INSERT INTO books (isbn, title, author_id, publisher_id, year, quantity, deleted)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                ON CONFLICT (isbn) DO UPDATE SET
                    title = excluded.title,
                    author_id = excluded.author_id,
                    publisher_id = excluded.publisher_id,
                    year = excluded.year,
                    quantity = excluded.quantity,
                    deleted = excluded.deleted
                """,
                (
                    book.isbn,
                    book.title,
                    book.author.author_id,
                    book.publisher.publisher_id,
                    book.year,
                    book.quantity,
                    int(bool(book.deleted))
                )
            )
            connection.commit()

    @classmethod
    def _build_book_from_row(cls, row) -> Book:
        author = AuthorRepository.get_author_by_id(row['author_id'])
        publisher = PublisherRepository.get_publisher_by_id(row['publisher_id'])

        return Book(
            isbn=row['isbn'],
            title=row['title'],
            author=author,
            publisher=publisher,
            year=row['year'],
            quantity=row['quantity'],
            deleted=bool(row['deleted'])
        )

    @classmethod
    def get_all(cls) -> Iterable[Book]:
        with cls._get_connection() as connection:
            rows = connection.execute(
                "SELECT * FROM books WHERE deleted = 0"
            ).fetchall()

        books = []
        for row in rows:
            book = cls._build_book_from_row(row)
            books.append(book)

        return books

    @classmethod
    def get_by_id(cls, isbn: str, deleted: int = 0) -> Optional[Book]:
        with cls._get_connection() as connection:
            row = connection.execute(
                "SELECT * FROM books WHERE isbn = ? AND deleted = ?", (isbn, deleted, )
            ).fetchone()

        if row is None:
            return None

        return cls._build_book_from_row(row)

    @classmethod
    def delete(cls, isbn: str) -> None:
        with cls._get_connection() as connection:
            connection.execute("UPDATE books SET deleted = 1 WHERE isbn = ?", (isbn, ))
            connection.commit()

    @classmethod
    def restore(cls, isbn: str) -> None:
        with cls._get_connection() as connection:
            connection.execute("UPDATE books SET deleted = 0 WHERE isbn = ?", (isbn, ))
            connection.commit()
