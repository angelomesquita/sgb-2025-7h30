from typing import Tuple

from controller.publisher_controller import PublisherController
from validators.publisher_validator import PublisherValidator
from view.view import View


class PublisherView(View):
    __NOT_FOUND = 'Publisher not found.\n'
    __INVALID_OPTION = 'Invalid option\n'

    def __init__(self):
        self.controller = PublisherController()

    def show_menu(self) -> None:
        while True:
            self.clear_screen()

            print('\n=== Publisher Module ===')
            print('1. Register Publisher')
            print('2. List Publishers')
            print('3. Update Publisher')
            print('4. Delete Publisher')
            print('5. Restore Publisher')
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
            if not self.run_action(menu_actions, option):
                break

    def register(self) -> None:
        print("\n=== Register Publisher ===")
        data = self.get_publisher_data()
        self.controller.register(*data)
        self.press_enter_to_continue()
        self.clear_screen()

    def list(self) -> None:
        print('\n=== List Publisher ===')
        self.controller.list()
        self.press_enter_to_continue()
        self.clear_screen()

    def update(self) -> None:
        print('\n=== Update Publisher ===')
        publisher_id = self.get_publisher_id_data()
        publisher = self.controller.find(publisher_id)
        if publisher:
            data = self.get_publisher_data()
            self.controller.update(*data)
        else:
            print(self.__NOT_FOUND)
        self.press_enter_to_continue()
        self.clear_screen()

    def delete(self) -> None:
        print('\n=== Delete Publisher ===')
        publisher_id = self.get_publisher_id_data()
        publisher = self.controller.find(publisher_id)
        if publisher:
            self.controller.delete(publisher_id)
        else:
            print(self.__NOT_FOUND)
        self.press_enter_to_continue()
        self.clear_screen()

    def restore(self) -> None:
        print('\n=== Restore Publisher ===')
        publisher_id = self.get_publisher_id_data()
        publisher = self.controller.find_deleted(publisher_id)
        if publisher:
            self.controller.restore(publisher_id)
        else:
            print(self.__NOT_FOUND)
        self.press_enter_to_continue()
        self.clear_screen()

    def get_publisher_data(self) -> Tuple[str, str, str, str]:
        author_id = self.get_publisher_id_data()
        legal_name = self.get_legal_name()
        city = self.get_city()
        state = self.get_state()
        return author_id, legal_name, city, state

    @staticmethod
    def get_publisher_id_data() -> str:
        while True:
            publisher_id = input("Publisher ID: ")
            if PublisherValidator.validate_publisher_id(publisher_id):
                return publisher_id
            print('❌ Invalid ID. Please enter an integer.')

    @staticmethod
    def get_legal_name() -> str:
        while True:
            legal_name = input("Legal Name: ")
            if PublisherValidator.validate_legal_name(legal_name):
                return legal_name
            print("❌ Invalid legal name. Must be at least 5 characters.")

    @staticmethod
    def get_city() -> str:
        while True:
            city = input("City: ")
            if PublisherValidator.validate_city(city):
                return city
            print("❌ Invalid city. Must be at least 5 characters.")

    @staticmethod
    def get_state() -> str:
        while True:
            state = input("State: ")
            if PublisherValidator.validate_state(state):
                return state
            print("❌ Invalid state. Must be 2 characters.")
