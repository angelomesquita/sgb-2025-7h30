import os
import pytest

from typing import Iterable, Tuple

from model.author import Author
from model.author_dao import AuthorDao

from model.book import Book
from model.book_dao import BookDao

from model.publisher import Publisher
from model.publisher_dao import PublisherDao


@pytest.fixture(autouse=True)
def use_temp_database(tmp_path, monkeypatch):
    """
    Use a temporary SQLite database for each test to avoid
    interfering with the real 'library.db' file.
    """
    db_file = tmp_path / 'test_library.db'
    monkeypatch.setattr(BookDao, "_DB_NAME", str(db_file))

    BookDao.create_table()
    yield

    assert os.path.exists(db_file)


@pytest.fixture
def dependency_injection() -> Tuple[Author, Publisher]:
    author = Author(author_id="1", name="Author")
    AuthorDao.save(author=author)

    publisher = Publisher(publisher_id="1", legal_name="Author", city="City", state="ST")
    PublisherDao.save(publisher=publisher)

    return author, publisher


def test_create_table_is_idempotent():
    """Ensures create_table() can be called multiple times without errors."""
    BookDao.create_table()


def test_save_inserts_new_book_and_get_by_id_returns_it(dependency_injection):
    """Ensures save() inserts a new book and get_by_id() retrieves it."""
    author, publisher = dependency_injection

    book = Book(isbn="9789789789781", title="Book", author=author, publisher=publisher, year=2025, quantity=1)
    BookDao.save(book=book)

    loaded = BookDao.get_by_id(isbn=book.isbn)

    assert loaded is not None
    assert loaded.isbn == book.isbn
    assert loaded.title == book.title
    assert loaded.author.name == book.author.name
    assert loaded.publisher.legal_name == book.publisher.legal_name
    assert loaded.year == book.year
    assert loaded.quantity == str(book.quantity)
    assert loaded.deleted == book.deleted


def test_save_updates_existing_book(dependency_injection):
    """Ensures save() updates an existing book when the same isbn is used."""
    author, publisher = dependency_injection

    updated_book = Book(isbn="9789789789781", title="Book UP", author=author, publisher=publisher, year=2024, quantity=2, deleted=True)
    BookDao.save(book=updated_book)

    active = BookDao.get_by_id(isbn=updated_book.isbn)
    assert active is None

    deleted_book = BookDao.get_by_id(isbn=updated_book.isbn, deleted=1)
    assert deleted_book is not None
    assert deleted_book.isbn == updated_book.isbn
    assert deleted_book.title == updated_book.title
    assert deleted_book.author.name == updated_book.author.name
    assert deleted_book.publisher.legal_name == updated_book.publisher.legal_name
    assert deleted_book.deleted is True


def test_get_by_id_returns_none_when_book_not_found():
    """Ensures get_by_id() returns None when isbn is not found."""
    result = BookDao.get_by_id(isbn="not_found")
    assert result is None


def test_get_all_returns_empty_list_when_no_books():
    """Ensures get_all() return an empty list when there are no books."""
    books = BookDao.get_all()
    assert list(books) == []


def test_get_all_returns_only_not_deleted_books(dependency_injection):
    """Ensures get_all() returns only books where deleted = 0."""
    author, publisher = dependency_injection

    b1 = Book(isbn="1", title="Book 1", author=author, publisher=publisher, year=2025, quantity=1)
    b2 = Book(isbn="2", title="Book 2", author=author, publisher=publisher, year=2025, quantity=2)
    b3 = Book(isbn="3", title="Book 3", author=author, publisher=publisher, year=2025, quantity=3, deleted=True)

    BookDao.save(b1)
    BookDao.save(b2)
    BookDao.save(b3)

    books: Iterable[Book] = BookDao.get_all()
    book_list = list(books)

    assert len(book_list) == 2
    ids = { b.isbn for b in book_list }
    assert "1" in ids
    assert "2" in ids
    assert "3" not in ids


def test_delete_sets_deleted_flag_to_true(dependency_injection):
    """Ensures delete() sets deleted=1 for the given isbn."""
    author, publisher = dependency_injection

    book = Book(isbn="1", title="Book", author=author, publisher=publisher, year=2025, quantity=1)
    BookDao.save(book=book)

    BookDao.delete(isbn=book.isbn)

    active = BookDao.get_by_id(isbn=book.isbn)
    assert active is None

    deleted_book = BookDao.get_by_id(isbn=book.isbn, deleted=1)
    assert deleted_book is not None
    assert deleted_book.deleted is True

    result = BookDao.get_all()
    assert list(result) == []


def test_restore_book(dependency_injection):
    author, publisher = dependency_injection

    book = Book(isbn="1", title="book", author=author, publisher=publisher, year=2025, quantity=1, deleted=True)
    BookDao.save(book=book)

    deleted_book = BookDao.get_by_id(isbn=book.isbn, deleted=1)
    assert deleted_book is not None

    BookDao.restore(isbn=deleted_book.isbn)

    restored_book = BookDao.get_by_id(isbn=deleted_book.isbn)
    assert restored_book
    assert restored_book.isbn == deleted_book.isbn
