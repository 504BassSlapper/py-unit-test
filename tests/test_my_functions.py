import pytest
import source.my_functions as my_functions


def test_add():
    result = my_functions.add_two_numbers(n1=3, n2=4)
    assert result == 7


def test_division():
    result = my_functions.divide_two_numbers(n1=30, n2=5)
    assert result == 6


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        my_functions.divide_two_numbers(n1=90, n2=0)
        assert True
