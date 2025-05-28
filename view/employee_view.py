import os


def show_menu():
    clear_screen()
    print('\n=== Library Management System ===')  # Sistema Gerenciador de Biblioteca
    print('1. Register Employee')  # Registrar Funcionário
    print('2. List Employees')  # Listar Funcionários
    print('3. Authenticate Employee')  # Autenticar Funcionário
    print('0. Exit')  # Sair


def get_employee_data():
    name = input("Name: ")
    cpf = input("CPF: ")
    role = input("Role: ")
    username = input("Username: ")
    password = input("Password: ")
    return name, cpf, role, username, password


def get_auth_data():
    username = input("Username: ")
    password = input("Password: ")
    return username, password


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
