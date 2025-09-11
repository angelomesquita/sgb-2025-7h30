from validators.validator import Validator


class AuthorValidator:

    @staticmethod
    def validate_name(name: str) -> bool:
        return Validator.min_length(name, 15)
