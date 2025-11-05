import pytest
from model.author import Author


def test_create_author_default_deleted_false():
    """Checks if the author is created correctly with deleted=False by default."""
    author = Author(author_id="JD1", name="John Doe")
    assert author.author_id == "JD1"
    assert author.name == "John Doe"
    assert author.deleted is False


def test_create_author_with_deleted_true():
    """Checks if the author can be created with deleted=True."""
    author = Author(author_id="JD1", name="John Doe", deleted=True)
    assert author.author_id == "JD1"
    assert author.name == "John Doe"
    assert author.deleted is True


def test_setters_update_values_correctly():
    """Checks if the setters correctly update the attribute values."""
    author = Author(author_id="JD1", name="John Doe")

    author.author_id = "JD2"
    author.name = "John Doe 2"
    author.deleted = True

    assert author.author_id == "JD2"
    assert author.name == "John Doe 2"
    assert author.deleted is True


def test_str_representation():
    """Checks if the __str__ method return the correctly formatted string."""
    author = Author(author_id="JD1", name="John Doe")
    expected = "ID: JD1 - Name: John Doe"
    assert str(author) == expected










