import pytest
from model.publisher import Publisher


@pytest.fixture
def publisher_data():
    return {
        'publisher_id': '001',
        'legal_name': 'Publisher',
        'city': 'New York',
        'state': 'New York'
    }


def test_create_publisher_default_deleted_false(publisher_data):
    """Checks if the publisher is created correctly with deleted=False by default."""
    publisher = Publisher(
        publisher_id=publisher_data['publisher_id'],
        legal_name=publisher_data['legal_name'],
        city=publisher_data['city'],
        state=publisher_data['state']
    )
    assert publisher.publisher_id == publisher_data['publisher_id']
    assert publisher.legal_name == publisher_data['legal_name']
    assert publisher.city == publisher_data['city']
    assert publisher.state == publisher_data['state']
    assert publisher.deleted is False


def test_create_publisher_with_deleted_true(publisher_data):
    """Checks if the publisher can be created with deleted=True."""
    publisher = Publisher(
        publisher_id=publisher_data['publisher_id'],
        legal_name=publisher_data['legal_name'],
        city=publisher_data['city'],
        state=publisher_data['state'],
        deleted=True
    )
    assert publisher.publisher_id == publisher_data['publisher_id']
    assert publisher.legal_name == publisher_data['legal_name']
    assert publisher.city == publisher_data['city']
    assert publisher.state == publisher_data['state']
    assert publisher.deleted is True


'''
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
'''
