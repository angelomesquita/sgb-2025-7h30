from model.cpf import Cpf


def test_clean_removes_non_digits():
    """Ensure non-digits characters are removed from CPF."""
    cpf = '111.111.111-11'
    cleaned = Cpf.clean(cpf=cpf)
    assert cleaned == '11111111111'


def test_clean_keeps_only_digits():
    """Ensure numbers remain unchanged after cleaning."""
    cpf = '11111111111'
    cleaned = Cpf.clean(cpf=cpf)
    assert cleaned == cpf


def test_validate_returns_false_for_invalid_format():
    """Ensure invalid CPF format (for example: with character) return False."""
    invalid_cpf_format = "415.081.330-2A"
    assert Cpf.validate(cpf=invalid_cpf_format) is False


def test_validate_returns_false_for_wrong_length():
    """Ensure CPF with incorrect length returns False."""
    short_cpf = '1111'
    long_cpf = '11111111111111111'
    assert not Cpf.validate(cpf=short_cpf)
    assert Cpf.validate(cpf=long_cpf) is False


def test_validate_returns_false_for_repeated_digits():
    """Ensure CPF with all identical digits returns False."""
    repeated_digits_cpf = '111.111.111-11'
    assert Cpf.validate(cpf=repeated_digits_cpf) is False


def test_validate_returns_true_for_valid_cpf():
    """Ensure valid CPF return True."""
    valid_cpf = "415.081.330-26"
    assert Cpf.validate(cpf=valid_cpf) is True


def test_validate_returns_false_for_invalid_cpf():
    """Ensure invalid CPF (with wrong check digits) return False."""
    invalid_cpf = "415.081.330-27"
    assert Cpf.validate(cpf=invalid_cpf) is False


def test_calculate_check_digits_first_and_second():
    """Ensure check digit calculation returns expected digits."""
    cpf_digits = "41508133026"
    expected_first_digit = 2
    expected_second_digit = 6
    first_digit = Cpf._Cpf__calculate_check_digit(cpf_digits, length=9, initial_weight=10)  # type: ignore
    second_digit = Cpf._Cpf__calculate_check_digit(cpf_digits, length=10, initial_weight=11)  # type: ignore
    assert (first_digit, second_digit) == (expected_first_digit, expected_second_digit)


def test_recursive_weighted_sum_with_empty_string():
    """Ensure recursive base case returns 0 when digits are empty."""
    assert Cpf._Cpf__recursive_weighted_sum("", 5) == 0  # type: ignore


def test_recursive_weighted_sum_calculation():
    """Ensure recursive sum is calculated correctly."""
    # digits = 303, weights = 5, 4, 3
    result = Cpf._Cpf__recursive_weighted_sum("303", 5)  # type: ignore
    # 3*5 + 0*4 + 3*3 | 15 + 0 + 9 | 24
    assert result == 24
