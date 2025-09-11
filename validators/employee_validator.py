from validators.validator import Validator


class EmployeeValidator:

    @staticmethod
    def validate_name(name: str) -> bool:
        return Validator.min_length(name, 3)

    @staticmethod
    def validate_role(role: str) -> bool:
        return Validator.not_empty(role)

    @staticmethod
    def validate_username(username: str) -> bool:
        return Validator.min_length(username, 4)
