class Publisher:

    def __init__(self, publisher_id: str, legal_name: str, city: str, state: str, deleted: bool = False):
        self._publisher_id = publisher_id
        self._legal_name = legal_name
        self._city = city
        self._state = state
        self._deleted = deleted

    @property
    def publisher_id(self) -> str:
        return self._publisher_id

    @publisher_id.setter
    def publisher_id(self, value: str) -> None:
        self._publisher_id = value

    @property
    def legal_name(self) -> str:
        return self._legal_name

    @legal_name.setter
    def legal_name(self, value: str) -> None:
        self._legal_name = value

    @property
    def city(self) -> str:
        return self._city

    @city.setter
    def city(self, value: str) -> None:
        self._city = value

    @property
    def state(self) -> str:
        return self._state

    @state.setter
    def state(self, value: str) -> None:
        self._state = value

    @property
    def deleted(self) -> bool:
        return self._deleted

    @deleted.setter
    def deleted(self, value: str) -> None:
        self._deleted = value

    def __str__(self):
        return f"ID: {self.publisher_id}, Legal Name: {self.legal_name}, City: {self.city} - State: {self.state}"
