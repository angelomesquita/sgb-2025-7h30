from model.auth import Auth
from model.employee import Employee
from typing import Optional


class EmployeeController:
    def __init__(self):
        self.employees = []

    def register(self, name: str, cpf: str, role: str, username: str, password: str) -> None:
        if self.find(cpf):
            print('An Employee with this CPF is already registered!\n')
            return
        password_hash = Auth.hash_password(password)
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
        print('Employee not found!\n')

    def delete(self, cpf: str) -> None:
        for employee in self.employees:
            if employee.cpf == cpf and employee.deleted is not True:
                employee.deleted = True
                print('Employee successfully deleted!\n')
                return
        print('Employee not found!\n')
