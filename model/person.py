class Person:

    def __init__(self, name: str, cpf: str, password_hash: str, deleted: bool = False):
        self._name = name
        self._cpf = cpf
        self._password_hash = password_hash
        self._deleted = deleted

    #  Getters and Setters
    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        self._name = value

    @property
    def cpf(self) -> str:
        return self._cpf

    @cpf.setter
    def cpf(self, value: str) -> None:
        self._cpf = value

    @property
    def password_hash(self) -> str:
        return self._password_hash

    @password_hash.setter
    def password_hash(self, value: str) -> None:
        self._password_hash = value

    @property
    def deleted(self) -> bool:
        return self._deleted

    @deleted.setter
    def deleted(self, value: str) -> None:
        self._deleted = value
