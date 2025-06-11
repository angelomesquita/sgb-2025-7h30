import os
from controller.auth_controller import AuthController
from controller.employee_controller import EmployeeController
from model.cpf import Cpf
from model.password import Password
from typing import Tuple


def show_menu() -> None:  # Procedimento porque NÃO retorna valor
    clear_screen()
    print('\n=== Library Management System ===')  # Sistema Gerenciador de Biblioteca
    print('1. Register Employee')  # Registrar Funcionário
    print('2. List Employees')  # Listar Funcionários
    print('3. Authenticate Employee')  # Autenticar Funcionário
    print('4. Update Employee')  # Atualizar Funcionário
    print('5. Delete Employee')  # Deletar Funcionário
    print('6. Restore Employee')  # Restaurar Funcionário
    print('0. Exit')  # Sair


def register_employee(controller: EmployeeController) -> None:
    print("\n=== Register Employee ===")
    data = get_employee_data()
    controller.register(*data)
    press_enter_to_continue()


def list_employees(controller: EmployeeController) -> None:
    print('\n=== List Employees ===')
    controller.list()
    press_enter_to_continue()


def authenticate_employee(controller: EmployeeController) -> None:
    print("\n=== Authenticate Employee ===")
    username, password = get_auth_data()
    AuthController.auth(controller.employees, username, password)
    press_enter_to_continue()


def update_employee(controller: EmployeeController) -> None:
    print('\n=== Update Employee ===')
    cpf = get_cpf_data()
    employee = controller.find(cpf)
    if employee:
        data = get_employee_data()
        controller.update(*data)
    else:
        employee_not_found()
    press_enter_to_continue()


def delete_employee(controller: EmployeeController) -> None:
    print('\n=== Delete Employee ===')
    cpf = get_cpf_data()
    employee = controller.find(cpf)
    if employee:
        controller.delete(cpf)
    else:
        employee_not_found()
    press_enter_to_continue()


def restore_employee(controller: EmployeeController) -> None:
    print('\n=== Restore Employee ===')
    cpf = get_cpf_data()
    employee = controller.find_deleted(cpf)
    if employee:
        controller.restore(cpf)
    else:
        employee_not_found()
    press_enter_to_continue()


def get_employee_data() -> Tuple[str, str, str, str, str]:  # Função porque retorna valor
    name = input("Name: ")
    cpf = get_cpf_data()
    role = input("Role: ")
    username, password = get_auth_data()
    return name, cpf, role, username, password


def get_auth_data() -> Tuple[str, str]:
    username = input("Username: ")
    while True:
        password = input("Password: ")
        if Password.validate(password):
            return username, password
        print('Invalid Password. Try again.\n')


def get_cpf_data() -> str:
    while True:
        cpf = input("CPF: ")
        if Cpf.validate(cpf):
            return cpf
        print('Invalid CPF. Try again.\n')


def clear_screen() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')


def press_enter_to_continue() -> None:
    input('Press Enter to continue...')


def employee_not_found() -> None:
    print('Employee not found.\n')
