""" tests/test_calculator.py """
import sys
from io import StringIO
from app.calculator.calculator import Calculator

def run_calculator_with_input(monkeypatch, inputs):
    input_iterator = iter(inputs)
    monkeypatch.setattr('builtins.input', lambda _: next(input_iterator))
    captured_output = StringIO()
    sys.stdout = captured_output
    calculator = Calculator()
    calculator.run()
    sys.stdout = sys.__stdout__
    return captured_output.getvalue()

def test_no_operands(monkeypatch):
    """Test non-exit REPL operation with no inputs"""
    inputs = ["add", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Error:" in output

def test_one_operand(monkeypatch):
    """Test non-exit REPL operation with one input"""
    inputs = ["add 1", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Error:" in output
