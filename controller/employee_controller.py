import bcrypt
from model.employee import Employee


class EmployeeController:
    def __init__(self):
        self.employees = []

    def register(self, name, cpf, role, username, password):
        password_hash = self.__hash_password(password)
        employee = Employee(name, cpf, role, username, password_hash)
        self.employees.append(employee)
        print('Employee successfully registered!')

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
                    employee.password_hash = self.__hash_password(password)
                print(f'Employee {employee.name} successfully updated!\n')
                return
        print('Employee not found!\n')

    def list(self):
        if not self.employees:
            print("No employees registered yet.")
            return
        print("\n=== List of Employees ===")
        for employee in self.employees:
            print(employee)

    def __hash_password(self, password):
        password_bytes = password.encode('utf-8')
        return bcrypt.hashpw(password_bytes, bcrypt.gensalt())

    def auth(self, username, password):
        for employee in self.employees:
            if employee.username == username and self.__verify_password(password, employee.password_hash):
                print(f"Welcome, {employee.name}")
                return True
        print("Authentication failed.")
        return False

    def __verify_password(self, password, password_hash):
        return bcrypt.checkpw(password.encode('utf-8'), password_hash)
