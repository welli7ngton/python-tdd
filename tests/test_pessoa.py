# flake8: noqa
import unittest
from unittest.mock import patch
from pessoa import Pessoa


class TestPessoa(unittest.TestCase):
    def setUp(self):
        self.pessoa = Pessoa('Wellington', 'Almeida')
    
    def test_pessoa_attr_nome_tem_valor(self):
        self.assertEqual(self.pessoa.nome, 'Wellington')

    def test_pessoa_attr_sobrenome_tem_valor(self):
        self.assertEqual(self.pessoa.sobrenome, 'Almeida')

    def test_pessoa_attr_dados_obtidos_inicia_false(self):
        self.assertFalse(self.pessoa.dados_obtidos)
    
    def test_pessoa_attr_nome_e_str(self):
        self.assertIsInstance(self.pessoa.nome, str)

    def test_pessoa_attr_sobrenome_e_str(self):
        self.assertIsInstance(self.pessoa.sobrenome, str)

    def test_obter_todos_os_dados_sucesso_OK(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = True

            self.assertEqual(self.pessoa.obter_todos_os_dados(), 'Conectado')
            self.assertTrue(self.pessoa.dados_obtidos)

    def test_obter_todos_os_dados_falha_404(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = False

            self.assertEqual(self.pessoa.obter_todos_os_dados(), 'Erro 404')
            self.assertFalse(self.pessoa.dados_obtidos)

if __name__ == '__main__':
    unittest.main(verbosity=2)