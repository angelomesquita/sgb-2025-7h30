from model.auth import Auth
from model.category import Category
from model.customer import Customer
from model.password import Password
from typing import Optional


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
        if not Password.validate(password):
            print('Invalid Password. Try again.\n')
            return
        password_hash = Auth.hash_password(password)
        customer = Customer(name, cpf, contact, category, password_hash)
        self.customers.append(customer)
        print('Customer successfully registered!')

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
