"""Test utils pedro"""
from helpers.helper import valida_cpf, retira_formatacao

class TestValidaCpf():
    """ TestValidaCpf """
    def test_valida_true(self):
        """ Testes para retorno True """
        assert valida_cpf('427.709.678-60') is True
        assert valida_cpf('42770967860') is True

    def test_valida_invalid_data(self):
        """ Testes para retorno False com dados inválidos"""
        assert valida_cpf('a') is False
        assert valida_cpf('11111111111') is False
        assert valida_cpf('42770964470') is False


class TestFormata():
    """ TestFormata """
    def test_formata_true(self):
        """ Testes para retorno True """
        assert retira_formatacao('427.709.678-60') == '42770967860'
