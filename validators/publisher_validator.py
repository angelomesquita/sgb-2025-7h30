from validators.validator import Validator


class PublisherValidator:

    @staticmethod
    def validate_publisher_id(author_id: str) -> bool:
        return Validator.is_numeric(author_id)

    @staticmethod
    def validate_legal_name(legal_name: str) -> bool:
        return Validator.min_length(legal_name, 5)

    @staticmethod
    def validate_city(city: str) -> bool:
        return Validator.min_length(city, 5)

    @staticmethod
    def validate_state(state: str) -> bool:
        return Validator.length(state, 2)
