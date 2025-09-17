from typing import Tuple

from controller.author_controller import AuthorController
from validators.author_validator import AuthorValidator
from view.view import View


class AuthorView(View):
    __NOT_FOUND = 'Author not found.\n'
    __INVALID_OPTION = 'Invalid option\n'

    def __init__(self):
        self.controller = AuthorController()

    def show_menu(self) -> None:
        while True:
            self.clear_screen()

            print('\n=== Author Module ===')
            print('1. Register Author')
            print('2. List Authors')
            print('3. Update Authors')
            print('4. Delete Authors')
            print('5. Restore Authors')
            print('0. Back to main menu')

            option = input('Select an option: ')

            menu_actions = {
                '1': self.register,
                '2': self.list,
                '3': self.update,
                '4': self.delete,
                '5': self.restore,
                '0': lambda: 'exit'
            }
            action = menu_actions.get(option)
            if action:
                if action() == 'exit':
                    break
            else:
                print(self.__INVALID_OPTION)
                self.press_enter_to_continue()

    def register(self) -> None:
        print("\n=== Register Author ===")
        data = self.get_author_data()
        self.controller.register(*data)
        self.press_enter_to_continue()
        self.clear_screen()

    def list(self) -> None:
        print('\n=== List Author ===')
        self.controller.list()
        self.press_enter_to_continue()
        self.clear_screen()

    def update(self) -> None:
        print('\n=== Update Author ===')
        author_id = self.get_author_id_data()
        author = self.controller.find(author_id)
        if author:
            data = self.get_author_data()
            self.controller.update(*data)
        else:
            print(self.__NOT_FOUND)
        self.press_enter_to_continue()
        self.clear_screen()

    def delete(self) -> None:
        print('\n=== Delete Author ===')
        author_id = self.get_author_id_data()
        author = self.controller.find(author_id)
        if author:
            self.controller.delete(author_id)
        else:
            print(self.__NOT_FOUND)
        self.press_enter_to_continue()
        self.clear_screen()

    def restore(self) -> None:
        print('\n=== Restore Author ===')
        author_id = self.get_author_id_data()
        author = self.controller.find_deleted(author_id)
        if author:
            self.controller.restore(author_id)
        else:
            print(self.__NOT_FOUND)
        self.press_enter_to_continue()
        self.clear_screen()

    def get_author_data(self) -> Tuple[str, str]:
        name = self.get_name()
        author_id = self.get_author_id_data()
        return name, author_id

    @staticmethod
    def get_name() -> str:
        while True:
            name = input("Name: ")
            if AuthorValidator.validate_name(name):
                return name
            print("❌ Invalid name. Must be at least 15 characters.")

    @staticmethod
    def get_author_id_data() -> str:
        while True:
            author_id = input("Author ID: ")
            try:
                int(author_id)
                return author_id
            except ValueError:
                print('❌ Invalid ID. Please enter an integer.\n')
