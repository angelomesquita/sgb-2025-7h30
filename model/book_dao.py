from model.base_dao_file import BaseDao
from model.book import Book
from repository.author_repository import AuthorRepository
from repository.publisher_repository import PublisherRepository


class BookDao(BaseDao[Book]):

    _FILE_PATH = 'books.txt'

    @staticmethod
    def _serialize(b: Book) -> str:
        return f"{b.isbn}|{b.title}|{b.author.author_id}|{b.publisher.publisher_id}|{b.year}|{b.quantity}|{b.deleted}"

    @staticmethod
    def _deserialize(data: str) -> Book:
        isbn, title, author_id, publisher_id, year, quantity, deleted = data.split("|")

        author = AuthorRepository.get_author_by_id(author_id)
        publisher = PublisherRepository.get_publisher_by_id(publisher_id)

        book = Book(isbn, title, author, publisher, year, quantity, deleted)
        book.deleted = deleted.lower() == "true"

        return book
