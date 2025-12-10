import pytest

from unittest.mock import patch
from model.author import Author
from model.author_dao import AuthorDao
from repository.author_repository import AuthorRepository
from model.exceptions import AuthorNotFoundError


@pytest.fixture
def sample_authors():
    """Fixture that provides a sample list of Author objects."""
    return [
        Author(author_id="1", name="Author 1", deleted=False),
        Author(author_id="2", name="Author 2", deleted=True),
        Author(author_id="3", name="Author 3", deleted=False),
    ]


@pytest.mark.parametrize('author_id, expected_name', [
    ('1', 'Author 1'),
    ('2', 'Author 2'),
    ('3', 'Author 3'),
])
def test_get_author_by_id_return_author(sample_authors, author_id, expected_name):
    """Ensures get_author_by_id() returns the correct Author when found."""
    with patch.object(AuthorDao, 'get_all', return_value=sample_authors) as mock_load_all:
        author = AuthorRepository.get_author_by_id(author_id)
        assert author.name == expected_name
        mock_load_all.assert_called_once()


def test_get_author_by_id_raises_error(sample_authors):
    """Ensures get_author_by_id() raises AuthorNotFoundError when ID is not found."""
    with patch.object(AuthorDao, 'get_all', return_value=sample_authors) as mock_load_all:
        with pytest.raises(AuthorNotFoundError, match="Author with id X999 not found."):
            AuthorRepository.get_author_by_id("X999")


def test_get_author_options(sample_authors):
    """Ensures options() returns the correct list with correct tuple."""
    with patch.object(AuthorDao, 'get_all', return_value=sample_authors) as mock_load_all:
        options = AuthorRepository.options()
        expected = [(str(a.author_id), a.name) for a in sample_authors if not a.deleted]
        assert options == expected
        mock_load_all.assert_called_once()
