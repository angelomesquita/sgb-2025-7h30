from typing import Optional

from model.auth import Auth
from model.category import Category
from model.customer import Customer


class CustomerController:
    def __init__(self):
        self.customers = []  # TODO: Lição 10 - Python: Trabalhando com I/O

    def register(self, name: str, cpf: str, contact: str, category: str, password: str) -> None:
        if self.find(cpf):
            print('An Customer with this CPF is already registered!\n')
            return
        if self.find_deleted(cpf):
            print('An Customer with this CPF was previously deleted.\n')
            return
        if not Category.validate(category):
            print('Invalid category. Try again.')
            return
        password_hash = Auth.hash_password(password)
        customer = Customer(name, cpf, contact, category, str(password_hash))
        self.customers.append(customer)
        print('✅ Customer successfully registered!')

    def list(self) -> None:
        if not self.customers:
            print("No customers registered yet.")
            return
        actives_customers = [customer for customer in self.customers if not getattr(customer, 'deleted', False)]
        if not actives_customers:
            print("No active customers found.")
            return
        for customer in actives_customers:
            print(customer)

    def find(self, cpf: str) -> Optional[Customer]:
        for customer in self.customers:
            if customer.cpf == cpf and customer.deleted is not True:
                return customer
        return None

    def find_deleted(self, cpf: str) -> Optional[Customer]:
        for customer in self.customers:
            if customer.cpf == cpf and getattr(customer, 'deleted', False) is True:
                return customer
        return None

    def update(self, name: str, cpf: str, contact: str, category: str, password: str) -> None:
        for customer in self.customers:
            if customer.cpf == cpf and customer.deleted is not True:
                if name is not None:
                    customer.name = name
                if contact is not None:
                    customer.contact = contact
                if category is not None:
                    customer.category = category
                if password is not None:
                    customer.password_hash = Auth.hash_password(password)
                print('Customer successfully updated!\n')
                return
            self.__customer_not_found()

    def delete(self, cpf: str) -> None:
        for customer in self.customers:
            if customer.cpf == cpf and customer.deleted is not True:
                customer.deleted = True
                print('Customer successfully deleted!\n')
                return
        self.__customer_not_found()

    def restore(self, cpf: str) -> None:
        for customer in self.customers:
            if customer.cpf == cpf and customer.deleted is True:
                customer.deleted = False
                print('Customer successfully restored!\n')
                return
        self.__customer_not_found()

    @staticmethod
    def __customer_not_found() -> None:
        print('Customer not found.\n')
