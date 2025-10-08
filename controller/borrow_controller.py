from datetime import date, timedelta
from typing import List, Optional
from model.borrow import Borrow
from model.borrow_dao import BorrowDao
from model.logger import borrow_logger
from model.exceptions import BorrowLoadError
from repository.book_repository import BookRepository
from repository.employee_repository import EmployeeRepository
from repository.customer_repository import CustomerRepository


class BorrowController:

    def __init__(self):
        self._borrow_days = 7
        self.borrows: List[Borrow] = []
        try:
            self.borrows = BorrowDao.load_all()
            borrow_logger.info(f"{self.__class__.__name__} loaded successfully.")
        except BorrowLoadError as e:
            borrow_logger.error(f"{self.__class__.__class__}: Failed to load borrows - {e}")

    def find(self, borrow_id: str) -> Optional[Borrow]:
        for borrow in self.borrows:
            if borrow.borrow_id == borrow_id:
                return borrow
        return None

    def register(self, borrow_id: str, book_isbn: str, employee_cpf: str, customer_cpf: str) -> None:
        if not borrow_id:
            print('❌ borrow_id is required.')
            return
        if self.find(borrow_id):
            print(f'An entry with this {borrow_id} is already registered!\n')
            return

        borrow = Borrow(
            borrow_id=borrow_id,
            book=BookRepository.get_book_by_isbn(book_isbn),
            employee=EmployeeRepository.get_employee_by_cpf(employee_cpf),
            customer=CustomerRepository.get_customer_by_cpf(customer_cpf),
            start_date=date.today(),
            due_date=date.today() + timedelta(days=self._borrow_days),
            return_date=None,
            returned=False
        )

        self.borrows.append(borrow)
        BorrowDao.save_all(self.borrows)
        message = '✅ Borrow successfully registered!'
        borrow_logger.info(f"{message} [{borrow}]")
        print(message)
