from model.base_dao import BaseDao
from model.borrow import Borrow
from repository.book_repository import BookRepository
from repository.employee_repository import EmployeeRepository
from repository.customer_repository import CustomerRepository


class BorrowDao(BaseDao[Borrow]):

    _FILE_PATH = 'borrows.txt'

    @staticmethod
    def _serialize(b: Borrow) -> str:
        return f"{b.borrow_id}|{b.book.isbn}|{b.employee.cpf}|{b.customer.cpf}|{b.start_date}|{b.due_date}|{b.return_date}|{b.returned}|{b.deleted}"

    @staticmethod
    def _deserialize(data: str) -> Borrow:
        borrow_id, book_isbn, employee_cpf, customer_cpf, start_date, due_date, return_date, returned, deleted = data.split("|")

        book = BookRepository.get_book_by_isbn(book_isbn)
        employee = EmployeeRepository.get_employee_by_cpf(employee_cpf)
        customer = CustomerRepository.get_customer_by_cpf(customer_cpf)

        return Borrow(
            borrow_id,
            book,
            employee,
            customer,
            start_date,
            due_date,
            return_date,
            returned.lower() == "true",
            deleted.lower() == "true"
        )
