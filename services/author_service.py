from typing import List, Tuple
from model.author import Author
from model.author_dao import AuthorDao
from model.exceptions import AuthorNotFoundError


class AuthorService:

    @staticmethod
    def _get_all_authors() -> List[Author]:
        """Load all authors from DAO (active and deleted)"""
        return AuthorDao.load_all()

    @staticmethod
    def get_author_by_id(author_id: str) -> Author:
        authors = AuthorService._get_all_authors()
        author = next((a for a in authors if str(a.author_id) == author_id), None)
        if author is None:
            raise AuthorNotFoundError(f"Author with id {author_id} not found.")
        return author

    @staticmethod
    def options() -> List[Tuple[str, str]]:
        authors = AuthorService._get_all_authors()
        return [(str(a.author_id), a.name) for a in authors if not a.deleted]
