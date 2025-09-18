from validators.validator import Validator


class AuthorValidator:

    @staticmethod
    def validate_author_id(author_id: str) -> bool:
        return Validator.is_numeric(author_id)

    @staticmethod
    def validate_name(name: str) -> bool:
        return Validator.min_length(name, 3)
