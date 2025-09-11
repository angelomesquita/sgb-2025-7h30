class Author:

    def __init__(self, name: str, deleted: bool = False):
        self._name = name
        self._deleted = deleted

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        self._name = value

    def __str__(self):
        return f"Name: {self.name}"
