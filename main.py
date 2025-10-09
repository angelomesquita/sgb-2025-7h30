from view.author_view import AuthorView
from view.book_view import BookView
from view.borrow_view import BorrowView
from view.employee_view import EmployeeView
from view.customer_view import CustomerView
from view.publisher_view import PublisherView
from view.view import View


def main():
    show_app_menu()


def option_1() -> None:
    author_view = AuthorView()
    author_view.show_menu()
    View.clear_screen()


def option_2() -> None:
    borrow_view = BorrowView()
    borrow_view.show_menu()
    View.clear_screen()


def option_3() -> None:
    book_view = BookView()
    book_view.show_menu()
    View.clear_screen()


def option_4() -> None:
    employee_view = EmployeeView()
    employee_view.show_menu()
    View.clear_screen()


def option_5() -> None:
    customer_view = CustomerView()
    customer_view.show_menu()
    View.clear_screen()


def option_6() -> None:
    publisher_view = PublisherView()
    publisher_view.show_menu()
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
    '4': option_4,
    '5': option_5,
    '6': option_6,
    '0': option_0
}


def show_app_menu() -> None:
    running = True
    while running:
        EmployeeView.clear_screen()
        print('\n=== Library Management System ===')
        print('1. Author Module')
        print('2. Book Module')
        print('3. Borrow Module')
        print('4. Employee Module')
        print('5. Customer Module')
        print('6. Publisher Module')
        print('0. Exit')

        option = input('Select an option: ')
        action = menu_actions.get(option, invalid_option)
        result = action()
        running = result if result is not None else True


if __name__ == '__main__':
    main()
