from datetime import datetime
from validators.validator import Validator


class BookValidator:

    @staticmethod
    def validate_isbn(isbn: str) -> bool:
        return Validator.is_numeric(isbn)

    @staticmethod
    def validate_title(title: str) -> bool:
        return Validator.min_length(title, 5)

    @staticmethod
    def validate_year(year: int) -> bool:
        current_year = datetime.now().year
        return 0 < year <= current_year

    @staticmethod
    def validate_quantity(quantity: int) -> bool:
        return quantity > 0 and Validator.is_numeric(str(quantity)) and isinstance(quantity, int)
