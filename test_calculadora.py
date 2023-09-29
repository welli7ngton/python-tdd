# flake8: noqa
import unittest
from calculadora import soma


class TestCalculadora(unittest.TestCase):
    def test_soma_5_e_5_retorna_10(self):
        self.assertEqual(soma(5, 5), 10)

    def test_soma_2_e_5_retorna_7(self):
        self.assertEqual(soma(3, 4), 7)

    def test_soma_varias_entradas(self):
        x_y_saidas = (
            (10, 10, 20),
            (5, 15, 20),
            (1, 1, 2),
            (8, 8, 16),
            (1, 3, 4),
            (101, 101, 202),
        )

        for saida in x_y_saidas:
            x, y, saida = saida
            self.assertEqual(soma(x, y), saida)

    def test_verifica_tipo_de_x_int_ou_float_deve_retornar_assertionerror(self):
        with self.assertRaises(AssertionError):
            soma('x', 0)

    def test_verifica_tipo_de_y_int_ou_float_deve_retornar_assertionerror(self):
        with self.assertRaises(AssertionError):
            soma(2, 'y')


unittest.main(verbosity=2)
