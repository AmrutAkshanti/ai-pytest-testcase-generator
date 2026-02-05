# Auto-generated tests for multi_funcs.py
# To execute: pytest output\test_multi_funcs.py

from examples.multi_funcs import *
import pytest
def test_is_even():
    assert is_even(0)
    assert is_even(2)
    assert not is_even(3)
    assert is_even(None)
    assert is_even('')

def test_reverse_string():
    assert reverse_string('abc') == 'cba'
    assert reverse_string('123') == '321'
    with pytest.raises(ValueError):
        reverse_string(123)

def test_sum_list():
    assert sum_list([1, 2, 3]) == 6
    assert sum_list([0, 0, 0]) == 0
    assert sum_list([-1, -2, -3]) == -6
    with pytest.raises(ValueError):
        sum_list([1, '2', 3])

