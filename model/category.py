class Category:
    STUDENT = 'student'
    TEACHER = 'teacher'
    VISITOR = 'visitor'

    @staticmethod
    def validate(category: str) -> bool:
        valid_categories = {Category.STUDENT, Category.TEACHER, Category.VISITOR}
        return category in valid_categories
