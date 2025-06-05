from controller.employee_controller import EmployeeController
from view.employee_view import *


def main():
    controller = EmployeeController()

    while True:
        show_menu()
        option = input('Select an option: ')

        if option == '1':
            register_employee(controller)
        elif option == '2':
            list_employees(controller)
        elif option == '3':
            authenticate_employee(controller)
        elif option == '4':
            update_employee(controller)
        elif option == '5':
            delete_employee(controller)
        elif option == '6':
            restore_employee(controller)
        elif option == '0':
            print('Exiting the system.') # Saindo do Sistema
            break
        else:
            print('Invalid option.') # Opção Inválida
            press_enter_to_continue()


if __name__ == '__main__':
    main()
