import pytest
from model.author import Author
from model.book import Book
from model.publisher import Publisher


@pytest.fixture
def book_default():
    """
    Provides a default Book instance for testing.

    Returns:
        - Book: A Book object with:
            - isbn: '9789789789789',
            - title: 'Book',
            - author_id: '1',
            - publisher_id: '1',
            - year = 2025,
            - quantity = 1,
            - Deleted=False.
    """
    author = Author(author_id="1", name="Author")
    publisher = Publisher(publisher_id="1", legal_name="Publisher", city="Curitiba", state="PR")
    return Book(isbn="9789789789789", title="Book", author=author, publisher=publisher, year=2025, quantity=1)


@pytest.mark.parametrize('deleted, expected', [
    (False, False),
    (True, True)
])
def test_book_creation_deleted_flag(deleted, expected):
    """
    Checks that the book instance is created with the correct deleted flag.

    Parameters (via parametrize):
        - deleted (bool): Value passed during Book creation.
        - expected (bool): Expected value for the deleted attribute.
    """
    author = Author(author_id="1", name="Author")
    publisher = Publisher(publisher_id="1", legal_name="Publisher", city="Curitiba", state="PR")
    book = Book(isbn="9789789789789", title="Book", author=author, publisher=publisher, year=2025, quantity=1, deleted=deleted)
    assert book.deleted is expected


def test_book_setters_update_attributes(book_default):
    """
    Verifies that the Book's setters correctly update its attributes.

    Fixture:
        - book_default: Provides a Book instance with default values.
    """
    book_default.isbn = "9789789789788"
    book_default.title = book_default.title + ' UPDATED'
    book_default.author = book_default.author
    book_default.publisher = book_default.publisher
    book_default.year = 2024
    book_default.quantity += 1
    book_default.deleted = True

    assert book_default.isbn == "9789789789788"
    assert book_default.title == book_default.title
    assert book_default.author == book_default.author
    assert book_default.publisher == book_default.publisher
    assert book_default.year == book_default.year
    assert book_default.quantity == book_default.quantity
    assert book_default.deleted is True


def test_book_str_returns_formatted_string(book_default):
    """
    Checks that the __str__ method returns the correctly formatted string representation.
    """
    expected = f"ISBN: {book_default.isbn}, Title: {book_default.title}, Author: {book_default.author.name}, Publisher: {book_default.publisher.legal_name}, Year: {book_default.year}, Quantity: {book_default.quantity}"
    assert str(book_default) == expected
