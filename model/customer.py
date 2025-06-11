class Customer:

    # TODO: apply encapsulation by converting attributes to private or protected instead of public

    def __init__(self, name: str, cpf: str, contact: str, category: str, password_hash: str):
        # TODO Is customer equals to Employee?
        self.name = name
        self.cpf = cpf
        self.contact = contact
        self.category = category  # student, teacher, visitor
        self.password_hash = password_hash
        self.deleted = False

    def __str__(self):
        return f'Name: {self.name}, CPF: {self.cpf}, Contact: {self.contact}, Category: {self.category}'
