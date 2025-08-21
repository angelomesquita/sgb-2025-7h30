"""
exceptions.py

This module defines custom exceptions classes related to app management.
These exceptions are intended to provide meaningful error handling and improve
readability throughout the application, following the principles of explicitness.

Hierarchy:
    - EmployeeError (base class for all Employee-related exceptions)
        - EmployeeLoadError
        - EmployeeAlreadyExistsError
        - EmployeeDeletedError
        - EmployeeRestoreError
        - EmployeeNotFoundError
        - InvalidCpfError
"""


class EmployeeError(Exception):
    """Base class for Employee-related errors."""
    pass


class EmployeeLoadError(EmployeeError):
    """Raised when there is an error loading employee data from storage."""
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


class InvalidCpfError(EmployeeError):
    """Raised when CPF validation fails."""
    pass
