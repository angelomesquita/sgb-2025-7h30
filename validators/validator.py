class Validator:

    @staticmethod
    def not_empty(value: str) -> bool:
        return len(value.strip()) > 0

    @staticmethod
    def min_length(value: str, length: int) -> bool:
        return len(value.strip()) >= length

    @staticmethod
    def is_numeric(value: str) -> bool:
        return value.isdigit()
