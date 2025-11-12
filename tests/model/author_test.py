import pytest
from model.author import Author


@pytest.fixture
def publisher_data():
    return {
        'author_id': 'JD1',
        'name': 'John Doe'
    }


def test_create_author_default_deleted_false(publisher_data):
    """Checks if the author is created correctly with deleted=False by default."""
    author = Author(author_id=publisher_data['author_id'], name=publisher_data['name'])
    assert author.author_id == publisher_data['author_id']
    assert author.name == publisher_data['name']
    assert author.deleted is False


def test_create_author_with_deleted_true(publisher_data):
    """Checks if the author can be created with deleted=True."""
    author = Author(author_id=publisher_data['author_id'], name=publisher_data['name'], deleted=True)
    assert author.author_id == publisher_data['author_id']
    assert author.name == publisher_data['name']
    assert author.deleted is True


def test_setters_update_values_correctly(publisher_data):
    """Checks if the setters correctly update the attribute values."""
    author = Author(author_id=publisher_data['author_id'], name=publisher_data['name'])

    author.author_id = "JD2"
    author.name = publisher_data['name'] + '2'
    author.deleted = True

    assert author.author_id == "JD2"
    assert author.name == publisher_data['name'] + '2'
    assert author.deleted is True


def test_str_representation(publisher_data):
    """Checks if the __str__ method return the correctly formatted string."""
    author = Author(author_id=publisher_data['author_id'], name=publisher_data['name'])
    expected = f"ID: {publisher_data['author_id']} - Name: {publisher_data['name']}"
    assert str(author) == expected
