from typing import List

from model.customer import Customer
from model.customer_dao import CustomerDao
from model.exceptions import CustomerNotFoundError


class CustomerRepository:

    @staticmethod
    def get_all_customers() -> List[Customer]:
        """Load all customers from DAO (active and deleted)"""
        return CustomerDao.load_all()

    @staticmethod
    def get_customer_by_cpf(cpf: str) -> Customer:
        customers = CustomerRepository.get_all_customers()
        customer = next((c for c in customers if str(c.cpf) == cpf), None)
        if customer is None:
            raise CustomerNotFoundError(f"Customer with cpf {cpf} not found.")
        return customer
