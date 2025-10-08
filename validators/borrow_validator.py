from datetime import date
from model.book import Book
from validators.validator import Validator


class BorrowValidator:

    @staticmethod
    def validate_borrow_id(borrow_id: str) -> bool:
        return Validator.is_numeric(borrow_id)

    @staticmethod
    def validate_dates(start_date: date, due_date: date) -> bool:
        return start_date <= due_date

    @staticmethod
    def validate_availability(book: Book) -> bool:
        return book.quantity > 0
