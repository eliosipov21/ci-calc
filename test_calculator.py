"""
tests for calc app4
"""
import calculator


class TestCalculatorApp:
    def test_add(self):
        assert 5 == calculator.add(3, 2)

    def test_subtract(self):
        assert 5 == calculator.subtract(10, 5)
    
    def test_multiple(self):
        assert 5 == calculator.multiply(5, 1)
    
    def test_divide(self):
        assert 5 == calculator.divide(15, 3)
