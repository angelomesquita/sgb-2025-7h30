import pytest
from model.author import Author


@pytest.fixture
def author_default():
    """
    Provides a default Author instance for testing.

    Returns:
        - Author: An Author object with ID 'JD01', name 'John Doe', and deleted=False.
    """
    return Author(author_id='JD01', name='John Doe')


@pytest.mark.parametrize('deleted, expected', [
    (False, False),
    (True, True)
])
def test_author_creation_deleted_flag(author_default, deleted, expected):
    """
    Checks that the author instance is created with the correct deleted flag.

    Fixture:
        - author_default: Provides an Author instance with default values.

    Parameters (via parametrize):
        - deleted (bool): Value passed during Author creation.
        - expected (bool): Expected value for the deleted attribute.
    """
    author = Author(author_id=author_default.author_id, name=author_default.name, deleted=deleted)
    assert author.author_id == author_default.author_id
    assert author.name == author_default.name
    assert author.deleted is expected


def test_author_setters_update_attributes(author_default):
    """
    Verifies that the Author's setters correctly update its attributes.

    Fixture:
        - author_default: Provides an Author instance with default values.
    """
    author_default.author_id = "JD2"
    author_default.name = author_default.name + ' UPDATED'
    author_default.deleted = True

    assert author_default.author_id == "JD2"
    assert author_default.name == author_default.name
    assert author_default.deleted is True


def test_author_str_returns_formatted_string(author_default):
    """
    Checks that the __str__ method returns the correctly formatted string representation.
    """
    expected = f"ID: {author_default.author_id} - Name: {author_default.name}"
    assert str(author_default) == expected
