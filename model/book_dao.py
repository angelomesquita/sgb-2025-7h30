from model.base_dao import BaseDao
from model.book import Book
from services.author_service import AuthorService
from services.publisher_service import PublisherService


class BookDao(BaseDao[Book]):

    _FILE_PATH = 'books.txt'

    @staticmethod
    def _serialize(b: Book) -> str:
        return f"{b.isbn}|{b.title}|{b.author.author_id}|{b.publisher.publisher_id}|{b.year}|{b.deleted}"

    @staticmethod
    def _deserialize(data: str) -> Book:
        isbn, title, author_id, publisher_id, year, deleted = data.split("|")

        author = AuthorService.get_author_by_id(author_id)
        publisher = PublisherService.get_publisher_by_id(publisher_id)

        book = Book(isbn, title, author, publisher, year, deleted)
        book.deleted = deleted.lower() == "true"

        return book
