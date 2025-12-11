import os
import pytest

from typing import Iterable

from model.author import Author
from model.author_dao import AuthorDao


@pytest.fixture(autouse=True)
def use_temp_database(tmp_path, monkeypatch):
    """
    Use a temporary SQLite database for each test to avoid
    interfering with the real 'library.db' file.
    """
    db_file = tmp_path / 'test_library.db'
    monkeypatch.setattr(AuthorDao, "_DB_NAME", str(db_file))

    AuthorDao.create_table()
    yield

    assert os.path.exists(db_file)


def test_create_table_is_idempotent():
    """Ensures create_table() can be called multiple times without errors."""
    AuthorDao.create_table()


def test_save_inserts_new_author_and_get_by_id_returns_it():
    """Ensures save() inserts a new author and get_by_id() retrieves it."""
    author = Author(author_id="1", name="Author")
    AuthorDao.save(author=author)

    loaded = AuthorDao.get_by_id(author_id=author.author_id)

    assert loaded is not None
    assert loaded.author_id == author.author_id
    assert loaded.name == author.name
    assert loaded.deleted == author.deleted


def test_save_updates_existing_author():
    """Ensures save() updates an existing author when the same author_id is used."""
    author = Author(author_id="A001", name="Original Name")
    AuthorDao.save(author=author)

    updated_author = Author(author_id="A001", name="Updated Name", deleted=True)
    AuthorDao.save(author=updated_author)

    active = AuthorDao.get_by_id(author_id=updated_author.author_id)
    assert active is None

    deleted_author = AuthorDao.get_by_id(author_id=updated_author.author_id, deleted=1)
    assert deleted_author is not None
    assert deleted_author.author_id == updated_author.author_id
    assert deleted_author.name == updated_author.name
    assert deleted_author.deleted is True


def test_get_by_id_returns_none_when_author_not_found():
    """Ensures get_by_id() returns None when author_id is not found."""
    result = AuthorDao.get_by_id(author_id="not_found")
    assert result is None


def test_get_all_returns_empty_list_when_no_authors():
    """Ensures get_all() return an empty list when there are no authors."""
    authors = AuthorDao.get_all()
    assert list(authors) == []


def test_get_all_returns_only_not_deleted_author():
    """Ensures get_all() returns only authors where deleted = 0."""
    a1 = Author(author_id="1", name="Author 1")
    a2 = Author(author_id="2", name="Author 2")
    a3 = Author(author_id="3", name="Author 3", deleted=True)

    AuthorDao.save(a1)
    AuthorDao.save(a2)
    AuthorDao.save(a3)

    authors: Iterable[Author] = AuthorDao.get_all()
    authors_list = list(authors)

    assert len(authors_list) == 2
    ids = { a.author_id for a in authors_list }
    assert "1" in ids
    assert "2" in ids
    assert "3" not in ids


def test_delete_sets_deleted_flag_to_true():
    """Ensures delete() sets deleted=1 for the given author_id."""
    author = Author(author_id="A002", name="To Delete")
    AuthorDao.save(author=author)

    AuthorDao.delete(author_id=author.author_id)

    active = AuthorDao.get_by_id(author_id=author.author_id)
    assert active is None

    deleted_author = AuthorDao.get_by_id(author_id=author.author_id, deleted=1)
    assert deleted_author is not None
    assert deleted_author.deleted is True


def test_truncate_delete_all_authors():
    """Ensures truncate() clean authors table."""
    a1 = Author(author_id="001", name="Author 1")
    a2 = Author(author_id="002", name="Author 2")
    a3 = Author(author_id="003", name="Author 3")

    AuthorDao.save(a1)
    AuthorDao.save(a2)
    AuthorDao.save(a3)

    result = AuthorDao.get_all()
    assert len(list(result)) == 3

    AuthorDao.truncate()

    result = AuthorDao.get_all()
    assert list(result) == []
