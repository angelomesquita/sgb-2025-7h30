from model.auth import Auth


class AuthController:

    @staticmethod
    def auth(employees, username, password):
        for employee in employees:
            if Auth.auth(employee, username, password) and employee.deleted is not True:
                print(f"Welcome, {employee.name}")
                return True
        print("Authentication failed.")
        return False
