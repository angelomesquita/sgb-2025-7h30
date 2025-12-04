import pytest
from model.author import Author


@pytest.fixture
def publisher_default():
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
def test_author_creation_deleted_flag(publisher_default, deleted, expected):
    """
    Checks that the author instance is created with the correct deleted flag.

    Fixture:
        - author_default: Provides an Author instance with default values.

    Parameters (via parametrize):
        - deleted (bool): Value passed during Author creation.
        - expected (bool): Expected value for the deleted attribute.
    """
    author = Author(author_id=publisher_default.author_id, name=publisher_default.name, deleted=deleted)
    assert author.author_id == publisher_default.author_id
    assert author.name == publisher_default.name
    assert author.deleted is expected


def test_author_setters_update_attributes(publisher_default):
    """
    Verifies that the Author's setters correctly update its attributes.

    Fixture:
        - author_default: Provides an Author instance with default values.
    """
    publisher_default.author_id = "JD2"
    publisher_default.name = publisher_default.name + ' UPDATED'
    publisher_default.deleted = True

    assert publisher_default.author_id == "JD2"
    assert publisher_default.name == publisher_default.name
    assert publisher_default.deleted is True


def test_author_str_returns_formatted_string(publisher_default):
    """
    Checks that the __str__ method returns the correctly formatted string representation.
    """
    expected = f"ID: {publisher_default.author_id} - Name: {publisher_default.name}"
    assert str(publisher_default) == expected
