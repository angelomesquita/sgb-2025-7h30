from typing import Iterable, List, Tuple
from model.author import Author
from model.author_dao import AuthorDao
from model.exceptions import AuthorNotFoundError


class AuthorRepository:

    @staticmethod
    def get_all_authors() -> Iterable[Author]:
        """Load all authors from DAO (active and deleted)"""
        return AuthorDao.get_all()

    @staticmethod
    def get_author_by_id(author_id: str) -> Author:
        authors = AuthorRepository.get_all_authors()
        author = next((a for a in authors if str(a.author_id) == author_id), None)
        if author is None:
            raise AuthorNotFoundError(f"Author with id {author_id} not found.")
        return author

    @staticmethod
    def options() -> List[Tuple[str, str]]:
        authors = AuthorRepository.get_all_authors()
        return [(str(a.author_id), a.name) for a in authors if not a.deleted]
