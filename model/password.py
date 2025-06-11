class Password:

    @staticmethod
    def validate(password: str) -> bool:
        return len(password) >= 6

