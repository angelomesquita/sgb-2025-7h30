from model.author_dao import AuthorDao
from model.base_dao import BaseDao
from model.publisher_dao import PublisherDao
from model.book import Book
from model.exceptions import AuthorNotFoundError, PublisherNotFoundError


class BookDao(BaseDao[Book]):

    _FILE_PATH = 'books.txt'

    @staticmethod
    def _serialize(b: Book) -> str:
        return f"{b.isbn}|{b.title}|{b.author.author_id}|{b.publisher.publisher_id}|{b.year}|{b.deleted}"

    @staticmethod
    def _deserialize(data: str) -> Book:
        isbn, title, author_id, publisher_id, year, deleted = data.split("|")

        authors = AuthorDao.load_all()
        author = next((a for a in authors if str(a.author_id) == author_id), None)
        if author is None:
            raise AuthorNotFoundError(f"Author with id {author_id} not found.")

        publishers = PublisherDao.load_all()
        publisher = next((p for p in publishers if str(p.publisher_id) == publisher_id), None)
        if publisher is None:
            raise PublisherNotFoundError(f"Publisher with id {publisher_id} not found.")

        book = Book(isbn, title, author, publisher, year, deleted)
        book.deleted = deleted.lower() == "true"

        return book
