from model.base_dao import BaseDao
from model.author import Author


class AuthorDao(BaseDao[Author]):

    _FILE_PATH = 'authors.txt'

    @staticmethod
    def _serialize(a: Author) -> str:
        return f"{a.name}|{a.deleted}"

    @staticmethod
    def _deserialize(data: str) -> Author:
        name, deleted = data.split("|")
        author = Author(name, deleted)
        author.deleted = deleted.lower() == "true"

        return author
