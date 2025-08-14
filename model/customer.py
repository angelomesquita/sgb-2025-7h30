from model.person import Person


class Customer(Person):

    def __init__(self, name: str, cpf: str, contact: str, category: str, password_hash: str, deleted: bool = False):
        super().__init__(name, cpf, password_hash, deleted)
        self._contact = contact
        self._category = category  # student, teacher, visitor

    @property
    def contact(self) -> str:
        return self._contact

    @contact.setter
    def contact(self, value: str) -> None:
        self._contact = value

    @property
    def category(self) -> str:
        return self._category

    @category.setter
    def category(self, value: str) -> None:
        self._category = value

    def __str__(self):
        return f'Name: {self.name}, CPF: {self.cpf}, Contact: {self.contact}, Category: {self.category}'
