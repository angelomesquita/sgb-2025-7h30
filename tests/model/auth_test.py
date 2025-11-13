import bcrypt
import pytest

from model.auth import Auth
from model.exceptions import AuthenticationError
from unittest.mock import Mock, patch


@pytest.fixture
def credentials():
    """
    Fixture that provides basic authentication credentials for the tests.

    Returns:
        dict: A dictionary containing:
            - 'username' (str): valid username
            - 'password' (str): plain text password
            - 'hashed' (str): bcrypt hash generated from the password
    """
    username = 'admin'
    password = '123'
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    return {'username': username, 'password': password, 'hashed': hashed}


def test_hash_password_create_valid_hash(credentials):
    """
    Ensure that the hash_password() method creates a valid bcrypt hash
    that is not equal to the original password.

    Scenario:
        - Uses the password provided by the `credentials` fixture.
        - Verifies that the generated hash is a string, different from
          the plain password, and matches the original when validated
          using bcrypt.
    """
    hashed = Auth.hash_password(password=credentials['password'])

    assert isinstance(hashed, str)
    assert hashed != credentials['password']
    assert bcrypt.checkpw(credentials['password'].encode('utf-8'), hashed.encode('utf-8'))


@pytest.mark.parametrize('side_effect, expected_exception, expected_message', [
    (ValueError('bcrypt failed'), ValueError, 'bcrypt failed'),
])
def test_hash_password_raises_exception(side_effect, expected_exception, expected_message):
    """Should raise an exception if bcrypt.hashpw() fails."""
    with patch('model.auth.bcrypt.hashpw', side_effect=side_effect):
        with pytest.raises(expected_exception, match=expected_message):
            Auth.hash_password('123')


@pytest.mark.parametrize('password, expected', [
    ('123', True),
    ('WrongPassword', False)
])
def test_verify_password(credentials, password, expected):
    """
    Verify that que verify_password() method behaves correctly for both
    matching and non-matching passwords.

    Fixture:
        - credentials: Provides the valid hash password.

    Parameters (via parametrize):
        - password (str): Input password to be checked.
        - expected (bool): Expected result (True if match, False otherwise).
    """
    assert Auth.verify_password(password, credentials['hashed']) is expected


@pytest.mark.parametrize('side_effect, expected_exception, expected_message', [
    (ValueError('bcrypt failed'), ValueError, 'bcrypt failed'),
])
def test_verify_password_raises_exception(credentials, side_effect, expected_exception, expected_message):
    """Should raise an exception if bcrypt.checkpw fails."""
    with patch('model.auth.bcrypt.checkpw', side_effect=side_effect):
        with pytest.raises(expected_exception, match=expected_message):
            Auth.verify_password('wrong_password', credentials['hashed'])


@pytest.mark.parametrize('username, password, expected', [
    ('admin', '123', True),
])
def test_auth_returns_true_when_credentials_are_valid(credentials, username, password, expected):
    """
    Ensure that Auth.auth() returns True when valid credentiais are provided.

    Fixture:
        - credentials: Provides the valid hash password.

    Parameters (via parametrize):
        - username (str): Username provided for authentication.
        - password (str): Password provided for authentication.
        - expected (bool): Expected result (True for successful authentication).

    Scenario:
        - A mock employee object is created with valid credentials.
        - Auth.auth() should return True, confirming successful authentication.
    """
    employee = Mock()
    employee.username = credentials['username']
    employee.password_hash = credentials['hashed']

    assert Auth.auth(employee, username, password) is expected


@pytest.mark.parametrize('username, password', [
    ('wrong_username', '123'),
    ('admin', 'wrong_password'),
])
def test_auth_raises_authentication_error(credentials, username, password):
    """
    Ensure auth() raise AuthenticationError when credentials are invalid.
    """
    employee = Mock()
    employee.username = credentials['username']
    employee.password_hash = credentials['hashed']

    with pytest.raises(AuthenticationError) as exception_info:
        Auth.auth(employee, username, password)

    assert f'Invalid credentials for username: {username}' in str(exception_info)
