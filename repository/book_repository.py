from typing import List, Optional
from model.book import Book
from model.book_dao import BookDao
from model.exceptions import BookNotAvailableError, BookNotFoundError


class BookRepository:

    @staticmethod
    def get_all_books() -> List[Book]:
        return BookDao.load_all()

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
    def decrease_quantity(book_isbn: str, amount: int = 1) -> None:
        books = BookRepository.get_all_books()
        for book in books:
            quantity = int(book.quantity)
            if book.isbn == book_isbn:
                if quantity - amount < 0:
                    raise BookNotAvailableError(f"Book '{book.title}' is not available.")
                quantity -= amount
                book.quantity = quantity
                break
        BookDao.save_all(books)

    @staticmethod
    def increase_quantity(book_isbn: str, amount: int = 1) -> None:
        books = BookRepository.get_all_books()
        for book in books:
            if book.isbn == book_isbn:
                quantity = int(book.quantity)
                quantity += amount
                book.quantity = quantity
                break
        BookDao.save_all(books)


