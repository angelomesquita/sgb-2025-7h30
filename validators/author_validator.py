from typing import Iterable

from model.author import Author
from validators.validator import Validator


class AuthorValidator:

    @staticmethod
    def validate_author_id(author_id: str) -> bool:
        return Validator.is_numeric(author_id)

    @staticmethod
    def validate_name(name: str) -> bool:
        return Validator.min_length(name, 3)

    @staticmethod
    def validate_unique_name(name: str, authors: Iterable[Author]) -> bool:
        normalized_name = name.strip().lower()
        existing_names = set(a.name.strip().lower() for a in authors if not a.deleted)
        return normalized_name not in existing_names
