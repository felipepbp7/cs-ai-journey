from calc101.ops import soma, sub, mul, div
import pytest

def test_soma():
    assert soma(2, 3) == 5

def test_sub():
    assert sub(5, 3) == 2

def test_mul():
    assert mul(4, 2) == 8

def test_div():
    assert div(6, 3) == 2

def test_div_zero():
    import pytest
    with pytest.raises(ZeroDivisionError):
        div(1, 0)
