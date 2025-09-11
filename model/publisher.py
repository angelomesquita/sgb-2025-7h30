class Publisher:

    def __init__(self, legal_name: str, city: str, state: str, deleted: bool = False):
        self._legal_name = legal_name
        self._city = city
        self._state = state
        self._deleted = deleted

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

    def __str__(self):
        return f"Legal Name: {self.legal_name}, City: {self.city} - State: {self.state}"
