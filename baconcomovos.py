"""
1 - receber um inteiro
2 - saber se o numero é múltiplo de 3 e 5
    retorna bacon com ovos
3 - saber se o numero é múltiplo somente de 3
    retorna bacon
4 - saber se o número é múltiplo somente de 5
    retorna ovos
5 - saber se o número não é múltiplo de 3 e 5:
    retorna passar fome
"""


def bacon_com_ovos(n):
    assert isinstance(n, int), 'n deve ser inteiro'

    if n % 3 == 0 and n % 5 == 0:
        return 'Bacon com Ovos'

    if n % 3 == 0 and n % 5 != 0:
        return 'Bacon'

    if n % 3 != 0 and n % 5 == 0:
        return 'Ovos'

    return 'Passar fome'
