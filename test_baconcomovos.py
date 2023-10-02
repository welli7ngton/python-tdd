# flake8: noqa
"""
TDD - Test Deiven Development

RED
Parte 1 - Criar o teste e ver falhar

GREEN
Parte 2 - Criar o código e ver o teste passar

REFACTOR
Parte 3 - Melhorar o código
"""

import unittest
from baconcomovos import bacon_com_ovos


class TestBaconComOvos(unittest.TestCase):
    def test_bacon_com_ovos_verifica_se_n_e_isntancia_de_int(self):
        with self.assertRaises(AssertionError):
            bacon_com_ovos('0')

    def test_bacon_com_ovos_deve_retornar_bacon_com_ovos_se_entrada_for_multiplo_de_3_e_5(self):
        entradas = (15, 30, 45, 60)
        saida = 'Bacon com Ovos'

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(bacon_com_ovos(entrada), saida)

    def test_bacon_com_ovos_deve_retornar_passar_fome_caso_entrada_nao_seja_multipla_nem_de_3_e_nem_de_5(self):
        entradas = (8, 1412, 17, 94)
        saida = 'Passar fome'

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(bacon_com_ovos(entrada), saida)

    def test_bacon_com_ovos_deve_retornar_bacon_caso_entrada_seja_multipla_somente_de_3(self):
        entradas = (3, 9, 27, 33)
        saida = 'Bacon'

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(bacon_com_ovos(entrada), saida)

    def test_bacon_com_ovos_retorna_ovos_caso_entrada_seja_multipla_somente_de_5(self):
        entradas = (5, 10, 20, 50)
        saida = 'Ovos'

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(bacon_com_ovos(entrada), saida)

unittest.main(verbosity=2)
