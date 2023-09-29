def soma(x, y):
    """Soma x e y
    >>> soma(10, 10)
    20

    >>> soma('100', 19)
    Traceback (most recent call last):
    ...
    AssertionError: x precisa ser int ou float
    """
    assert isinstance(x, (int, float))
    assert isinstance(y, (int, float))
    return x + y


def subtrai(x, y):
    """Subtrai x e y
    >>> subtrai(10, 5)
    5

    >>> subtrai('8', 3)
    Traceback (most recent call last):
    ...
    AssertionError: x precisa ser int ou float
    """
    assert isinstance(x, (int, float))
    assert isinstance(y, (int, float))
    return x - y


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
