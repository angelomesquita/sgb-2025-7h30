"""
    CPF Validation Rules
        1. The CPF has 11 numeric digits
        2. The first 9 digits are used to calculate the last 2 (check digits)
        3. The fist check digit (10th digit) is calculated by multiplying the first 9 digits
           by decreasing weights from 10 to 2.
        4. The second check digit (11th digit) is calculated by multiplying the first 9 digits
           + the first check digit, with weights from 11 to 2.
        5. The check digit formula is:
            - Sum of the products of digits * weights
            - Remainder of the division of the sum by 11
            - if the remainder is less than 2, the digit is 0; otherwise, it is 11 - remainder
        Example:
            - 415.081.330-??
            - First check digit:
                - 4x10 + 1x9 + 5x8 + 0x7 + 8x6 + 1x5 + 3x4 + 3x3 + 0x2
                - 40 + 9 + 40 + 0 + 48 + 5 + 12 + 9 + 0 = 163
                - 163 / 11 = 14 remainder 9 | 11 - 9 = 2
                - 415.081.330-2?
            - Second check digit:
                - 4x11 + 1x10 + 5x9 + 0x8 + 8x7 + 1x6 + 3x5 + 3x4 + 0x3 + 2x2
                - 44 + 10 + 45 + 0 + 56 + 6 + 15 + 12 + 0 + 4 = 192
                - 192 / 11 = 17 remainder 5 | 11 - 5 = 6
                - 415.081.330-26
"""


class Cpf:
    _LENGTH = 11

    @staticmethod
    def validate(cpf: str) -> bool:
        cleaned_cpf = Cpf.clean(cpf)

        if not (cleaned_cpf.isdigit() and len(cleaned_cpf) == Cpf._LENGTH):
            return False

        if cleaned_cpf == cleaned_cpf[0] * Cpf._LENGTH:
            return False

        first_digit = Cpf.__calculate_check_digit(cpf=cleaned_cpf, length=9, initial_weight=10)
        second_digit = Cpf.__calculate_check_digit(cpf=cleaned_cpf, length=10, initial_weight=11)

        return cleaned_cpf[-2:] == f"{first_digit}{second_digit}"

    @staticmethod
    def clean(cpf: str) -> str:
        """ Removes non-numeric characters from the CPF """
        return ''.join(filter(str.isdigit, cpf))

    @staticmethod
    def __calculate_check_digit(cpf: str, length: int, initial_weight: int) -> int:
        total = Cpf.__recursive_weighted_sum(cpf[:length], initial_weight)
        remainder = total % Cpf._LENGTH
        return 0 if remainder < 2 else Cpf._LENGTH - remainder

    @staticmethod
    def __recursive_weighted_sum(digits: str, weight: int) -> int:
        if not digits:
            return 0
        return int(digits[0]) * weight + Cpf.__recursive_weighted_sum(digits[1:], weight - 1)

