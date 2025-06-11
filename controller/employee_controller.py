from model.auth import Auth
from model.cpf import Cpf
from model.employee import Employee
from typing import Optional


class EmployeeController:
    def __init__(self):
        self.employees = []

    def register(self, name: str, cpf: str, role: str, username: str, password: str) -> None:
        if self.find(cpf):
            print('An Employee with this CPF is already registered!\n')
            return
        if self.find_deleted(cpf):
            print('An Employee with this CPF was previously deleted.\n')
            return
        password_hash = Auth.hash_password(password)
        if not Cpf.validate(cpf):
            print('Invalid CPF. Try again.\n')
            return
        employee = Employee(name, cpf, role, username, password_hash)
        self.employees.append(employee)
        print('Employee successfully registered!')

    def list(self) -> None:
        if not self.employees:
            print("No employees registered yet.")
            return
        active_employees = [emp for emp in self.employees if not getattr(emp, 'deleted', False)]
        if not active_employees:
            print("No active employees found")
            return
        for employee in active_employees:
            print(employee)

    def find(self, cpf: str) -> Optional[Employee]:
        for employee in self.employees:
            if employee.cpf == cpf and employee.deleted is not True:
                return employee
        return None

    def find_deleted(self, cpf: str) -> Optional[Employee]:
        for employee in self.employees:
            if employee.cpf == cpf and getattr(employee, 'deleted', False) is True:
                return employee
        return None

    def update(self, name: str, cpf: str, role: str, username: str, password: str) -> None:
        for employee in self.employees:
            if employee.cpf == cpf and employee.deleted is not True:
                if name is not None:
                    employee.name = name
                if role is not None:
                    employee.role = role
                if username is not None:
                    employee.username = username
                if password is not None:
                    employee.password_hash = Auth.hash_password(password)
                print(f'Employee {employee.name} successfully updated!\n')
                return
        self.__employee_not_found()

    def delete(self, cpf: str) -> None:
        for employee in self.employees:
            if employee.cpf == cpf and employee.deleted is not True:
                employee.deleted = True
                print('Employee successfully deleted!\n')
                return
        self.__employee_not_found()

    def restore(self, cpf: str) -> None:
        for employee in self.employees:
            if employee.cpf == cpf and employee.deleted is True:
                employee.deleted = False
                print('Employee successfully restored!\n')
                return
        self.__employee_not_found()

    @staticmethod
    def __employee_not_found() -> None:
        print('Employee not found.\n')
