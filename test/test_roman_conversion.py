"""Test utils pedro"""
from utils_pedro import roman_conversion

class TestConversao():
    """ TestConversao """
    def test_conversao_true(self):
        """ Testes para retorno True """
        assert roman_conversion(2) == 'II'
        assert roman_conversion(10) == 'X'

    def test_conversao_invalid_data(self):
        """ Testes para retorno False com dados inválidos"""
        assert roman_conversion('a') is False
        assert roman_conversion('1sx') is False
