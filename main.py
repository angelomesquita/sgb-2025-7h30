from view.author_view import AuthorView
from view.employee_view import EmployeeView
from view.customer_view import CustomerView
from view.view import View


def main():
    show_app_menu()


def option_1() -> None:
    author_view = AuthorView()
    author_view.show_menu()
    View.clear_screen()


def option_2() -> None:
    employee_view = EmployeeView()
    employee_view.show_menu()
    View.clear_screen()


def option_3() -> None:
    customer_view = CustomerView()
    customer_view.show_menu()
    View.clear_screen()


def option_0() -> False:
    print('Exiting the system.')
    return False


def invalid_option() -> True:
    print('Invalid option.')
    View.press_enter_to_continue()
    return True


menu_actions = {
    '1': option_1,
    '2': option_2,
    '3': option_3,
    '0': option_0
}


def show_app_menu() -> None:
    running = True
    while running:
        EmployeeView.clear_screen()
        print('\n=== Library Management System ===')
        print('1. Author Module')
        print('2. Employee Module')
        print('3. Customer Module')
        print('0. Exit')

        option = input('Select an option: ')
        action = menu_actions.get(option, invalid_option)
        result = action()
        running = result if result is not None else True


if __name__ == '__main__':
    main()
