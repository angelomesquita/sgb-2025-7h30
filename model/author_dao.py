from typing import Iterable, Optional

from model.author import Author
from model.base_dao import BaseDao


class AuthorDao(BaseDao[Author]):

    @classmethod
    def create_table(cls) -> None:
        with cls._get_connection() as connection:
            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS authors (
                    author_id TEXT PRIMARY KEY,
                    name TEXT NOT NULL,
                    deleted INTEGER NOT NULL DEFAULT 0
                )
                """
            )
            connection.commit()

    @classmethod
    def save(cls, author: Author) -> None:
        deleted_value = int(bool(author.deleted))
        with cls._get_connection() as connection:
            connection.execute(
                """
                INSERT INTO authors (author_id, name, deleted)
                VALUES (?, ?, ?)
                ON CONFLICT (author_id) DO UPDATE SET
                    name = excluded.name,
                    deleted = excluded.deleted
                """,
                (author.author_id, author.name, deleted_value),
            )
            connection.commit()

    @classmethod
    def get_all(cls) -> Iterable[Author]:
        """Returns all non-deleted authors."""
        with cls._get_connection() as connection:
            rows = connection.execute(
                "SELECT * FROM authors WHERE deleted = 0"
            ).fetchall()

        authors = []
        for row in rows:
            authors.append(
                Author(
                    author_id=row['author_id'],
                    name=row['name'],
                    deleted=bool(row['deleted'])
                )
            )
        return authors

    @classmethod
    def get_by_id(cls, author_id: str) -> Optional[Author]:
        with cls._get_connection() as connection:
            row = connection.execute(
                'SELECT * FROM authors WHERE author_id = ? AND deleted = ?', (author_id, 0,)
            ).fetchone()

        if row is None:
            return None

        return Author(
            author_id=row['author_id'],
            name=row['name'],
            deleted=bool(row['deleted'])
        )

    @classmethod
    def delete(cls, author_id: str) -> None:
        with cls._get_connection() as connection:
            connection.execute(
                'UPDATE authors SET deleted = 1 WHERE author_id = ?', (author_id,)
            )
            connection.commit()
