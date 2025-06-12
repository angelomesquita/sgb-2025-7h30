from view.employee_view import EmployeeView


def main():

    while True:
        show_app_menu()

        option = input('Select an option: ')

        if option == '1':
            employee_view = EmployeeView()
            employee_view.show_menu()
            EmployeeView.clear_screen()
        elif option == '2':
            #custormer_view = CustomerView()
            #custormer_view.show_menu()
            #CustomerView.clear_screen()
            print('Menu do módulo de usuário')
        elif option == '0':
            print('Exiting the system.') # Saindo do Sistema
            break
        else:
            print('Invalid option.') # Opção Inválida
            EmployeeView.press_enter_to_continue()


def show_app_menu():
    print('\n=== Library Management System ===')  # Sistema Gerenciador de Bibliotecas
    print('1. Employee Module')  # Módulo Funcionários
    print('2. Customer Module')  # Módulo Usuário (Estudante, Professor ou Visitante)
    print('0. Exit')  # Sair do Sistema


if __name__ == '__main__':
    main()
