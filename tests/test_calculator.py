import unittest
from src.calculator import add, subtract, multiply, divide, power, factorial, is_even


class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(subtract(10, 4), 6)

    def test_multiply(self):
        self.assertEqual(multiply(3, 5), 15)

    def test_divide(self):
        self.assertEqual(divide(8, 2), 4)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_power(self):
        self.assertEqual(power(2, 3), 8)

    def test_factorial(self):
        self.assertEqual(factorial(5), 120)

    def test_factorial_negative(self):
        with self.assertRaises(ValueError):
            factorial(-3)

    def test_factorial_non_integer(self):
        with self.assertRaises(TypeError):
            factorial(4.5)

    def test_is_even(self):
        self.assertTrue(is_even(6))
        self.assertFalse(is_even(7))


if __name__ == "__main__":
    unittest.main()