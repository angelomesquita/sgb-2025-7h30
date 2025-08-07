import bcrypt
from model.employee import Employee


class Auth:

    @staticmethod
    def hash_password(password: str) -> str:
        password_bytes = password.encode('utf-8')
        return str(bcrypt.hashpw(password_bytes, bcrypt.gensalt()))

    @staticmethod
    def verify_password(password: str, password_hash: str) -> bool:
        return bcrypt.checkpw(password.encode('utf-8'), bytes(password_hash))

    @staticmethod
    def auth(employee: Employee, username: str, password: str) -> bool:
        return employee.username == username and Auth.verify_password(password, employee.password_hash)
