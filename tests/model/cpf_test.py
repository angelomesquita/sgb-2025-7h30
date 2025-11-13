import pytest

from model.cpf import Cpf


@pytest.fixture
def cpf_samples():
    """
    Provides samples CPF string for testing different validation case.

    Returns:
        - dict: Dictionary containing valid and invalid CPF examples.
    """
    return {
        'valid': '415.081.330-26',
        'invalid_format': '415.081.330-2A',
        'short': '1111',
        'long': '11111111111111111',
        'repeated': '111.111.111-11',
        'invalid_check': '415.081.330-27'
    }


@pytest.mark.parametrize('input_cpf, expected', [
    ('111.111.111-11', '11111111111'),
    ('11111111111', '11111111111'),
])
def test_clean_removes_non_digits(input_cpf, expected):
    """
    Ensure that Cpf.clean() removes non-digits characters while keeping digits intact.

    Parameters (via parametrize):
        - input_cpf (str): CPF string to be cleaned.
        - expected (bool): Expected cleaned CPF contained only digits.
    """
    assert Cpf.clean(cpf=input_cpf) == expected


@pytest.mark.parametrize('cpf_key, expected', [
    ('valid', True),
    ('invalid_format', False),
    ('short', False),
    ('long', False),
    ('repeated', False),
    ('invalid_check', False),
])
def test_validate_various_cpfs(cpf_samples, cpf_key, expected):
    """
    Validates different CPF inputs using Cpf.validate()

    Fixture:
        - cpf_samples: Provides different CPF cases (valid and invalid).

    Parameters (via parametrize):
        - cpf_key (str): Key to select which CPF sample to validate.
        - expected (bool): Expected validation result.
    """
    assert Cpf.validate(cpf=cpf_samples[cpf_key]) is expected


def test_calculate_check_digits_first_and_second():
    """Ensure that Cpf.__calculate_check_digit() correctly computes both check digits."""
    cpf_digits = "41508133026"
    expected_first_digit = 2
    expected_second_digit = 6
    first_digit = Cpf._Cpf__calculate_check_digit(cpf_digits, length=9, initial_weight=10)  # type: ignore
    second_digit = Cpf._Cpf__calculate_check_digit(cpf_digits, length=10, initial_weight=11)  # type: ignore
    assert (first_digit, second_digit) == (expected_first_digit, expected_second_digit)


@pytest.mark.parametrize('digits, weight, expected', [
    ("303", 5, 24),
    ("", 5, 0)
])
def test_recursive_weighted_sum_calculation(digits, weight, expected):
    """
    Ensures that the private recursive method correctly calculate the weight sum.

    Parameters (via parametrize):
        - digits (str): Sequence of numeric digits.
        - weight (int): Initial weight for calculation.
        - expected (int): Expected weighed sum result.
    """
    result = Cpf._Cpf__recursive_weighted_sum(digits, weight)  # type: ignore
    assert result == expected

