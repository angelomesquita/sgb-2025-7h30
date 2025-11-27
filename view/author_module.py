import tkinter as tk

from tkinter import ttk, messagebox

from controller.author_controller import AuthorController
from validators.author_validator import AuthorValidator


class AuthorModule(tk.Toplevel):

    def __init__(self, parent):
        super().__init__(parent)

        self.controller = AuthorController()
        self.style = ttk.Style()

        self.entry_id = None
        self.entry_name = None
        self.tree = None
        self.selected_author_id = None

        self.create_window()
        self.config_style()
        self.create_widgets()
        self.bind_events()
        self.load_authors()

    def create_window(self):
        self.title("Author Module")
        self.geometry("600x400")
        self.resizable(False, False)
        self.style.theme_use("clam")

    def config_style(self):
        self.style.configure("Valid.TEntry", fieldbackground="white")
        self.style.configure("Invalid.TEntry", fieldbackground="#ffcccc")
        self.style.configure("Treeview.Heading", font=("Segoe UI", 10, "bold"))
        self.style.configure("TButton", padding=0)

    def create_widgets(self):
        ttk.Label(self, text="Manage Authors", font=("Segoe UI", 14, "bold")).pack(pady=(10, 5))

        form_frame = ttk.LabelFrame(self, text="Author Form")
        form_frame.pack(fill="x", padx=15, pady=15)

        ttk.Label(form_frame, text="Author ID:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.entry_id = ttk.Entry(form_frame, width=40)
        self.entry_id.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(form_frame, text="Name:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.entry_name = ttk.Entry(form_frame, width=40)
        self.entry_name.grid(row=1, column=1, padx=5, pady=5)

        button_frame = ttk.Frame(self)
        button_frame.pack(pady=15)
        ttk.Button(button_frame, text="Register", command=self.register_author).grid(row=0, column=0, padx=6)
        ttk.Button(button_frame, text="Update", command=self.update_author).grid(row=0, column=1, padx=6)
        ttk.Button(button_frame, text="Delete", command=self.delete_author).grid(row=0, column=2, padx=6)
        ttk.Button(button_frame, text="Clear", command=self.clear_form).grid(row=0, column=3, padx=6)
        ttk.Button(button_frame, text="Close", command=self.destroy).grid(row=0, column=4, padx=6)

        list_frame = ttk.LabelFrame(self, text="Author List")
        list_frame.pack(fill="both", expand=True, padx=15, pady=15)

        self.tree = ttk.Treeview(
            list_frame,
            columns=("id", "name"),
            show="headings",
            height=8
        )
        self.tree.heading("id", text="Author ID")
        self.tree.heading("name", text="Name")
        self.tree.column("id", width=100, anchor="center")
        self.tree.column("name", width=300, anchor="w")
        self.tree.pack(fill="both", expand=True, padx=5, pady=5)

        self.tree.bind("<<TreeviewSelect>>", self.on_select_author)

    def bind_events(self):
        self.entry_id.bind("<KeyRelease>", self.validate_entry_id)
        self.entry_name.bind("<KeyRelease>", self.validate_entry_name)
        self.entry_name.bind("<Return>", lambda e: self.register_author())

    def validate_entry_id(self, event):
        value = event.widget.get().strip()
        style = "Valid.TEntry" if AuthorValidator.validate_author_id(value) else "Invalid.TEntry"
        self.entry_id.config(style=style)

    def validate_entry_name(self, event):
        value = event.widget.get().strip()
        style = "Valid.TEntry" if AuthorValidator.validate_name(value) else "Invalid.TEntry"
        self.entry_name.config(style=style)

    def register_author(self):
        author_id = self.entry_id.get().strip()
        name = self.entry_name.get().strip()

        if not AuthorValidator.validate_author_id(author_id):
            messagebox.showerror("Validation Error", "Invalid Author ID. Must be numeric.", parent=self)
            return

        if not AuthorValidator.validate_name(name):
            messagebox.showerror("Validation Error", "Name must be at least 3 characters.", parent=self)
            return

        try:
            self.controller.register(author_id=author_id, name=name)
            messagebox.showinfo("Success", f"Author: '{name}' registered successfully.", parent=self)
            self.load_authors()
            self.clear_form()
        except Exception as e:
            messagebox.showerror("Error", str(e), parent=self)

    def update_author(self):
        if not self.selected_author_id:
            messagebox.showwarning("Warning", "Select an author to update.", parent=self)
            return

        name = self.entry_name.get().strip()
        if not AuthorValidator.validate_name(name):
            messagebox.showerror("Validation Error", "Name must be at least 3 characters.", parent=self)
            return

        try:
            self.controller.update(author_id=self.selected_author_id, name=name)
            messagebox.showinfo("Success", "Author updated successfully.", parent=self)
            self.load_authors()
            self.clear_form()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def delete_author(self):
        if not self.selected_author_id:
            messagebox.showwarning("Warning", "Select an author to delete.", parent=self)
            return

        # books = BookRepository.search(author=self.entry_name.get().strip())
        # if books:
            # TODO: implements messagebox warning
            # TODO: implements book delete cascade

        confirm = messagebox.askyesno("Confirm Delete", "Are you sure you to delete this author?", parent=self)
        if not confirm:
            return

        try:
            self.controller.delete(self.selected_author_id)
            messagebox.showinfo("Success", "Author deleted successfully.", parent=self)
            self.load_authors()
            self.clear_form()
        except Exception as e:
            messagebox.showerror("Error", str(e), parent=self)

    def load_authors(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        try:
            authors = self.controller.list_all()
            for author in authors:
                self.tree.insert("", "end", values=(author.author_id, author.name))
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load authors: {e}", parent=self)

    def clear_form(self):
        self.entry_id.delete(0, tk.END)
        self.entry_name.delete(0, tk.END)
        self.entry_id.focus_set()

    def on_select_author(self, event):
        selected = event.widget.selection()
        if not selected:
            return

        values = self.tree.item(selected[0], "values")
        self.selected_author_id = values[0]

        self.entry_id.delete(0, tk.END)
        self.entry_name.delete(0, tk.END)

        self.entry_id.insert(0, values[0])
        self.entry_name.insert(0, values[1])
