from model.employee import Employee


class EmployeeController:
    def __init__(self):
        self.employess = []

    def register(self, name, cpf, role, username, password):
        password_hash = self.__hash_password(password)
        employee = Employee(name, cpf, role, username, password_hash)
        self.employess.append(employee)
        print('Employee successfuly regitered!')

    #TODO: def list():

    def __hash_password(self, password):
        return password
        #TODO
        #password_bytes = password.encode('utf-8')
        #salt =

    #TODO: def auth(self, username, passoword):

    #TODO: def __verify_password(self, password, password_hash):
