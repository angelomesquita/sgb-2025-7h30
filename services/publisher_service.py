from typing import List, Tuple
from model.publisher import Publisher
from model.publisher_dao import PublisherDao
from model.exceptions import PublisherNotFoundError


class PublisherService:

    @staticmethod
    def _get_all_publishers() -> List[Publisher]:
        """Load all publishers from DAO (active and deleted)"""
        return PublisherDao.load_all()

    @staticmethod
    def get_publisher_by_id(publisher_id: str) -> Publisher:
        publishers = PublisherService._get_all_publishers()
        publisher = next((p for p in publishers if str(p.publisher_id) == publisher_id), None)
        if publisher is None:
            raise PublisherNotFoundError(f"Publisher with id {publisher_id} not found.")
        return publisher

    @staticmethod
    def options() -> List[Tuple[str, str]]:
        publishers = PublisherService._get_all_publishers()
        return [(str(p.publisher_id), p.legal_name) for p in publishers if not p.deleted]
