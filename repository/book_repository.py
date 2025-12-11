from typing import Iterable, List, Optional
from model.book import Book
from model.book_dao import BookDao
from model.exceptions import BookNotAvailableError, BookNotFoundError


class BookRepository:

    @staticmethod
    def get_all_books() -> Iterable[Book]:
        return BookDao.get_all()

    @staticmethod
    def get_book_by_isbn(isbn: str) -> Book:
        books = BookRepository.get_all_books()
        book = next((b for b in books if str(b.isbn) == isbn), None)
        if book is None:
            raise BookNotFoundError(f"Book with isbn {isbn} not found.")
        return book

    @staticmethod
    def search(
        title: Optional[str] = None,
        author: Optional[str] = None,
        available: Optional[bool] = None
    ) -> List[Book]:
        """Search books applying optional filters"""
        results = BookRepository.get_all_books()

        if title:
            results = [b for b in results if title.lower() in b.title.lower()]

        if author:
            results = [b for b in results if author.lower() in b.author.name.lower()]

        if available is not None:
            if available:
                results = [b for b in results if int(b.quantity) > 0]
            else:
                results = [b for b in results if int(b.quantity) <= 0]

        return results

    @staticmethod
    def decrease_quantity(isbn: str, amount: int = 1) -> Optional[bool]:
        book = BookRepository.get_book_by_isbn(isbn=isbn)

        if (book.quantity - amount) < 0:
            raise BookNotAvailableError(f"Book '{book.title}' is out of stock.")

        book.quantity -= amount
        BookDao.save(book)
        return True

    @staticmethod
    def increase_quantity(isbn: str, amount: int = 1) -> Optional[bool]:
        book = BookRepository.get_book_by_isbn(isbn=isbn)

        book.quantity += amount
        BookDao.save(book)
        return True
