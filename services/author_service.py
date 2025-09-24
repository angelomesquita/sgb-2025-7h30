from model.author import Author
from model.author_dao import AuthorDao
from model.exceptions import AuthorNotFoundError


class AuthorService:

    @staticmethod
    def get_author_by_id(author_id: str) -> Author:
        authors = AuthorDao.load_all()
        author = next((a for a in authors if str(a.author_id) == author_id), None)
        if author is None:
            raise AuthorNotFoundError(f"Author with id {author_id} not found.")
        return author
