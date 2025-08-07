class Password:

    _LENGTH = 6

    @staticmethod
    def validate(password: str) -> bool:
        return len(password) >= Password._LENGTH
