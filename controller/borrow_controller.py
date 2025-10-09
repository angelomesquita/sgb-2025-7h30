from datetime import date, timedelta

from controller.base_controller import BaseController
from model.borrow import Borrow
from model.borrow_dao import BorrowDao
from model.logger import borrow_logger
from model.exceptions import (
    BookNotAvailableError,
    BorrowAlreadyExistsError,
    BorrowDeletedError,
    BorrowNotFoundError,
    BorrowLoadError
)
from repository.book_repository import BookRepository
from repository.borrow_repository import BorrowRepository
from repository.employee_repository import EmployeeRepository
from repository.customer_repository import CustomerRepository


class BorrowController(BaseController[Borrow]):

    _BORROW_DAYS: int = 7

    dao_class = BorrowDao
    logger = borrow_logger

    AlreadyExistsError = BorrowAlreadyExistsError
    DeleteExistsError = BorrowDeletedError
    NotFoundError = BorrowNotFoundError
    LoadError = BorrowLoadError

    def __init__(self):
        super().__init__(model_class=Borrow, key_field="borrow_id")

    def register(self, borrow_id: str, book_isbn: str, employee_cpf: str, customer_cpf: str) -> None:
        try:
            BookRepository.decrease_quantity(book_isbn=book_isbn)
            super().register(borrow_id, book_isbn=book_isbn, employee_cpf=employee_cpf, customer_cpf=customer_cpf)
        except BookNotAvailableError as e:
            self.logger.error(str(e))
            print(f"⚠ Cannot register borrow: {e}")

    def create_instance(
        self,
        borrow_id: str,
        book_isbn: str,
        employee_cpf: str,
        customer_cpf: str,
        return_date: date = None,
        returned: bool = False,
        deleted: bool = False
    ) -> Borrow:

        book = BookRepository.get_book_by_isbn(book_isbn)
        employee = EmployeeRepository.get_employee_by_cpf(employee_cpf)
        customer = CustomerRepository.get_customer_by_cpf(customer_cpf)
        start_date = date.today()
        due_date = start_date + timedelta(days=self._BORROW_DAYS)

        return Borrow(
            borrow_id,
            book,
            employee,
            customer,
            start_date,
            due_date,
            return_date,
            returned,
            deleted
        )

    def update(
        self,
        borrow_id: str,
        book_isbn: str,
        employee_cpf: str,
        customer_cpf: str,
        return_date: date = None,
        returned: bool = False
    ) -> None:

        borrow = BorrowRepository.get_borrow_by_id(borrow_id)
        book = BookRepository.get_book_by_isbn(book_isbn)
        employee = EmployeeRepository.get_employee_by_cpf(employee_cpf)
        customer = CustomerRepository.get_customer_by_cpf(customer_cpf)

        if borrow.book.isbn != book.isbn:
            BookRepository.increase_quantity(borrow.book.isbn)
            BookRepository.decrease_quantity(book.isbn)

        super().update(
            borrow_id,
            book=book,
            employee=employee,
            customer=customer,
            return_date=return_date,
            returned=returned
        )
