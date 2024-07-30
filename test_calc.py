import pytest
from calc import calc_sum, calc_mul


@pytest.mark.parametrize("a, b, c", [(1, 2, 3)])
def test_calc_sum(a, b, c):
    assert calc_sum(a, b) == c


@pytest.mark.parametrize("a, b, c", [(1, 2, 2)])
def test_calc_mul(a, b, c):
    assert calc_mul(a, b) == c
