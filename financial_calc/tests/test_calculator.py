from calculator import calculate_simple_interest, calculate_compound_interest, calculate_tax
import pytest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestSimpleInterest:
    def test_calculation(self):
        assert calculate_simple_interest(1000, 5, 3) == 150.0
        assert calculate_simple_interest(500, 10, 2) == 100.0

    def test_zeros(self):
        assert calculate_simple_interest(0, 5, 3) == 0.0
        assert calculate_simple_interest(1000, 0, 3) == 0.0
        assert calculate_simple_interest(1000, 5, 0) == 0.0

    def test_negative_values(self):
        with pytest.raises(ValueError):
            calculate_simple_interest(-1000, 5, 3)
        with pytest.raises(ValueError):
            calculate_simple_interest(1000, -5, 3)
        with pytest.raises(ValueError):
            calculate_simple_interest(1000, 5, -3)


class TestCompoundInterest:
    def test_calculation(self):
        assert round(calculate_compound_interest(1000, 5, 3, 1), 3) == 1157.625
        assert round(calculate_compound_interest(1000, 5, 3, 4), 3) == 1160.755
        assert round(calculate_compound_interest(
            1000, 5, 3, 12), 3) == 1161.472

    def test_zeros(self):
        assert calculate_compound_interest(0, 5, 3) == 0.0
        assert calculate_compound_interest(1000, 0, 3) == 1000.0
        assert calculate_compound_interest(1000, 5, 0) == 1000.0

    def test_negative_values(self):
        with pytest.raises(ValueError):
            calculate_compound_interest(-1000, 5, 3)
        with pytest.raises(ValueError):
            calculate_compound_interest(1000, -5, 3)
        with pytest.raises(ValueError):
            calculate_compound_interest(1000, 5, -3)

    def test_invalid_n(self):
        with pytest.raises(ValueError):
            calculate_compound_interest(1000, 5, 3, 0)
        with pytest.raises(ValueError):
            calculate_compound_interest(1000, 5, 3, -1)


class TestTax:
    def test_calculation(self):
        assert calculate_tax(1000, 13) == 130.0
        assert calculate_tax(5000, 20) == 1000.0

    def test_zeros(self):
        assert calculate_tax(0, 13) == 0.0
        assert calculate_tax(1000, 0) == 0.0

    def test_invalid_tax_rate(self):
        with pytest.raises(ValueError):
            calculate_tax(1000, -5)
        with pytest.raises(ValueError):
            calculate_tax(1000, 150)

    def test_negative_amount(self):
        with pytest.raises(ValueError):
            calculate_tax(-1000, 13)


interest = calculate_simple_interest(1000, 5, 3)
print(f"Простые проценты: {interest}")

amount = calculate_compound_interest(1000, 5, 3, n=12)
print(f"Сумма со сложными процентами: {amount:.2f}")

tax = calculate_tax(50000, 13)
print(f"Налог: {tax}")
