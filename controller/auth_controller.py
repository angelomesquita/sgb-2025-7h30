from model.auth import Auth
from model.logger import auth_logger
from model.exceptions import AuthenticationError
from model.employee import Employee
from typing import List


class AuthController:

    @staticmethod
    def auth(employees: List[Employee], username: str, password: str) -> bool:
        """
        Attempts to authenticate a user against a list of employees.
        Raises AuthenticationError if no valid employee is found or credentials are invalid.
        Log all authentication attempts.
        """
        try:
            for employee in employees:
                if employee.deleted is not True:
                    try:
                        if Auth.auth(employee, username, password):
                            auth_logger.info(f"Employee authenticated successfully: {employee.username}")
                            print(f"Welcome, {employee.name}")
                            return True
                    except AuthenticationError as error:
                        # Log a failed login attempt for this employee but continue checking others
                        auth_logger.warning(f"Failed login attempt for username: {username} - {error}")

            # If no employee matched, raise a generic authenticate failure.
            raise AuthenticationError(f"Authentication failed for username: {username}")
        except AuthenticationError as error:
            auth_logger.error(str(error))
            print("Authentication failed.")
            return False
        except Exception as error:
            auth_logger.error(f"Unexpected error during authentication: {error}")
            print("An unexpected error occurred during authentication.")
            return False
