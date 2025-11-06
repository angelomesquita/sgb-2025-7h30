import bcrypt
import pytest

from model.auth import Auth
from model.exceptions import AuthenticationError
from unittest.mock import Mock, patch


def test_hash_password_create_valid_hash():
    """Ensure hash_password method returns a valid hash bcrypt and is not equal to the original password."""
    password = "123"
    hashed = Auth.hash_password(password=password)

    assert isinstance(hashed, str)
    assert hashed != password
    assert bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))

# TODO: verify log register


def test_hash_password_raises_exception(monkeypatch):
    """Should raise an exception if bcrypt.hashpw fails."""
    def fake_hashpw(*args, **kwargs):
        raise ValueError("bcrypt failed")

    with patch("model.auth.bcrypt.hashpw", side_effect=fake_hashpw):
        with pytest.raises(ValueError, match="bcrypt failed"):
            password = "123"
            Auth.hash_password(password=password)


def test_verify_password_returns_true_for_correct_password():
    """Ensure verify_password returns True for a matching password."""
    password = "123"
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    assert Auth.verify_password(password, hashed) is True

# TODO: verify log register


def test_verify_password_returns_false_for_incorrect_password():
    """Ensure verify_password returns False for a wrong password."""
    password = "123"
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    assert Auth.verify_password("wrong_password", hashed) is False


def test_verify_password_raises_exception(monkeypatch):
    """Should raise an exception if bcrypt.checkpw fails."""
    def fake_checkpw(*args, **kwargs):
        raise ValueError("bcrypt failed")

    with patch("model.auth.bcrypt.checkpw", side_effect=fake_checkpw):
        with pytest.raises(ValueError, match="bcrypt failed"):
            password = "123"
            hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            Auth.verify_password("wrong_password", hashed)


def test_auth_returns_true_when_username_and_password_match():
    """Ensure auth() return True when username and password are correct."""
    expected_username = "admin"
    password = "123"
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    employee = Mock()
    employee.username = expected_username
    employee.password_hash = hashed

    assert Auth.auth(employee, expected_username, password) is True


def test_auth_raise_authentication_exception_error_when_username_is_wrong():
    """Ensure auth() raise AuthenticationError exception when username does not match."""
    expected_username = "admin"
    wrong_username = 'wrong_username'
    password = "123"
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    employee = Mock()
    employee.username = expected_username
    employee.password_hash = hashed

    with pytest.raises(AuthenticationError) as exception_info:
        Auth.auth(employee, wrong_username, hashed)
    assert f"Invalid credentials for username: {wrong_username}" in str(exception_info.value)


def test_auth_raises_authentication_exception_error_when_password_is_wrong():
    """Ensure auth() raise AuthenticationError exception when password does not match."""
    expected_username = "admin"
    password = "123"
    wrong_password = 'wrong_password'
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    employee = Mock()
    employee.username = expected_username
    employee.password_hash = hashed

    with pytest.raises(AuthenticationError) as exception_info:
        Auth.auth(employee, expected_username, wrong_password)
    assert f"Invalid credentials for username: {expected_username}" in str(exception_info.value)


def test_auth_raises_unexpected_exception(monkeypatch):
    """Should raise unexpected exception if something goes wrong."""
    expected_username = "admin"
    expected_password = "123"

    employee = Mock()
    employee.username = expected_username
    employee.password_hash = expected_password

    with patch("model.auth.Auth.verify_password", side_effect=Exception("unexpected error")):
        with pytest.raises(Exception, match="unexpected error"):
            Auth.auth(employee, expected_username, expected_password)
