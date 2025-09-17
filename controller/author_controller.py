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
    key_field = "author_id"

    AlreadyExistsError = AuthorAlreadyExistsError
    DeletedError: AuthorDeletedError
    RestoredError: AuthorRestoreError
    NotFoundError: AuthorNotFoundError
    LoadError: AuthorLoadError

    def register(self, author_id: int, name: str) -> None:
        super().register(author_id, name=name)

    def create_instance(self, author_id: int, name: str, deleted: bool = False) -> Author:
        return Author(author_id, name, deleted)

    def update(self, author_id: int, name: str) -> None:
        super().update(author_id, name=name)
