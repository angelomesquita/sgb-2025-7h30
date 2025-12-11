import pytest

from unittest.mock import patch
from model.author import Author
from model.book import Book
from model.publisher import Publisher
from model.book_dao import BookDao
from repository.book_repository import BookRepository
from model.exceptions import BookNotAvailableError, BookNotFoundError


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
    ('9789789789781', 'Book 1', 'Author', 'Publisher', 2025, 1),
    ('9789789789782', 'Book 2', 'Author', 'Publisher', 2025, 1),
    ('9789789789783', 'Book 3', 'Author', 'Publisher', 2025, 1),
])
def test_get_book_by_id_return_book(sample_books, isbn, expected_title, expected_author_name, expected_publisher_legal_name, expected_year, expected_quantity):
    """Ensures get_book_by_id() returns the correct Book when found."""
    with patch.object(BookDao, 'get_all', return_value=sample_books) as mock_load_all:
        book = BookRepository.get_book_by_isbn(isbn)
        assert book.title == expected_title
        assert book.author.name == expected_author_name
        assert book.publisher.legal_name == expected_publisher_legal_name
        assert book.year == expected_year
        assert book.quantity == expected_quantity
        mock_load_all.assert_called_once()


def test_get_book_by_id_raises_error(sample_books):
    """Ensures get_book_by_id() raises BookNotFoundError when isbn is not found."""
    with patch.object(BookDao, 'get_all', return_value=sample_books) as mock_load_all:
        with pytest.raises(BookNotFoundError, match="Book with isbn X999 not found."):
            BookRepository.get_book_by_isbn("X999")


@pytest.mark.parametrize("search_by, value", [
    ("title", "Book"),
    ("author", "Author"),
    ("available", True),
])
def test_search_book(sample_books, search_by, value):
    """Ensures search() return the correct book when found."""
    with patch.object(BookDao, 'get_all', return_value=sample_books) as mock_load_all:
        filters = {search_by: value}
        books = BookRepository.search(**filters)

        assert books == sample_books
        mock_load_all.assert_called_once()


def test_search_book_return_empty_iterable_when_book_not_available(sample_books):
    """Ensure search() return the empty list (iterable)"""
    with patch.object(BookDao, 'get_all', return_value=sample_books) as mock_load_all:
        books = BookRepository.search(title="Book 1", author="Author", available=False)

        assert books == []
        mock_load_all.assert_called_once()


def test_decrease_quantity_of_book(sample_books):
    with patch.object(BookDao, 'get_all', return_value=sample_books) as mock_load_all:
        result = BookRepository.decrease_quantity(isbn="9789789789781")

        assert result
        mock_load_all.assert_called_once()


def test_decrease_quantity_of_book_raises_error_when_book_has_not_quantity(sample_books):
    with patch.object(BookDao, 'get_all', return_value=sample_books):
        with pytest.raises(BookNotAvailableError, match="Book 'Book 1' is out of stock."):
            BookRepository.decrease_quantity(isbn="9789789789781", amount=2)

def test_increase_quantity_of_book(sample_books):
    with patch.object(BookDao, 'get_all', return_value=sample_books) as mock_load_all:
        result = BookRepository.increase_quantity(isbn="9789789789781")

        assert result
        mock_load_all.assert_called_once()
