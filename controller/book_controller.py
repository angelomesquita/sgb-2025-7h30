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
from repository.author_repository import AuthorRepository
from repository.book_repository import BookRepository
from repository.publisher_repository import PublisherRepository


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

    def register(self, isbn: str, title: str, author_id: str, publisher_id: str, year: int, quantity: int) -> None:
        super().register(isbn, title=title, author_id=author_id, publisher_id=publisher_id, year=year, quantity=quantity)

    def create_instance(self, isbn: str, title: str, author_id: str, publisher_id: str, year: int, quantity: int, deleted: bool = False) -> Book:
        author = AuthorRepository.get_author_by_id(author_id)
        publisher = PublisherRepository.get_publisher_by_id(publisher_id)
        return Book(isbn, title, author, publisher, year, quantity, deleted)

    def update(self, isbn: str, title: str, author_id: str, publisher_id: str, year: int, quantity: int) -> None:
        author = AuthorRepository.get_author_by_id(author_id)
        publisher = PublisherRepository.get_publisher_by_id(publisher_id)
        super().update(isbn, title=title, author=author, publisher=publisher, year=year, quantity=quantity)

    def adjust_quantity(self, isbn: str, amount: str) -> None:
        book = self.find(isbn)
        if not book:
            print(f"Book with ISBN {isbn} not found.")
        book.quantity = int(book.quantity) + int(amount)
        self.dao_class.save_all(self.items)
        message = f'✅ {book.__class__.__name__} quantity updated. New quantity: {book.quantity}'
        self.logger.info(f"{message} [{book}]")
        print(message)

    def search_books(self, title: str, author: str, available: bool) -> None:
        results = BookRepository.search(title=title, author=author, available=available)
        if not results:
            message = f'\nNo books found with the given filters: {title}, {author}, {available}'
            self.logger.info(message)
            print(message)
            return
        print(f'\nFound {len(results)} book(s):')
        for book in results:
            print(book)
        print()
