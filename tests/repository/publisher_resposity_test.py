import pytest

from unittest.mock import patch
from model.publisher import Publisher
from model.publisher_dao import BookDao
from repository.publisher_repository import PublisherRepository
from model.exceptions import PublisherNotFoundError


@pytest.fixture
def sample_publishers():
    """Fixture that provides a sample list of Publisher objects."""
    return [
        Publisher(publisher_id="1", legal_name="Publisher 1", city='City 1', state='ST', deleted=False),
        Publisher(publisher_id="2", legal_name="Publisher 2", city='City 2', state='ST', deleted=True),
        Publisher(publisher_id="3", legal_name="Publisher 3", city='City 3', state='ST', deleted=False),
    ]


@pytest.mark.parametrize('publisher_id, expected_legal_name, expected_city, expected_state', [
    ('1', 'Publisher 1', 'City 1', 'ST'),
    ('2', 'Publisher 2', 'City 2', 'ST'),
    ('3', 'Publisher 3', 'City 3', 'ST'),
])
def test_get_publisher_by_id_return_publisher(sample_publishers, publisher_id, expected_legal_name, expected_city, expected_state):
    """Ensures get_publisher_by_id() returns the correct Publisher when found."""
    with patch.object(BookDao, 'get_all', return_value=sample_publishers) as mock_load_all:
        publisher = PublisherRepository.get_publisher_by_id(publisher_id)
        assert publisher.legal_name == expected_legal_name
        assert publisher.city == expected_city
        assert publisher.state == expected_state
        mock_load_all.assert_called_once()


def test_get_publisher_by_id_raises_error(sample_publishers):
    """Ensures get_publisher_by_id() raises PublisherNotFoundError when ID is not found."""
    with patch.object(BookDao, 'get_all', return_value=sample_publishers) as mock_load_all:
        with pytest.raises(PublisherNotFoundError, match="Publisher with id X999 not found."):
            PublisherRepository.get_publisher_by_id("X999")


def test_get_publisher_options(sample_publishers):
    """Ensures options() returns the correct list with correct tuple."""
    with patch.object(BookDao, 'get_all', return_value=sample_publishers) as mock_load_all:
        options = PublisherRepository.options()
        expected = [(str(p.publisher_id), p.legal_name) for p in sample_publishers if not p.deleted]
        assert options == expected
        mock_load_all.assert_called_once()
