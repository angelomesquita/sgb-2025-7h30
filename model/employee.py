class Employee:

    # TODO: apply encapsulation by converting attributes to private or protected instead of public

    def __init__(self, name, cpf, role, username, password_hash):
        self.name = name
        self.cpf = cpf
        self.role = role
        self.username = username
        self.password_hash = password_hash
        self.deleted = False

    def __str__(self):
        return f'Name: {self.name}, CPF: {self.cpf}, Role: {self.role}, Login: {self.username}'
