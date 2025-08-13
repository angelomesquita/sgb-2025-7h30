import bcrypt
from model.employee import Employee


class Auth:

    @staticmethod
    def hash_password(password: str) -> bytes:
        password_bytes = password.encode('utf-8')
        return bcrypt.hashpw(password_bytes, bcrypt.gensalt())

    @staticmethod
    def verify_password(password: str, password_hash: str) -> bool:
        if isinstance(password_hash, str):
            password_hash = password_hash.encode('utf-8')
        return bcrypt.checkpw(password.encode('utf-8'), password_hash)

    @staticmethod
    def auth(employee: Employee, username: str, password: str) -> bool:
        return employee.username == username and Auth.verify_password(password, employee.password_hash)
