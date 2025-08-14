from model.person import Person


class Employee(Person):

    def __init__(self, name: str, cpf: str, role: str, username: str, password_hash: str, deleted: bool = False):
        super().__init__(name, cpf, password_hash, deleted)
        self._role = role
        self._username = username

    @property
    def role(self) -> str:
        return self._role

    @role.setter
    def role(self, value: str) -> None:
        self._role = value

    @property
    def username(self) -> str:
        return self._username

    @username.setter
    def username(self, value: str) -> None:
        self._username = value

    def __str__(self):
        return f'Name: {self.name}, CPF: {self.cpf}, Role: {self.role}, Login: {self.username}'
