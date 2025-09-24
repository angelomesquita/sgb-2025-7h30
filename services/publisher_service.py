from model.publisher import Publisher
from model.publisher_dao import PublisherDao
from model.exceptions import PublisherNotFoundError


class PublisherService:

    @staticmethod
    def get_publisher_by_id(publisher_id: str) -> Publisher:
        publishers = PublisherDao.load_all()
        publisher = next((p for p in publishers if str(p.publisher_id) == publisher_id), None)
        if publisher is None:
            raise PublisherNotFoundError(f"Publisher with id {publisher_id} not found.")
        return publisher
