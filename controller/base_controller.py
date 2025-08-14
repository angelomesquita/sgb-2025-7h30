from abc import ABC, abstractmethod
from typing import Generic, List, TypeVar
from model.auth import Auth

T = TypeVar("T")  # Generic Type (Customer, Employee, Etc...)
D = TypeVar("D")  # Generic Type (DAO)


class BaseController(ABC, Generic[T]):

    def __init__(self, dao_class: D):
        self.dao_class = dao_class
        self.items: List[T] = self.dao_class.load_all()

    @abstractmethod
    def create_instance(self, *args, **kwargs):
        """Create a new instance of the object (Customer, Employee, etc...)"""
        pass

    def register(self, *args, **kwargs) -> None:
        cpf = args[1] if len(args) > 1 else kwargs.get("cpf")
        if self.find(cpf):
            print('An entry with this CPF is already registered!\n')
            return
        if self.find_deleted(cpf):
            print('An entry with this CPF was previously deleted.\n')
            return

        if "password" in kwargs and kwargs["password"]:
            kwargs["password"] = Auth.hash_password(kwargs["password"])

        item = self.create_instance(*args, *kwargs)
        self.items.append(item)
        self.dao_class.save_all(self.items)
        print('✅ Successfully registered!')
