from controller.base_controller_sqlite import BaseControllerSqlite
from model.publisher import Publisher
from model.publisher_dao import PublisherDao
from model.logger import publisher_logger
from model.exceptions import (
    PublisherAlreadyExistsError,
    PublisherDeletedError,
    PublisherRestoreError,
    PublisherNotFoundError,
    PublisherLoadError
)


class PublisherController(BaseControllerSqlite[Publisher]):

    dao_class = PublisherDao
    logger = publisher_logger

    AlreadyExistsError = PublisherAlreadyExistsError
    DeletedError: PublisherDeletedError
    RestoredError: PublisherRestoreError
    NotFoundError: PublisherNotFoundError
    LoadError: PublisherLoadError

    def __init__(self):
        super().__init__(model_class=Publisher, key_field="publisher_id")

    def create_instance(self, publisher_id: str, legal_name: str, city: str, state: str, deleted: bool = False) -> Publisher:
        return Publisher(publisher_id, legal_name, city, state, deleted)
