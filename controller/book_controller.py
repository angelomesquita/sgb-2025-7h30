from controller.base_controller import BaseController
from model.book import Book
from model.book_dao import BookDao
from model.logger import book_logger
from model.exceptions import (
    BookAlreadyExistsError,
    BookDeletedError,
    BookRestoreError,
    BookNotFoundError,
    BookLoadError,
)
from services.author_service import AuthorService
from services.publisher_service import PublisherService


class BookController(BaseController[Book]):

    dao_class = BookDao
    logger = book_logger

    AlreadyExistsError = BookAlreadyExistsError
    DeletedError: BookDeletedError
    RestoredError: BookRestoreError
    NotFoundError: BookNotFoundError
    LoadError: BookLoadError

    def __init__(self):
        super().__init__(model_class=Book, key_field="isbn")

    def register(self, isbn: str, title: str, author_id: str, publisher_id: str, year: int) -> None:
        super().register(isbn, title=title, author_id=author_id, publisher_id=publisher_id, year=year)

    def create_instance(self, isbn: str, title: str, author_id: str, publisher_id: str, year: int, deleted: bool = False) -> Book:
        author = AuthorService.get_author_by_id(author_id)
        publisher = PublisherService.get_publisher_by_id(publisher_id)
        return Book(isbn, title, author, publisher, year, deleted)

    def update(self, isbn: str, title: str, author_id: str, publisher_id: str, year: int) -> None:
        author = AuthorService.get_author_by_id(author_id)
        publisher = PublisherService.get_publisher_by_id(publisher_id)
        super().update(isbn, title=title, author=author, publisher=publisher, year=year)
