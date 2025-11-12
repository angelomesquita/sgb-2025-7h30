import pytest
from model.author import Author


@pytest.fixture
def author_data():
    return {
        'author_id': 'JD1',
        'name': 'John Doe'
    }


def test_create_author_default_deleted_false(author_data):
    """Checks if the author is created correctly with deleted=False by default."""
    author = Author(author_id=author_data['author_id'], name=author_data['name'])
    assert author.author_id == author_data['author_id']
    assert author.name == author_data['name']
    assert author.deleted is False


def test_create_author_with_deleted_true(author_data):
    """Checks if the author can be created with deleted=True."""
    author = Author(author_id=author_data['author_id'], name=author_data['name'], deleted=True)
    assert author.author_id == author_data['author_id']
    assert author.name == author_data['name']
    assert author.deleted is True


def test_setters_update_values_correctly(author_data):
    """Checks if the setters correctly update the attribute values."""
    author = Author(author_id=author_data['author_id'], name=author_data['name'])

    author.author_id = "JD2"
    author.name = author_data['name'] + '2'
    author.deleted = True

    assert author.author_id == "JD2"
    assert author.name == author_data['name'] + '2'
    assert author.deleted is True


def test_str_representation(author_data):
    """Checks if the __str__ method return the correctly formatted string."""
    author = Author(author_id=author_data['author_id'], name=author_data['name'])
    expected = f"ID: {author_data['author_id']} - Name: {author_data['name']}"
    assert str(author) == expected
