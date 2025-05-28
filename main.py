from controller.employee_controller import EmployeeController
from view.employee_view import show_menu, get_employee_data, get_auth_data


def main():
    controller = EmployeeController()

    while True:
        show_menu()
        option = input('Select an option: ')

        if option == '1':
            print("\n=== Register Employee ===")
            data = get_employee_data()
            controller.register(*data)
            input('Press Enter to continue...')
        elif option == '2':
            controller.list()
            input('Press Enter to continue...')
        elif option == '3':
            print("\n=== Authenticate Employee ===")
            auth_data = get_auth_data()
            controller.auth(*auth_data)
            input('Press Enter to continue...')
        elif option == '0':
            print('Exiting the system.')
            break
        else:
            print('Invalid option.')
            input('Press Enter to continue...')


if __name__ == '__main__':
    main()
