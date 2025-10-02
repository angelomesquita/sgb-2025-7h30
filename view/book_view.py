from typing import Tuple

from controller.book_controller import BookController
from services.author_service import AuthorService
from services.publisher_service import PublisherService
from validators.book_validator import BookValidator
from view.view import View


class BookView(View):
    __NOT_FOUND = 'Book not found.\n'
    __INVALID_OPTION = 'Invalid option\n'

    def __init__(self):
        self.controller = BookController()

    def show_menu(self) -> None:
        while True:
            self.clear_screen()

            print('\n=== Book Module ===')
            print('1. Register Book')
            print('2. List Books')
            print('3. Update Book')
            print('4. Delete Book')
            print('5. Restore Book')
            print('6. Adjust Quantity')
            print('0. Back to main menu')

            option = input('Select an option: ')

            menu_actions = {
                '1': self.register,
                '2': self.list,
                '3': self.update,
                '4': self.delete,
                '5': self.restore,
                '6': self.adjust_quantity,
                '0': lambda: 'exit'
            }
            if not self.run_action(menu_actions, option):
                break

    def register(self) -> None:
        print("\n=== Register Book ===")
        data = self.get_book_data()
        self.controller.register(*data)
        self.press_enter_to_continue()
        self.clear_screen()

    def list(self) -> None:
        print('\n=== List Books ===')
        self.controller.list()
        self.press_enter_to_continue()
        self.clear_screen()

    def update(self) -> None:
        print('\n=== Update Book ===')
        isbn = self.get_isbn()
        book = self.controller.find(isbn)
        if book:
            data = self.get_book_data()
            self.controller.update(*data)
        else:
            print(self.__NOT_FOUND)
        self.press_enter_to_continue()
        self.clear_screen()

    def delete(self) -> None:
        print('\n=== Delete Book ===')
        isbn = self.get_isbn()
        book = self.controller.find(isbn)
        if book:
            self.controller.delete(isbn)
        else:
            print(self.__NOT_FOUND)
        self.press_enter_to_continue()
        self.clear_screen()

    def restore(self) -> None:
        print('\n=== Restore Book ===')
        isbn = self.get_isbn()
        book = self.controller.find_deleted(isbn)
        if book:
            self.controller.restore(isbn)
        else:
            print(self.__NOT_FOUND)
        self.press_enter_to_continue()
        self.clear_screen()

    def adjust_quantity(self) -> None:
        print('\n=== Adjust Quantity ===')
        isbn = self.get_isbn()
        amount = self.get_amount()
        book = self.controller.find(isbn)
        if book:
            self.controller.adjust_quantity(isbn, amount)
        else:
            print(self.__NOT_FOUND)
        self.press_enter_to_continue()
        self.clear_screen()

    def get_book_data(self) -> Tuple[str, str, str, str, str, str]:
        isbn = self.get_isbn()
        title = self.get_title()
        author_id = self.get_author_id()
        publisher_id = self.get_publisher_id()
        year = self.get_year()
        quantity = self.get_quantity()
        return isbn, title, author_id, publisher_id, year, quantity

    @staticmethod
    def get_isbn() -> str:
        while True:
            isbn = input("ISBN: ")
            if BookValidator.validate_isbn(isbn):
                return isbn
            print('❌ Invalid ID. Please enter an integer.')

    @staticmethod
    def get_title() -> str:
        while True:
            title = input("Title: ")
            if BookValidator.validate_title(title):
                return title
            print("❌ Invalid title. Must be at least 5 characters.")

    @staticmethod
    def get_author_id() -> str:
        print('Choose Author: ')
        options = AuthorService.options()
        for i, (value, label) in enumerate(options, start=1):
            print(f"{i}. {label}")
        while True:
            choice = input('Enter the author id: ')
            if choice.isdigit() and 1 <= int(choice) <= len(options):
                return options[int(choice)-1][0]

    @staticmethod
    def get_publisher_id() -> str:
        print('Choose Publisher: ')
        options = PublisherService.options()
        for i, (value, label) in enumerate(options, start=1):
            print(f"{i}. {label}")
        while True:
            choice = input('Enter the publisher id: ')
            if choice.isdigit() and 1 <= int(choice) <= len(options):
                return options[int(choice)-1][0]

    @staticmethod
    def get_year() -> str:
        while True:
            year = input("Year: ")
            if BookValidator.validate_year(int(year)):
                return year
            print("❌ Invalid year. Must be a number less than or equal to the current year.")

    @staticmethod
    def get_quantity() -> str:
        while True:
            quantity = input("Quantity: ")
            if BookValidator.validate_quantity(int(quantity)):
                return quantity
            print("❌ Invalid quantity. Must be greater than zero.")

    @staticmethod
    def get_amount() -> str:
        while True:
            amount = input('Amount: ')
            if BookValidator.validate_amount(amount):
                return amount
            print('❌ Invalid amount. Must be a integer number')
