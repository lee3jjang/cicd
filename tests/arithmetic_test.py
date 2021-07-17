import pytest

@pytest.mark.parametrize("x, y, z", [(4, 2, 6), (6, 3, 9), (5, 2, 7)])
def test_add(calc, x, y, z):
    assert calc.add(x, y) == z

@pytest.mark.parametrize("x, y, z", [(4, 2, 2), (6, 3, 3), (5, 10, -5)])
def test_sub(calc, x, y, z):
    assert calc.sub(x, y) == z