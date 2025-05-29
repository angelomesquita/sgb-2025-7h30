from model.auth import Auth
from model.employee import Employee


class EmployeeController:
    def __init__(self):
        self.employees = []

    def register(self, name, cpf, role, username, password):
        password_hash = Auth.hash_password(password)
        employee = Employee(name, cpf, role, username, password_hash)
        self.employees.append(employee)
        print('Employee successfully registered!')

    def list(self):
        if not self.employees:
            print("No employees registered yet.")
            return
        for employee in self.employees:
            print(employee)

    def find(self, cpf):
        for employee in self.employees:
            if employee.cpf == cpf:
                return employee
        print('Employee not found.\n')
        return None

    def update(self, name, cpf, role, username, password):
        for employee in self.employees:
            if employee.cpf == cpf:
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
