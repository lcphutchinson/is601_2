""" tests/test_operations.py """
import pytest
from app.operations.operations import addition, subtraction, multiplication, division

def test_addition():
    """Test addition outputs"""
    assert addition(1, 2) == 3
    assert addition(-1, 2) == 1
    assert addition(-1, -2) == -3

def test_subtraction():
    """Test subtraction outputs"""
    assert subtraction(3, 2) == 1
    assert subtraction(1, 2) == -1
    assert subtraction(-1, 2) == -3
    assert subtraction(-1, -2) == 1

def test_multiplication():
    """Test multiplication outputs"""
    assert multiplication(2, 4) == 8
    assert multiplication(-2, 4) == -8
    assert multiplication(-2, -4) == 8

def test_division():
    """Test division outputs"""
    assert division(12, 6) == 2
    assert division(-12, 4) == -3
    assert division(12, -3) == -4
    assert division(-12, -2) == 6

