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

    #TODO: def list():

    def __hash_password(self, password):
        password_bytes = password.encode('utf-8')
        return bcrypt.hashpw(password_bytes, bcrypt.gensalt())

    #TODO: def auth(self, username, passoword):

    #TODO: def __verify_password(self, password, password_hash):
