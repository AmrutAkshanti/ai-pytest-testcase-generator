# Auto-generated tests for sample_func.py
# To execute: pytest tests\test_sample.py

from examples.sample_func import *
import pytest
def test_add_numbers():
    assert add_numbers(1, 2) == 3
    assert add_numbers(0, 0) == 0
    assert add_numbers(-1, 1) == 0
    assert add_numbers(-1, -1) == -2

def test_multiply_numbers():
    assert multiply_numbers(1, 2) == 2
    assert multiply_numbers(0, 0) == 0
    assert multiply_numbers(-1, 1) == -1
    assert multiply_numbers(-1, -1) == 1

def test_add_numbers_edge_cases():
    assert add_numbers(None, 2) == ValueError
    assert add_numbers(2, None) == ValueError
    assert add_numbers(None, None) == ValueError

def test_multiply_numbers_edge_cases():
    assert multiply_numbers(None, 2) == ValueError
    assert multiply_numbers(2, None) == ValueError
    assert multiply_numbers(None, None) == ValueError

def test_add_numbers_invalid_input():
    with pytest.raises(ValueError):
        add_numbers("1", 2)
    with pytest.raises(ValueError):
        add_numbers(1, "2")
    with pytest.raises(ValueError):
        add_numbers("1.5", 2)
    with pytest.raises(ValueError):
        add_numbers(1, "2.5")

def test_multiply_numbers_invalid_input():
    with pytest.raises(ValueError):
        multiply_numbers("1", 2)
    with pytest.raises(ValueError):
        multiply_numbers(2, "1")
    with pytest.raises(ValueError):
        multiply_numbers("1.5", 2)
    with pytest.raises(ValueError):
        multiply_numbers(1, "2.5")

def test_add_numbers_invalid_input():
    with pytest.raises(ValueError):
        add_numbers("1", 2)
    with pytest.raises(ValueError):
        add_numbers(1, "2")
    with pytest.raises(ValueError):
        add_numbers("1.5", 2)
    with pytest.raises(ValueError):
        add_numbers(1, "2.5")

def test_multiply_numbers_invalid_input():
    with pytest.raises(ValueError):
        multiply_numbers("1", 2)
    with pytest.raises(ValueError):
        multiply_numbers(2, "1")
    with pytest.raises(ValueError):
        multiply_numbers("1.5", 2)
    with pytest.raises(ValueError):
        multiply_numbers(1, "2.5")

def test_add_numbers_large_input():
    assert add_numbers(1e18, 2e18) == 3e18
    assert add_numbers(0, 2e18) == 2e18
    assert add_numbers(1e18, 0) == 1e18
    assert add_numbers(0, 0) == 0

def test_multiply_numbers_large_input():
    assert multiply_numbers(1e18, 2e18) == 2e36
    assert multiply_numbers(0, 2e18) == 0
    assert multiply_numbers(1e18, 0) == 0
    assert multiply_numbers(0, 0) == 0

def test_add_numbers_negative_input():
    assert add_numbers(-1, 2) == 1
    assert add_numbers(-1, -1) == 0
    assert add_numbers(1, -1) == 0
