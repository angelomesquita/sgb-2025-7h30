import tkinter as tk
from tkinter import ttk, messagebox

from view.book_view import BookView
from view.borrow_view import BorrowView
from view.customer_view import CustomerView
from view.employee_view import EmployeeView


class LibraryApp(tk.Tk):

    _TITLE = "Library Management System"

    def __init__(self):
        super().__init__()

        self.configure_window()
        self.create_header()
        self.create_module_buttons()
        self.create_exit_button()

    def configure_window(self) -> None:
        self.title(self._TITLE)
        self.geometry("400x500")
        self.resizable(False, False)
        ttk.Style(self).theme_use("clam")

    def create_header(self) -> None:
        ttk.Label(self, text=self._TITLE, font=("Segoe UI", 16, "bold"), anchor="center").pack(pady=(30, 10))
        ttk.Separator(self, orient="horizontal").pack(fill="x", pady=10)

    def create_exit_button(self) -> None:
        ttk.Button(self, text="Exit", command=self.confirm_exit, width=30).pack(pady=(5, 20))

    def confirm_exit(self) -> None:
        if messagebox.askyesno("Confirm", "Do you really want to logout of the system?"):
            self.destroy()

    def create_module_buttons(self) -> None:
        button_frame = ttk.Frame(self)
        button_frame.pack(pady=20)

        modules = [
            ("Author Module", self.open_author_module),
            ("Book Module", self.open_book_module),
            ("Borrow Module", self.open_borrow_module),
            ("Employee Module", self.open_employee_module),
            ("Customer Module", self.open_customer_module),
            ("Publisher Module", self.open_publisher_module),
        ]
        for i, (text, command) in enumerate(modules, start=0):
            button = ttk.Button(button_frame, text=f"{text}", command=command, width=30)
            button.grid(row=i, column=0, pady=5, padx=20)
        ttk.Separator(self, orient="horizontal").pack(fill="x", pady=15)

    def open_author_module(self) -> None:
        from view.author_module import AuthorModule
        AuthorModule(self)

    def open_book_module(self) -> None:
        self._open_module_window("Book Module", BookView)

    def open_borrow_module(self) -> None:
        self._open_module_window("Borrow Module", BorrowView)

    def open_employee_module(self) -> None:
        self._open_module_window("Employee Module", EmployeeView)

    def open_customer_module(self) -> None:
        self._open_module_window("Customer Module", CustomerView)

    def open_publisher_module(self) -> None:
        from view.publisher_module import PublisherModule
        PublisherModule(self)

    def _open_module_window(self, title: str, view_module) -> None:
        try:
            window = tk.Toplevel(self)
            window.title(title)
            window.geometry("600x400")
            window.grab_set()
            window.focus_force()

            view = view_module()
            if hasattr(view, "show_menu"):
                ttk.Label(window, text=f"{title} (terminal mode)", font=("Segoe UI", 12)).pack(pady=30)
                ttk.Button(window, text="Run in terminal", command=view.show_menu).pack(pady=10)
            else:
                ttk.Label(window, text=f"{title} interface not implemented yet.").pack(pady=20)

        except Exception as e:
            messagebox.showerror("Error", f"Failed to open module:\n{e}")


if __name__ == "__main__":
    app = LibraryApp()
    app.mainloop()
