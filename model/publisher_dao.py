from model.base_dao_file import BaseDao
from model.publisher import Publisher


class PublisherDao(BaseDao[Publisher]):

    _FILE_PATH = 'publishers.txt'

    @staticmethod
    def _serialize(p: Publisher) -> str:
        return f"{p.publisher_id}|{p.legal_name}|{p.city}|{p.state}|{p.deleted}"

    @staticmethod
    def _deserialize(data: str) -> Publisher:
        publisher_id, legal_name, city, state, deleted = data.split("|")
        publisher = Publisher(publisher_id, legal_name, city, state, deleted)
        publisher.deleted = deleted.lower() == "true"

        return publisher
