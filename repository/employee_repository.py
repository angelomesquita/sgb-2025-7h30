from typing import List

from model.employee import Employee
from model.employee_dao import EmployeeDao
from model.exceptions import EmployeeNotFoundError


class EmployeeRepository:

    @staticmethod
    def get_all_employees() -> List[Employee]:
        """Load all employees from DAO (active and deleted)"""
        return EmployeeDao.load_all()

    @staticmethod
    def get_employee_by_cpf(cpf: str) -> Employee:
        employees = EmployeeRepository.get_all_employees()
        employee = next((e for e in employees if str(e.cpf) == cpf), None)
        if employee is None:
            raise EmployeeNotFoundError(f"Employee with cpf {cpf} not found.")
        return employee
