class Cpf:

    _LENGTH = 11

    @staticmethod
    def validate(cpf: str) -> bool:
        cleaned_cpf = Cpf.clean(cpf)
        # TODO: Missing validation with check digit calculations
        # TODO: Lição 9 - Recursividade
        return cleaned_cpf.isdigit() and len(cleaned_cpf) == Cpf._LENGTH

    @staticmethod
    def clean(cpf: str) -> str:
        """ Removes non-numeric characters from the CPF """
        return ''.join(filter(str.isdigit, cpf)) # TODO: Lição 11 - Manipulação de String

