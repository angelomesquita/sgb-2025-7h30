import pytest
from model.publisher import Publisher


@pytest.fixture
def publisher_default():
    """
    Provides a default Publisher instance for testing.

    Returns:
        - Publisher: A Publisher object with:
            - ID: '1',
            - Legal name: 'Publisher',
            - City: 'New York',
            - State: 'NY',
            - Deleted=False.
    """
    return Publisher(publisher_id="1", legal_name="Publisher", city="New York", state="NY")


@pytest.mark.parametrize('deleted, expected', [
    (False, False),
    (True, True)
])
def test_publisher_creation_deleted_flag(deleted, expected):
    """
    Checks that the publisher instance is created with the correct deleted flag.

    Parameters (via parametrize):
        - deleted (bool): Value passed during Publisher creation.
        - expected (bool): Expected value for the deleted attribute.
    """
    publisher = Publisher(publisher_id="1", legal_name="Publisher", city="City", state="ST", deleted=deleted)
    assert publisher.deleted is expected


def test_publisher_setters_update_attributes(publisher_default):
    """
    Verifies that the Publisher's setters correctly update its attributes.

    Fixture:
        - author_default: Provides a Publisher instance with default values.
    """
    publisher_default.publisher_id = "2"
    publisher_default.legal_name = publisher_default.legal_name + ' UPDATED'
    publisher_default.city = publisher_default.city + ' UPDATED'
    publisher_default.state = 'ST'
    publisher_default.deleted = True

    assert publisher_default.publisher_id == "2"
    assert publisher_default.legal_name == publisher_default.legal_name
    assert publisher_default.city == publisher_default.city
    assert publisher_default.state == publisher_default.state
    assert publisher_default.deleted is True


def test_publisher_str_returns_formatted_string(publisher_default):
    """
    Checks that the __str__ method returns the correctly formatted string representation.
    """
    expected = f"ID: {publisher_default.publisher_id}, Legal Name: {publisher_default.legal_name}, City: {publisher_default.city} - State: {publisher_default.state}"
    assert str(publisher_default) == expected
