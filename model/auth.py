import bcrypt
from model.employee import Employee
from model.logger import auth_logger
from model.exceptions import AuthenticationError


class Auth:

    @staticmethod
    def hash_password(password: str) -> str:
        """Hashes a password using bcrypt"""
        try:
            password_bytes = password.encode('utf-8')
            hashed = bcrypt.hashpw(password_bytes, bcrypt.gensalt()).decode('utf-8')
            auth_logger.debug("Password hashed successfully.")
            return hashed
        except Exception as error:
            auth_logger.error(f"Error hashing password: {error}")
            raise

    @staticmethod
    def verify_password(password: str, password_hash: str) -> bool:
        """Verifies a plain password against a bcrypt hash."""
        try:
            valid = bcrypt.checkpw(password.encode('utf-8'), password_hash.encode('utf-8'))
            auth_logger.debug(f"Password verification result {valid}")
            return valid
        except Exception as error:
            auth_logger.error(f"Error verifying password: {error}")
            raise

    @staticmethod
    def auth(employee: Employee, username: str, password: str) -> bool:
        """
        Authenticates an employee using username and password.
        Raises AuthenticationError if credentials are invalid.
        """
        try:
            if employee.username != username or not Auth.verify_password(password, employee.password_hash):
                auth_logger.warning(f"Failed login attempt for username: {username}")
                raise AuthenticationError(f"Invalid credentials for username: {username}")
            auth_logger.info(f"Employee authenticated successfully: {username}")
            return True
        except AuthenticationError:
            raise
        except Exception as error:
            auth_logger.error(f"Unexpected error during authentication: {error}")
            raise
