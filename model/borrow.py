from datetime import date
from model.book import Book
from model.customer import Customer
from model.employee import Employee


class Borrow:

    def __init__(
        self,
        borrow_id: str,
        book: Book,
        employee: Employee,
        customer: Customer,
        start_date: date,
        due_date: date,
        return_date: date = None,
        returned: bool = False
    ) -> None:
        self._borrow_id = borrow_id
        self._book = book
        self._employee = employee
        self._customer = customer
        self._start_date = start_date
        self._due_date = due_date
        self._return_date = return_date
        self._returned = returned

    @property
    def borrow_id(self) -> str:
        return self._borrow_id

    @property
    def book(self) -> Book:
        return self._book

    @property
    def employee(self) -> Employee:
        return self._employee

    @property
    def customer(self) -> Customer:
        return self._customer

    @property
    def start_date(self) -> date:
        return self._start_date

    @property
    def due_date(self) -> date:
        return self._due_date

    @property
    def return_date(self) -> date:
        return self._return_date

    @return_date.setter
    def return_date(self, value: date) -> None:
        self._return_date = value

    @property
    def returned(self) -> bool:
        return self._returned

    @returned.setter
    def returned(self, value: bool) -> None:
        self._returned = value

    def __str__(self):
        return f"Borrow: {self.borrow_id} | Book: {self.book.title} | Employee: {self.employee.name} |Customer: {self.customer.name} | Start: {self.start_date} | Due: {self.due_date} | Return: {self.return_date} | Returned: {self.returned}"


