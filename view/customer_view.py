from getpass import getpass
from typing import Tuple

from controller.customer_controller import CustomerController
from model.category import Category
from model.cpf import Cpf
from model.password import Password
from validators.customer_validator import CustomerValidator
from view.view import View


class CustomerView(View):
    __CUSTOMER_NOT_FOUND = 'Customer not found.\n'
    __INVALID_OPTION = 'Invalid option\n'

    def __init__(self):
        self.controller = CustomerController()

    def show_menu(self) -> None:
        while True:
            self.clear_screen()

            print('\n=== Customer Module ===')
            print('1. Register Customer')
            print('2. List Customers')
            print('3. Update Customers')
            print('4. Delete Customers')
            print('5. Restore Customers')
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
        print("\n=== Register Customer ===")
        data = self.get_customer_data()
        self.controller.register(*data)
        self.press_enter_to_continue()
        self.clear_screen()

    def list(self) -> None:
        print('\n=== List Customer ===')
        self.controller.list()
        self.press_enter_to_continue()
        self.clear_screen()

    def update(self) -> None:
        print('\n=== Update Customer ===')
        cpf = self.get_cpf_data()
        customer = self.controller.find(cpf)
        if customer:
            data = self.get_customer_data()
            self.controller.update(*data)
        else:
            print(self.__CUSTOMER_NOT_FOUND)
        self.press_enter_to_continue()
        self.clear_screen()

    def delete(self) -> None:
        print('\n=== Delete Customer ===')
        cpf = self.get_cpf_data()
        customer = self.controller.find(cpf)
        if customer:
            self.controller.delete(cpf)
        else:
            print(self.__CUSTOMER_NOT_FOUND)
        self.press_enter_to_continue()
        self.clear_screen()

    def restore(self) -> None:
        print('\n=== Restore Customer ===')
        cpf = self.get_cpf_data()
        customer = self.controller.find_deleted(cpf)
        if customer:
            self.controller.restore(cpf)
        else:
            print(self.__CUSTOMER_NOT_FOUND)
        self.press_enter_to_continue()
        self.clear_screen()

    def get_customer_data(self) -> Tuple[str, str, str, str, str]:
        name = self.get_name()
        cpf = self.get_cpf_data()
        contact = self.get_contact()
        category = self.get_category_customer()
        password = self.get_password()
        return name, cpf, contact, category, password

    @staticmethod
    def get_name() -> str:
        while True:
            name = input("Name: ")
            if CustomerValidator.validate_name(name):
                return name
            print("❌ Invalid name. Must be at least 15 characters.")

    @staticmethod
    def get_cpf_data() -> str:
        while True:
            cpf = input("CPF: ")
            if Cpf.validate(cpf):
                return cpf
            print('❌ Invalid CPF. Try again.\n')

    @staticmethod
    def get_contact() -> str:
        while True:
            contact = input("Contact: ")
            if CustomerValidator.validate_contact(contact):
                return contact
            print("❌ Invalid name. Must be a simple email format.")

    @staticmethod
    def get_category_customer() -> str:
        print('Choose Category: ')
        options = Category.options()
        for i, (value, label) in enumerate(options, start=1):
            print(f"{i}. {label}")
        while True:
            choice = input('Enter the category number: ')
            if choice.isdigit() and 1 <= int(choice) <= len(options):
                return options[int(choice)-1][0]

    @staticmethod
    def get_password() -> str:
        password = getpass("Password: ")
        while True:
            if Password.validate(password):
                return password
            print('❌ Invalid password. Password >= 6 characters.\n')
