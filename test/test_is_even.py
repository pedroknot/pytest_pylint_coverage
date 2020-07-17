"""Test utilspedro"""
from utils_pedro import is_even

class TestHelperNumbers():
    """ TestHelperNumbers """
    def test_is_even_true(self):
        """ Testes para retorno True """
        assert is_even(2) is True
        assert is_even(10) is True

    def test_is_even_false(self):
        """ Testes para retorno False"""
        assert is_even(1) is False
        assert is_even(9) is False

    def test_is_even_invalid_data(self):
        """ Testes para retorno False com dados inválidos"""
        assert is_even('a') is False
        assert is_even(10.787) is False
