import pytest

from unittest.mock import patch
from model.author import Author
from model.book import Book
from model.publisher import Publisher
from model.book_dao import BookDao
from repository.book_repository import BookRepository
from model.exceptions import BookNotFoundError


@pytest.fixture
def sample_books():
    """Fixture that provides a sample list of Books objects."""
    author = Author(author_id="1", name="Author")
    publisher = Publisher(publisher_id="1", legal_name="Publisher", city="City", state="ST")
    return [
        Book(isbn="9789789789781", title="Book 1", author=author, publisher=publisher, year=2025, quantity=1, deleted=False),
        Book(isbn="9789789789782", title="Book 2", author=author, publisher=publisher, year=2025, quantity=1, deleted=True),
        Book(isbn="9789789789783", title="Book 3", author=author, publisher=publisher, year=2025, quantity=1, deleted=False),
    ]


@pytest.mark.parametrize('isbn, expected_title, expected_author_name, expected_publisher_legal_name, expected_year, expected_quantity', [
    ('1', 'Book 1', 'Author', 'Publisher', 2025, 1),
    ('2', 'Book 2', 'Author', 'Publisher', 2025, 1),
    ('3', 'Book 3', 'Author', 'Publisher', 2025, 1),
])
def test_get_book_by_id_return_publisher(sample_books, isbn, expected_title, expected_author_name, expected_publisher_legal_name, expected_year, expected_quantity):
    """Ensures get_book_by_id() returns the correct Book when found."""
    with patch.object(BookDao, 'get_all', return_value=sample_books) as mock_load_all:
        book = BookRepository.get_book_by_isbn(isbn)
        assert book.title == expected_title
        assert book.author.name == expected_author_name
        assert book.publisher.legal_name == expected_publisher_legal_name
        assert book.year == expected_year
        assert book.quantity == expected_quantity
        mock_load_all.assert_called_once()


def test_get_publisher_by_id_raises_error(sample_publishers):
    """Ensures get_publisher_by_id() raises PublisherNotFoundError when ID is not found."""
    with patch.object(PublisherDao, 'get_all', return_value=sample_publishers) as mock_load_all:
        with pytest.raises(PublisherNotFoundError, match="Publisher with id X999 not found."):
            PublisherRepository.get_publisher_by_id("X999")

