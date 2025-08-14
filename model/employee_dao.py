from model.base_dao import BaseDao
from model.employee import Employee


class EmployeeDao(BaseDao[Employee]):

    _FILE_PATH = 'employees.txt'

    @staticmethod
    def _serialize(e: Employee) -> str:
        return f"{e.name}|{e.cpf}|{e.role}|{e.username}|{e.password_hash}|{e.deleted}"

    @staticmethod
    def _deserialize(data: str) -> Employee:
        name, cpf, role, username, password_hash, deleted = data.split("|")
        employee = Employee(name, cpf, role, username, password_hash, deleted)
        employee.deleted = deleted.lower() == "true"

        return employee
