import pytest
import source.my_functions as my_functions

def test_add():
    result = my_functions.add_two_numbers(n1=3, n2=4)
    assert result == 7