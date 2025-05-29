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
        active_employees = [emp for emp in self.employees if not getattr(emp, 'deleted', False)]
        if not active_employees:
            print("No active employees found")
            return
        for employee in active_employees:
            print(employee)

    def find(self, cpf):
        for employee in self.employees:
            if employee.cpf == cpf and employee.deleted is not True:
                return employee
        print('Employee not found.\n')
        return None

    def update(self, name, cpf, role, username, password):
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

    def delete(self, cpf):
        for employee in self.employees:
            if employee.cpf == cpf and employee.deleted is not True:
                employee.deleted = True
                print('Employee successfully deleted!\n')
                return
        print('Employee not found!\n')
