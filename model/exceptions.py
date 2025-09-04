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
