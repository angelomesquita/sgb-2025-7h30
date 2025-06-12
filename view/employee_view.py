import os
from controller.auth_controller import AuthController
from controller.employee_controller import EmployeeController
from model.cpf import Cpf
from model.password import Password
from typing import Tuple


class EmployeeView:

    __EMPLOYEE_NOT_FOUND = 'Employee not found.\n'
    __INVALID_OPTION = 'Invalid option\n'

    def __init__(self):
        self.controller = EmployeeController()

    def show_menu(self) -> None:  # método
        while True:
            self.clear_screen()

            print('\n=== Library Management System ===')  # Sistema Gerenciador de Biblioteca
            print('1. Register Employee')  # Registrar Funcionário
            print('2. List Employees')  # Listar Funcionários
            print('3. Authenticate Employee')  # Autenticar Funcionário
            print('4. Update Employee')  # Atualizar Funcionário
            print('5. Delete Employee')  # Deletar Funcionário
            print('6. Restore Employee')  # Restaurar Funcionário
            print('0. Back to main menu')  # Voltar para o Menu Principal

            option = input('Select an option: ')

            if option == '1':
                self.register()
            elif option == '2':
                self.list()
            elif option == '3':
                self.authenticate()
            elif option == '4':
                self.update()
            elif option == '5':
                self.delete()
            elif option == '6':
                self.restore()
            elif option == '0':
                break
            else:
                print(self.__INVALID_OPTION) # Opção Inválida
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
        AuthController.auth(self.controller.employees, username, password)
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

    def get_employee_data(self) -> Tuple[str, str, str, str, str]:  # Método
        name = input("Name: ")
        cpf = self.get_cpf_data()
        role = input("Role: ")
        username, password = self.get_auth_data()
        return name, cpf, role, username, password

    def get_auth_data(self) -> Tuple[str, str]:
        username = input("Username: ")
        while True:
            password = input("Password: ")
            if Password.validate(password):
                return username, password
            print('Invalid Password. Try again.\n')

    def get_cpf_data(self) -> str:
        while True:
            cpf = input("CPF: ")
            if Cpf.validate(cpf):
                return cpf
            print('Invalid CPF. Try again.\n')

    @staticmethod
    def clear_screen() -> None:
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def press_enter_to_continue() -> None:
        input('Press Enter to continue...')
