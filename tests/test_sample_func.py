# Auto-generated tests for sample_func.py
# To execute: pytest tests\test_sample_func.py

from examples.sample_func import *

def test_add_numbers():
    assert add_numbers(1, 2) == 3
    assert add_numbers(0, 0) == 0
    assert add_numbers(-1, 1) == 0
    assert add_numbers(1000000000000000000, 1000000000000000000) == 2000000000000000000

def test_multiply_numbers():
    assert multiply_numbers(1, 2) == 2
    assert multiply_numbers(0, 0) == 0
    assert multiply_numbers(-1, 1) == -1
    assert multiply_numbers(1000000000000000000, 1000000000000000000) == 1000000000000000000000000000000000000000000000000000000000000000

