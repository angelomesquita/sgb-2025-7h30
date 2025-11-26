import logging
from abc import ABC, abstractmethod
from typing import Generic, Iterable, Optional, Type, TypeVar

from model.auth import Auth
from model.base_dao import BaseDao
from model.cpf import Cpf
from model.person import Person

T = TypeVar("T")


class BaseControllerSqlite(ABC, Generic[T]):
    dao_class: Type[BaseDao[T]]
    logger: logging.Logger = logging.getLogger(__name__)

    AlreadyExistsError: Type[Exception] = Exception
    DeletedError: Type[Exception] = Exception
    RestoredError: Type[Exception] = Exception
    NotFoundError: Type[Exception] = Exception
    LoadError: Type[Exception] = Exception
    InvalidCpfError: Type[Exception] = Exception

    def __init__(self, model_class: Type[T], key_field: str = "cpf"):
        self.model_class = model_class
        self.key_field = key_field

    @abstractmethod
    def create_instance(self, *args, **kwargs):
        """Create a new instance of the object (Customer, Employee, etc...)"""
        pass

    def register(self, **kwargs) -> None:
        key_value = kwargs.get(self.key_field)

        if not key_value:
            print(f'❌ {self.key_field} is required.')
        if self.key_field == 'cpf':
            if not Cpf.validate(key_value):
                print(f'Invalid {self.key_field}. Try again.\n')
                return
        if issubclass(self.model_class, Person) and "password" in kwargs:
            password = kwargs.pop("password")
            kwargs["password_hash"] = Auth.hash_password(password)

        item = self.create_instance(**kwargs)
        self.dao_class.save(item)

        message = f'✅ {item.__class__.__name__} successfully registered!'
        self.logger.info(f"{message} [{item}]")
        print(message)

    def list(self) -> None:
        items = self.dao_class.get_all()

        if not items:
            print("No entries registered yet.")
            return

        for item in items:
            print(item)

    def list_all(self) -> Optional[Iterable[T]]:
        items = self.dao_class.get_all()

        if not items:
            print("No entries registered yet.")
            return

        return items

    def find(self, key_value: str) -> Optional[T]:
        return self.dao_class.get_by_id(key_value)

    def update(self, *args, **kwargs) -> None:
        key_value = kwargs.get(self.key_field) or (args[0] if len(args) == 1 else None)
        item = self.dao_class.get_by_id(key_value)

        if not item:
            print("Entry not found.")
            return

        for field, value in kwargs.items():
            if value is not None:
                if field == "password":
                    setattr(item, "password_hash", Auth.hash_password(value))
                else:
                    setattr(item, field, value)

        self.dao_class.save(item)

        message = f'{item.__class__.__name__} successfully updated!\n'
        self.logger.info(f"{message} [{item}]")
        print(message)

    def delete(self, key_value: str) -> None:
        item = self.dao_class.get_by_id(key_value)

        if not item:
            print("Entry not found.")
            return

        self.dao_class.delete(key_value)

        message = f'{item.__class__.__name__} successfully deleted!\n'
        self.logger.info(f"{message} [{item}]")
        print(message)

    def restore(self, key_value: str) -> bool:
        item = self.dao_class.get_by_id(key_value, deleted=1)

        if not item:
            print("Entry not found.")
            return False

        item.deleted = False
        self.dao_class.save(item)

        message = f'{item.__class__.__name__} successfully restored!\n'
        self.logger.info(f"{message} [{item}]")
        print(message)

        return True
