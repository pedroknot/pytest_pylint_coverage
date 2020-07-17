""" Main """
from utils_pedro import is_even, roman_conversion
from helpers.helper import valida_cpf


NUMERO = 2

if __name__ == "__main__":
    print(valida_cpf(NUMERO))
    print(is_even(NUMERO))
    print(roman_conversion(NUMERO))
