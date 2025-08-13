from view.employee_view import EmployeeView
from view.customer_view import CustomerView


def main():
    show_app_menu()


def option_1() -> None:
    employee_view = EmployeeView()
    employee_view.show_menu()
    EmployeeView.clear_screen()


def option_2() -> None:
    customer_view = CustomerView()
    customer_view.show_menu()
    CustomerView.clear_screen()
    print('Menu do módulo de usuário')


def option_0() -> False:
    print('Exiting the system.')  # saindo do sistema
    return False


def invalid_option() -> True:
    print('Invalid option.')  # Opção Inválida
    EmployeeView.press_enter_to_continue()
    return True  # continuar no loop


# TODO: Lição 13 Módulo de coleções: listas, tuplas, conjuntos e dicionários
menu_actions = {
    '1': option_1,
    '2': option_2,
    '0': option_0
}


def show_app_menu() -> None:
    running = True
    while running:
        EmployeeView.clear_screen()
        print('\n=== Library Management System ===')  # Sistema Gerenciador de Bibliotecas
        print('1. Employee Module')  # Módulo Funcionários
        print('2. Customer Module')  # Módulo Usuário (Estudante, Professor ou Visitante)
        print('0. Exit')  # Sair do Sistema

        option = input('Select an option: ')
        action = menu_actions.get(option, invalid_option)
        result = action()
        running = result if result is not None else True


if __name__ == '__main__':
    main()
