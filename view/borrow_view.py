from typing import Tuple

from controller.borrow_controller import BorrowController
from model.cpf import Cpf
from validators.book_validator import BookValidator
from validators.borrow_validator import BorrowValidator
from view.view import View


class BorrowView(View):
    __NOT_FOUND = 'Borrow not found.\n'
    __INVALID_OPTION = 'Invalid option\n'

    def __init__(self):
        self.controller = BorrowController()

    def show_menu(self) -> None:
        while True:
            self.clear_screen()

            print('\n=== Borrow Module ===')
            print('1. Book Borrowing')
            print('2. List of Borrowings')
            print('3. Update Book Borrowing')
            print('4. Delete Book Borrowing')
            print('5. Restore Book Borrowing')
            print('6. Return borrowed Books')
            print('0. Back to main menu')

            option = input('Select an option: ')

            menu_actions = {
                '1': self.register,
                '2': self.list,
                '3': self.update,
                '4': self.delete,
                '5': self.restore,
                '6': self.return_book,
                '0': lambda: 'exit'
            }
            if not self.run_action(menu_actions, option):
                break

    def register(self) -> None:
        print("\n=== Book Borrowing ===")
        data = self.get_borrowing_data()
        self.controller.register(*data)
        self.press_enter_to_continue()
        self.clear_screen()

    def list(self) -> None:
        print('\n=== List of Borrowings ===')
        self.controller.list()
        self.press_enter_to_continue()
        self.clear_screen()

    def update(self) -> None:
        print('\n=== Update Book Borrowing ===')
        borrow_id = self.get_borrow_id()
        borrow = self.controller.find(borrow_id)
        if borrow:
            data = self.get_borrowing_data()
            self.controller.update(*data)
        else:
            print(self.__NOT_FOUND)
        self.press_enter_to_continue()
        self.clear_screen()

    def delete(self) -> None:
        print('\n=== Delete Book Borrowing ===')
        borrow_id = self.get_borrow_id()
        borrow = self.controller.find(borrow_id)
        if borrow:
            self.controller.delete(borrow_id)
        else:
            print(self.__NOT_FOUND)
        self.press_enter_to_continue()
        self.clear_screen()

    def restore(self) -> None:
        print('\n=== Delete Book Borrowing ===')
        borrow_id = self.get_borrow_id()
        borrow = self.controller.find_deleted(borrow_id)
        if borrow:
            self.controller.restore(borrow_id)
        else:
            print(self.__NOT_FOUND)
        self.press_enter_to_continue()
        self.clear_screen()

    def return_book(self) -> None:
        print('\n=== Return Books ===')
        borrow_id = self.get_borrow_id()
        borrow = self.controller.find(borrow_id)
        if borrow:
            self.controller.return_book(borrow_id)
        else:
            print(self.__NOT_FOUND)
        self.press_enter_to_continue()
        self.clear_screen()

    def get_borrowing_data(self) -> Tuple[str, str, str, str]:
        borrow_id = self.get_borrow_id()
        book_isbn = self.get_book_isbn()
        employee_cpf = self.get_employee_cpf()
        customer_cpf = self.get_customer_cpf()
        return borrow_id, book_isbn, employee_cpf, customer_cpf

    @staticmethod
    def get_borrow_id() -> str:
        while True:
            borrow_id = input("Borrow ID: ")
            if BorrowValidator.validate_borrow_id(borrow_id):
                return borrow_id
            print('❌ Invalid ID. Please enter an integer')

    @staticmethod
    def get_book_isbn() -> str:
        while True:
            book_isbn = input("Book ISBN: ")
            if BookValidator.validate_isbn(book_isbn):
                return book_isbn
            print('❌ Invalid Book ISBN. Please enter an integer.')

    @staticmethod
    def get_employee_cpf() -> str:
        while True:
            employee_cpf = input("Employee CPF: ")
            if Cpf.validate(employee_cpf):
                return employee_cpf
            print('❌ Invalid Employee CPF. Try again.')

    @staticmethod
    def get_customer_cpf() -> str:
        while True:
            customer_cpf = input("Customer CPF: ")
            if Cpf.validate(customer_cpf):
                return customer_cpf
            print('❌ Invalid Customer CPF. Try again.')
