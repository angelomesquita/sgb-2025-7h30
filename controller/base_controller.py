import logging
from abc import ABC, abstractmethod
from typing import Generic, List, Optional, Type, TypeVar

from model.auth import Auth
from model.base_dao import BaseDao
from model.cpf import Cpf

T = TypeVar("T")  # Generic Type (Customer, Employee, Etc...)
D = TypeVar("D")  # Generic Type (DAO)


class BaseController(ABC, Generic[T]):
    
    dao_class: Type[BaseDao[T]]
    logger: logging.Logger = logging.getLogger(__name__)
    key_field: str = "cpf"  # default

    AlreadyExistsError: Type[Exception] = Exception
    DeletedError: Type[Exception] = Exception
    RestoredError: Type[Exception] = Exception
    NotFoundError: Type[Exception] = Exception
    LoadError: Type[Exception] = Exception
    InvalidCpfError: Type[Exception] = Exception

    def __init__(self):
        self.items: List[T] = []
        try:
            self.items = self.dao_class.load_all()
            self.logger.info(f"{self.__class__.__name__} loaded successfully.")
        except Exception as e:
            self.logger.error(f"{self.__class__.__class__}: Failed to load items - {e}")
        
    @abstractmethod
    def create_instance(self, *args, **kwargs):
        """Create a new instance of the object (Customer, Employee, etc...)"""
        pass

    def register(self, *args, **kwargs) -> None:
        key_value = kwargs.get(self.key_field) or (args[0] if len(args) == 1 else None)
        self._register_logic(key_value, **kwargs)

    def _register_logic(self, key_value: str, **kwargs) -> None:
        if not key_value:
            print(f'❌ {self.key_field} is required.')
        if self.find(key_value):
            print(f'An entry with this {self.key_field} is already registered!\n')
            return
        if self.find_deleted(key_value):
            print(f'An entry with this {self.key_field} was previously deleted.\n')
            return
        if self.key_field == 'cpf':
            if not Cpf.validate(key_value):
                print(f'Invalid {self.key_field}. Try again.\n')
                return

        if "password" in kwargs:
            password = kwargs.pop("password")
            kwargs["password_hash"] = Auth.hash_password(password)

        item = self.create_instance(**{self.key_field: key_value}, **kwargs)
        self.items.append(item)
        self.dao_class.save_all(self.items)
        message = f'✅ {item.__class__.__name__} successfully registered!'
        self.logger.info(f"{message} [{item}]")
        print(message)

    def list(self) -> None:
        if not self.items:
            print("No entries registered yet.")
            return
        active_items = [item for item in self.items if not getattr(item, 'deleted', False)]
        if not active_items:
            print("No active entries found")
            return
        for item in active_items:
            print(item)
            
    def find(self, key_value: str) -> Optional[T]:
        for item in self.items:
            if getattr(item, self.key_field) == key_value and item.deleted is not True:
                return item
        return None

    def find_deleted(self, key_value: str) -> Optional[T]:
        for item in self.items:
            if getattr(item, self.key_field) == key_value and getattr(item, 'deleted', False) is True:
                return item
        return None
    
    def update(self, *args, **kwargs) -> None:
        key_value = kwargs.get(self.key_field) or (args[0] if len(args) == 1 else None)
        self._update_logic(key_value, **kwargs)
    
    def _update_logic(self, key_value: str, **kwargs) -> None:
        for item in self.items:
            if getattr(item, self.key_field) == key_value and not item.deleted:
                for field, value in kwargs.items():
                    if value is not None:
                        if field == "password":
                            setattr(item, "password_hash", Auth.hash_password(value))
                        else:
                            setattr(item, field, value)
                self.dao_class.save_all(self.items)
                message = f'{item.__class__.__name__} successfully updated!\n'
                self.logger.info(f"{message} [{item}]")
                print(message)
                return
        self.__entry_not_found()
    
    def delete(self, key_value: str) -> None:
        for item in self.items:
            if getattr(item, self.key_field) == key_value and item.deleted is not True:
                item.deleted = True
                message = f'{item.__class__.__name__} successfully deleted!\n'
                self.logger.info(f"{message} [{item}]")
                print(message)
                self.dao_class.save_all(self.items)
                return
        self.__entry_not_found()
    
    def restore(self, key_value: str) -> None:
        for item in self.items:
            if getattr(item, self.key_field) == key_value and item.deleted is True:
                item.deleted = False
                self.dao_class.save_all(self.items)
                message = f'{item.__class__.__name__} successfully restored!\n'
                self.logger.info(f"{message} [{item}]")
                print(message)
                return
        self.__entry_not_found()

    def _get_key_value(self, item: T) -> str:
        return getattr(item, self.key_field)

    @staticmethod
    def __entry_not_found() -> None:
        print('Entry not found.\n')
