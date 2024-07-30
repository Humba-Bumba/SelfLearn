import pytest
from calc import calc


@pytest.mark.parametrize("a, b, c", [(1, 2, 3)])
def test_calc(a, b, c):
    assert calc(a, b) == c
    