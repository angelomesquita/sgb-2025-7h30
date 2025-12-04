import tkinter as tk

from tkinter import ttk, messagebox

from controller.publisher_controller import PublisherController
from validators.publisher_validator import PublisherValidator


class PublisherModule(tk.Toplevel):

    def __init__(self, parent):
        super().__init__(parent)

        self.controller = PublisherController()
        self.style = ttk.Style()

        self.entry_id = None
        self.entry_legal_name = None
        self.entry_city = None
        self.entry_state = None
        self.tree = None
        self.selected_publisher_id = None

        self.create_window()
        self.config_style()
        self.create_widgets()
        self.bind_events()
        self.load_publishers()

    def create_window(self):
        self.title("Publisher Module")
        self.geometry("700x400")
        self.resizable(False, False)
        self.style.theme_use("clam")

    def config_style(self):
        self.style.configure("Valid.TEntry", fieldbackground="white")
        self.style.configure("Invalid.TEntry", fieldbackground="#ffcccc")
        self.style.configure("Treeview.Heading", font=("Segoe UI", 10, "bold"))
        self.style.configure("TButton", padding=0)

    def create_widgets(self):
        ttk.Label(self, text="Manage Publishers", font=("Segoe UI", 14, "bold")).pack(pady=(10, 5))

        form_frame = ttk.LabelFrame(self, text="Publisher Form")
        form_frame.pack(fill="x", padx=15, pady=15)

        ttk.Label(form_frame, text="Publisher ID:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.entry_id = ttk.Entry(form_frame, width=20)
        self.entry_id.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(form_frame, text="Legal Name:").grid(row=0, column=2, padx=5, pady=5, sticky="e")
        self.entry_legal_name = ttk.Entry(form_frame, width=20)
        self.entry_legal_name.grid(row=0, column=3, padx=5, pady=5)

        ttk.Label(form_frame, text="City:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.entry_city = ttk.Entry(form_frame, width=20)
        self.entry_city.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(form_frame, text="State:").grid(row=1, column=2, padx=5, pady=5, sticky="e")
        self.entry_state = ttk.Entry(form_frame, width=20)
        self.entry_state.grid(row=1, column=3, padx=5, pady=5)

        button_frame = ttk.Frame(self)
        button_frame.pack(pady=15)
        ttk.Button(button_frame, text="Register", command=self.register_publisher).grid(row=0, column=0, padx=6)
        ttk.Button(button_frame, text="Update", command=self.update_publisher).grid(row=0, column=1, padx=6)
        ttk.Button(button_frame, text="Delete", command=self.delete_publisher).grid(row=0, column=2, padx=6)
        ttk.Button(button_frame, text="Clear", command=self.clear_form).grid(row=0, column=3, padx=6)
        ttk.Button(button_frame, text="Close", command=self.destroy).grid(row=0, column=4, padx=6)

        list_frame = ttk.LabelFrame(self, text="Publisher List")
        list_frame.pack(fill="both", expand=True, padx=15, pady=15)

        self.tree = ttk.Treeview(
            list_frame,
            columns=("id", "legal_name", "city", "state"),
            show="headings",
            height=8
        )
        self.tree.heading("id", text="Publisher ID")
        self.tree.heading("legal_name", text="Legal Name")
        self.tree.heading("city", text="City")
        self.tree.heading("state", text="state")
        self.tree.column("id", width=120, anchor="center")
        self.tree.column("legal_name", width=300, anchor="w")
        self.tree.column("city", width=100, anchor="w")
        self.tree.column("state", width=50, anchor="w")
        self.tree.pack(fill="both", expand=True, padx=5, pady=5)

        self.tree.bind("<<TreeviewSelect>>", self.on_select_publisher)

    def bind_events(self):
        self.entry_id.bind("<KeyRelease>", self.validate_entry_id)
        self.entry_legal_name.bind("<KeyRelease>", self.entry_legal_name)
        self.entry_city.bind("<KeyRelease>", self.entry_city)
        self.entry_state.bind("<KeyRelease>", self.entry_state)
        self.entry_state.bind("<Return>", lambda e: self.register_publisher())

    def validate_entry_id(self, event):
        value = event.widget.get().strip()
        style = "Valid.TEntry" if PublisherValidator.validate_publisher_id(value) else "Invalid.TEntry"
        self.entry_id.config(style=style)

    def validate_entry_legal_name(self, event):
        value = event.widget.get().strip()
        style = "Valid.TEntry" if PublisherValidator.validate_legal_name(value) else "Invalid.TEntry"
        self.entry_legal_name.config(style=style)

    def validate_entry_city(self, event):
        value = event.widget.get().strip()
        style = "Valid.TEntry" if PublisherValidator.validate_city(value) else "Invalid.TEntry"
        self.entry_city.config(style=style)

    def validate_entry_state(self, event):
        value = event.widget.get().strip()
        style = "Valid.TEntry" if PublisherValidator.validate_state(value) else "Invalid.TEntry"
        self.entry_state.config(style=style)

    def register_publisher(self):
        publisher_id = self.entry_id.get().strip()
        legal_name = self.entry_legal_name.get().strip()
        city = self.entry_city.get().strip()
        state = self.entry_state.get().strip()

        if not PublisherValidator.validate_publisher_id(publisher_id):
            messagebox.showerror("Validation Error", "Invalid Publisher ID. Must be numeric.", parent=self)
            return

        if not PublisherValidator.validate_legal_name(legal_name):
            messagebox.showerror("Validation Error", "Legal name must be at least 5 characters.", parent=self)
            return

        if not PublisherValidator.validate_city(city):
            messagebox.showerror("Validation Error", "City must be at least 5 characters.", parent=self)
            return

        if not PublisherValidator.validate_state(state):
            messagebox.showerror("Validation Error", "State must be at least 2 characters.", parent=self)
            return

        try:
            self.controller.register(publisher_id=publisher_id, legal_name=legal_name, city=city, state=state)
            messagebox.showinfo("Success", f"Publisher: '{legal_name}' registered successfully.", parent=self)
            self.load_publishers()
            self.clear_form()
        except Exception as e:
            messagebox.showerror("Error", str(e), parent=self)

    def update_publisher(self):
        if not self.selected_publisher_id:
            messagebox.showwarning("Warning", "Select a publisher to update.", parent=self)
            return

        publisher_id = self.entry_id.get().strip()
        legal_name = self.entry_legal_name.get().strip()
        city = self.entry_city.get().strip()
        state = self.entry_state.get().strip()

        if not PublisherValidator.validate_publisher_id(publisher_id):
            messagebox.showerror("Validation Error", "Invalid Publisher ID. Must be numeric.", parent=self)
            return

        if not PublisherValidator.validate_legal_name(legal_name):
            messagebox.showerror("Validation Error", "Legal name must be at least 5 characters.", parent=self)
            return

        if not PublisherValidator.validate_city(city):
            messagebox.showerror("Validation Error", "City must be at least 5 characters.", parent=self)
            return

        if not PublisherValidator.validate_state(state):
            messagebox.showerror("Validation Error", "State must be at least 2 characters.", parent=self)
            return

        try:
            self.controller.update(publisher_id=publisher_id, legal_name=legal_name, city=city, state=state)
            messagebox.showinfo("Success", "Publisher updated successfully.", parent=self)
            self.load_publishers()
            self.clear_form()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def delete_publisher(self):
        if not self.selected_publisher_id:
            messagebox.showwarning("Warning", "Select a publisher to delete.", parent=self)
            return

        confirm = messagebox.askyesno("Confirm Delete", "Are you sure you to delete this publisher?", parent=self)
        if not confirm:
            return

        try:
            self.controller.delete(self.selected_publisher_id)
            messagebox.showinfo("Success", "Publisher deleted successfully.", parent=self)
            self.load_publishers()
            self.clear_form()
        except Exception as e:
            messagebox.showerror("Error", str(e), parent=self)

    def load_publishers(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        try:
            publishers = self.controller.list_all()
            for publisher in publishers:
                self.tree.insert("", "end", values=(publisher.publisher_id, publisher.legal_name, publisher.city, publisher.state))
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load publishers: {e}", parent=self)

    def clear_form(self):
        self.entry_id.delete(0, tk.END)
        self.entry_legal_name.delete(0, tk.END)
        self.entry_city.delete(0, tk.END)
        self.entry_state.delete(0, tk.END)
        self.entry_id.focus_set()

    def on_select_publisher(self, event):
        selected = event.widget.selection()
        if not selected:
            return

        values = self.tree.item(selected[0], "values")
        self.selected_publisher_id = values[0]

        self.entry_id.delete(0, tk.END)
        self.entry_legal_name.delete(0, tk.END)
        self.entry_city.delete(0, tk.END)
        self.entry_state.delete(0, tk.END)

        self.entry_id.insert(0, values[0])
        self.entry_legal_name.insert(0, values[1])
        self.entry_city.insert(0, values[2])
        self.entry_state.insert(0, values[3])
