from getpass import getpass
from typing import Tuple

from controller.auth_controller import AuthController
from controller.employee_controller import EmployeeController
from model.cpf import Cpf
from model.password import Password
from validators.employee_validator import EmployeeValidator
from view.view import View


class EmployeeView(View):
    __EMPLOYEE_NOT_FOUND = 'Employee not found.\n'
    __INVALID_OPTION = 'Invalid option\n'

    def __init__(self):
        self.controller = EmployeeController()

    def show_menu(self) -> None:
        while True:
            self.clear_screen()

            print('\n=== Employee Module ===')
            print('1. Register Employee')
            print('2. List Employees')
            print('3. Authenticate Employee')
            print('4. Update Employee')
            print('5. Delete Employee')
            print('6. Restore Employee')
            print('0. Back to main menu')

            option = input('Select an option: ')

            menu_actions = {
                '1': self.register,
                '2': self.list,
                '3': self.authenticate,
                '4': self.update,
                '5': self.delete,
                '6': self.restore,
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
        print("\n=== Register Employee ===")
        data = self.get_employee_data()
        self.controller.register(*data)
        self.press_enter_to_continue()

    def list(self) -> None:
        print('\n=== List Employees ===')
        self.controller.list()
        self.press_enter_to_continue()

    def authenticate(self) -> None:
        print("\n=== Authenticate Employee ===")
        username, password = self.get_auth_data()
        AuthController.auth(self.controller.items, username, password)
        self.press_enter_to_continue()

    def update(self) -> None:
        print('\n=== Update Employee ===')
        cpf = self.get_cpf_data()
        employee = self.controller.find(cpf)
        if employee:
            data = self.get_employee_data()
            self.controller.update(*data)
        else:
            print(self.__EMPLOYEE_NOT_FOUND)
        self.press_enter_to_continue()

    def delete(self) -> None:
        print('\n=== Delete Employee ===')
        cpf = self.get_cpf_data()
        employee = self.controller.find(cpf)
        if employee:
            self.controller.delete(cpf)
        else:
            print(self.__EMPLOYEE_NOT_FOUND)
        self.press_enter_to_continue()

    def restore(self) -> None:
        print('\n=== Restore Employee ===')
        cpf = self.get_cpf_data()
        employee = self.controller.find_deleted(cpf)
        if employee:
            self.controller.restore(cpf)
        else:
            print(self.__EMPLOYEE_NOT_FOUND)
        self.press_enter_to_continue()

    def get_employee_data(self) -> Tuple[str, str, str, str, str]:
        name = self.get_name()
        cpf = self.get_cpf_data()
        role = self.get_role()
        username, password = self.get_auth_data()
        return name, cpf, role, username, password

    @staticmethod
    def get_name() -> str:
        while True:
            name = input("Name: ")
            if EmployeeValidator.validate_name(name):
                return name
            print("❌ Invalid name. Must be at least 3 characters.")

    @staticmethod
    def get_cpf_data() -> str:
        while True:
            cpf = input("CPF: ")
            if Cpf.validate(cpf):
                return cpf
            print('❌ Invalid CPF. Try again.\n')

    @staticmethod
    def get_role() -> str:
        while True:
            role = input("Role: ")
            if EmployeeValidator.validate_role(role):
                return role
            print("❌ Invalid role. Cannot be empty.")

    @staticmethod
    def get_auth_data() -> Tuple[str, str]:
        username = input("Username: ")
        password = getpass("Password: ")
        while True:
            if EmployeeValidator.validate_username(username) and Password.validate(password):
                return username, password
            print('❌ Invalid username or password. Username >= 4, Password >= 6 characters.\n')
