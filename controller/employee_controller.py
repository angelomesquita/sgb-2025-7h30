from controller.base_controller import BaseController
from model.employee import Employee
from model.employee_dao import EmployeeDao
from model.logger import employee_logger


class EmployeeController(BaseController[Employee]):

    dao_class = EmployeeDao
    logger = employee_logger

    def register(self, name: str, cpf: str, role: str, username: str, password: str) -> None:
        super().register(cpf, name=name, role=role, username=username, password=password)

    def create_instance(self, name: str, cpf: str, role: str, username: str, password_hash: str, deleted: bool = False) -> Employee:
        return Employee(name, cpf, role, username, password_hash, deleted)

    def update(self, name: str, cpf: str, role: str, username: str, password: str) -> None:
        super().update(cpf, name=name, role=role, username=username, password=password)
