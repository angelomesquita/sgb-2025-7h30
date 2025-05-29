import os


def show_menu():
    clear_screen()
    print('\n=== Library Management System ===')  # Sistema Gerenciador de Biblioteca
    print('1. Register Employee')  # Registrar Funcionário
    print('2. List Employees')  # Listar Funcionários
    print('3. Authenticate Employee')  # Autenticar Funcionário
    print('4. Update Employee') # Atualizar Funcionário
    print('0. Exit')  # Sair


def update_employee(controller):
    print('\n=== Update Employee ===')
    cpf = get_cpf_data()
    employee = controller.find(cpf)
    if employee:
        data = get_employee_data()
        controller.update(*data)
    prees_enter_to_continue()


def get_employee_data():
    name = input("Name: ")
    cpf = get_cpf_data()
    role = input("Role: ")
    username, password = get_auth_data()
    return name, cpf, role, username, password


def get_auth_data():
    username = input("Username: ")
    password = input("Password: ")
    return username, password


def get_cpf_data():
    cpf = input("CPF: ")
    return cpf


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def prees_enter_to_continue():
    input('Press Enter to continue...')
