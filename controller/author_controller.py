from controller.base_controller import BaseController
from model.author import Author
from model.author_dao import AuthorDao
from model.logger import author_logger
from model.exceptions import (
    AuthorAlreadyExistsError,
    AuthorDeletedError,
    AuthorRestoreError,
    AuthorNotFoundError,
    AuthorLoadError
)


class CustomerController(BaseController[Author]):

    dao_class = AuthorDao
    logger = author_logger

    AlreadyExistsError = AuthorAlreadyExistsError
    DeletedError: AuthorDeletedError
    RestoredError: AuthorRestoreError
    NotFoundError: AuthorNotFoundError
    LoadError: AuthorLoadError

    def register(self, name: str) -> None:
        super().register(name=name)

    def create_instance(self, name: str, deleted: bool = False) -> Author:
        return Author(name, deleted)

    def update(self, name: str) -> None:
        super().update(name=name)
