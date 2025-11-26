from controller.base_controller_sqlite import BaseControllerSqlite
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


class AuthorController(BaseControllerSqlite[Author]):

    dao_class = AuthorDao
    logger = author_logger

    AlreadyExistsError = AuthorAlreadyExistsError
    DeletedError: AuthorDeletedError
    RestoredError: AuthorRestoreError
    NotFoundError: AuthorNotFoundError
    LoadError: AuthorLoadError

    def __init__(self):
        super().__init__(model_class=Author, key_field="author_id")

    def create_instance(self, author_id: str, name: str, deleted: bool = False) -> Author:
        return Author(author_id=author_id, name=name, deleted=deleted)
