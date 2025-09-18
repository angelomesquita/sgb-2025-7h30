"""
exceptions.py

This module defines custom exceptions classes related to app management.
It uses hierarchies so that BaseController can raise exceptions polymorphic ally.
"""


# --------------
# Base Exceptions (common)
# --------------


class AppError(Exception):
    """Base class for all application errors."""
    pass


class AuthenticationError(AppError):
    """Raised when authentication fails."""
    pass


class InvalidCpfError(AppError):
    """Raised when CPF validation fails."""
    pass


class LoadError(AppError):
    """Raised when DAO fails to load items."""
    pass


# --------------
# Employee-related exceptions
# --------------


class EmployeeError(AppError):
    """Base class for Employee-related errors."""
    pass


class EmployeeAlreadyExistsError(EmployeeError):
    """Raised when trying to register an employee with an existing CPF."""
    pass


class EmployeeDeletedError(EmployeeError):
    """Raised when trying to register/update a deleted employee"""
    pass


class EmployeeRestoreError(EmployeeError):
    """Raised when trying to restore an active/new employee"""
    pass


class EmployeeNotFoundError(EmployeeError):
    """Raised when employee cannot be found."""
    pass


class EmployeeLoadError(EmployeeError, LoadError):
    """Raised when there is an error loading employee data from storage."""
    pass

# --------------
# Customer-related exceptions
# --------------


class CustomerError(AppError):
    """Base class for Customer-related errors."""
    pass


class CustomerAlreadyExistsError(CustomerError):
    """Raised when trying to register a customer with an existing CPF."""
    pass


class CustomerDeletedError(CustomerError):
    """Raised when trying to register/update a deleted customer"""
    pass


class CustomerRestoreError(CustomerError):
    """Raised when trying to restore an active/new customer"""
    pass


class CustomerNotFoundError(CustomerError):
    """Raised when customer cannot be found."""
    pass


class CustomerLoadError(CustomerError, LoadError):
    """Raised when there is an error loading customer data from storage."""
    pass

# --------------
# Author-related exceptions
# --------------


class AuthorError(AppError):
    """Base class for Author-related errors."""
    pass


class AuthorAlreadyExistsError(AuthorError):
    """Raised when trying to register an author."""
    pass


class AuthorDeletedError(AuthorError):
    """Raised when trying to register/update a deleted author"""
    pass


class AuthorRestoreError(AuthorError):
    """Raised when trying to restore an active/new author"""
    pass


class AuthorNotFoundError(AuthorError):
    """Raised when author cannot be found."""
    pass


class AuthorLoadError(AuthorError, LoadError):
    """Raised when there is an error loading author data from storage."""
    pass


# --------------
# Publisher-related exceptions
# --------------


class PublisherError(AppError):
    """Base class for Publisher-related errors."""
    pass


class PublisherAlreadyExistsError(PublisherError):
    """Raised when trying to register a publisher."""
    pass


class PublisherDeletedError(PublisherError):
    """Raised when trying to register/update a deleted publisher"""
    pass


class PublisherRestoreError(PublisherError):
    """Raised when trying to restore an active/new publisher"""
    pass


class PublisherNotFoundError(PublisherError):
    """Raised when publisher cannot be found."""
    pass


class PublisherLoadError(PublisherError, LoadError):
    """Raised when there is an error loading publisher data from storage."""
    pass
