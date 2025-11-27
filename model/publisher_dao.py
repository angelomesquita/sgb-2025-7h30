from typing import Optional, Iterable

from model.base_dao import BaseDao
from model.publisher import Publisher


class PublisherDao(BaseDao[Publisher]):

    @classmethod
    def create_table(cls) -> None:
        with cls._get_connection() as connection:
            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS publishers (
                    publisher_id TEXT PRIMARY KEY,
                    legal_name TEXT NOT NULL,
                    city TEXTO NOT NULL,
                    state TEXTO NOT NULL,
                    deleted INTEGER NOT NULL DEFAULT 0
                )
                """
            )
            connection.commit()

    @classmethod
    def save(cls, publisher: Publisher) -> None:
        with cls._get_connection() as connection:
            connection.execute(
                """
                INSERT INTO publishers (publisher_id, legal_name, city, state, deleted)
                VALUES (?, ?, ?, ?, ?)
                ON CONFLICT (publisher_id) DO UPDATE SET
                    legal_name = excluded.legal_name,
                    city = excluded.city,
                    state = excluded.state,
                    deleted = excluded.deleted
                """,
                (publisher.publisher_id, publisher.legal_name, publisher.city, publisher.state, publisher.deleted)
            )
            connection.commit()

    @classmethod
    def get_all(cls) -> Iterable[Publisher]:
        with cls._get_connection() as connection:
            rows = connection.execute(
                "SELECT * FROM publishers WHERE deleted = 0"
            ).fetchall()

            publishers = []
            for row in rows:
                publishers.append(
                    Publisher(
                        publisher_id=row['publisher_id'],
                        legal_name=row['legal_name'],
                        city=row['city'],
                        state=row['state'],
                        deleted=bool(row['deleted'])
                    )
                )
            return publishers

    @classmethod
    def get_by_id(cls, publisher_id: str, deleted: int = 0) -> Optional[Publisher]:
        with cls._get_connection() as connection:
            row = connection.execute(
                "SELECT * FROM publishers WHERE publisher_id = ? AND deleted = ?", (publisher_id, deleted,)
            ).fetchone()

            if row is None:
                return None

            return Publisher(
                publisher_id=row['publisher_id'],
                legal_name=row['legal_name'],
                city=row['city'],
                state=row['state'],
                deleted=bool(row['deleted'])
            )

    @classmethod
    def delete(cls, publisher_id: str) -> None:
        with cls._get_connection() as connection:
            connection.execute(
                "UPDATE publishers SET deleted = 1 WHERE publisher_id = ?", (publisher_id, )
            )
            connection.commit()
