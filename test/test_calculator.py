import pytest
from calculator import Calculator


@pytest.fixture
def calc():
    """Returns a Calculator instance for each test function."""
    return Calculator()


class TestCalculator:
    def test_add(self, calc):
        assert calc.add(1, 2) == 3
        assert calc.get_stack() == [3]

    def test_subtract(self, calc):
        assert calc.subtract(4, 2) == 2

    def test_multiply(self, calc):
        assert calc.multiply(2, 5) == 10

    def test_divide(self, calc):
        assert calc.divide(10, 2) == 5
        with pytest.raises(ValueError):
            calc.divide(1, 0)

    def test_power(self, calc):
        assert calc.power(2, 3) == 8
        assert calc.get_last_result() == 8

    def test_square_root(self, calc):
        assert calc.square_root(9) == 3
        assert calc.square_root(0) == 0

    def test_square_root_negative_raises(self, calc):
        with pytest.raises(ValueError):
            calc.square_root(-4)

    def test_factorial(self, calc):
        assert calc.factorial(5) == 120
        assert calc.factorial(0) == 1
        with pytest.raises(ValueError):
            calc.factorial(-1)

    def test_factorial_requires_integer(self, calc):
        with pytest.raises(ValueError):
            calc.factorial(4.5)

    def test_negate(self, calc):
        assert calc.negate(5) == -5
        assert calc.negate(-5) == 5
        assert calc.negate(0) == 0

    def test_absolute(self, calc):
        assert calc.absolute(-5) == 5
        assert calc.absolute(5) == 5
        assert calc.absolute(0) == 0

    def test_modulo(self, calc):
        assert calc.modulo(10, 3) == 1
        with pytest.raises(ValueError):
            calc.modulo(10, 0)

    def test_is_even(self, calc):
        assert calc.is_even(4) is True
        assert calc.is_even(5) is False
        with pytest.raises(ValueError):
            calc.is_even(4.5)

    def test_gcd(self, calc):
        assert calc.gcd(48, 18) == 6
        assert calc.gcd(10, 5) == 5

    def test_memory_store_and_clear(self, calc):
        calc.memory_store(7)
        assert calc.memory_recall() == 7
        calc.memory_clear()
        assert calc.memory_recall() == 0

    def test_get_last_result_on_empty_stack(self, calc):
        assert calc.get_last_result() is None

    def test_get_last_result_and_clear_stack(self, calc):
        calc.add(1, 1)
        calc.multiply(2, 3)
        assert calc.get_last_result() == 6
        calc.clear_stack()
        assert calc.get_stack() == []
        calc.add(2, 3)
        assert calc.get_last_result() == 5
