from typing import List, Tuple


class Category:
    STUDENT = 'student'
    TEACHER = 'teacher'
    VISITOR = 'visitor'

    # TODO: Lição 13 Módulo de coleções: listas, tuplas, conjuntos e dicionários
    _TRANSLATIONS = {
        STUDENT: 'estudante',
        TEACHER: 'professor',
        VISITOR: 'visitante'
    }

    @staticmethod
    def validate(category: str) -> bool:
        valid_categories = {Category.STUDENT, Category.TEACHER, Category.VISITOR}
        return category in valid_categories

    @staticmethod
    def translate(category: str) -> str:
        return Category._TRANSLATIONS.get(category.lower(), 'Unknown Category')

    @staticmethod
    def options() -> List[Tuple[str, str]]:
        return list(Category._TRANSLATIONS.items())
