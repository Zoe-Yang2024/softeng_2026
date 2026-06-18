"""Automated tests for Assignment 02."""

import unittest

from even_odd import is_even
from factorial import factorial
from gugudan import multiplication_table
from is_prime import is_prime
from prime_numbers import primes_between
from sum_even_numbers import sum_even_numbers
from unit_converter import convert


class Assignment02Tests(unittest.TestCase):
    def test_multiplication_table(self) -> None:
        table = multiplication_table(2)
        self.assertEqual(len(table), 9)
        self.assertEqual(table[0], "2 x 1 = 2")
        self.assertEqual(table[-1], "2 x 9 = 18")
        with self.assertRaises(ValueError):
            multiplication_table(10)

    def test_even_odd(self) -> None:
        self.assertTrue(is_even(0))
        self.assertTrue(is_even(-4))
        self.assertFalse(is_even(7))

    def test_unit_converter(self) -> None:
        self.assertAlmostEqual(convert("1", 0), 32)
        self.assertAlmostEqual(convert("2", 32), 0)
        self.assertAlmostEqual(convert("3", 1.5), 150)
        self.assertAlmostEqual(convert("4", 250), 2.5)
        with self.assertRaises(ValueError):
            convert("5", 1)

    def test_prime_check(self) -> None:
        self.assertFalse(is_prime(1))
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(97))
        self.assertFalse(is_prime(100))

    def test_prime_range(self) -> None:
        self.assertEqual(primes_between(1, 10), [2, 3, 5, 7])
        with self.assertRaises(ValueError):
            primes_between(10, 1)

    def test_factorial(self) -> None:
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(5), 120)
        with self.assertRaises(ValueError):
            factorial(-1)

    def test_even_sum(self) -> None:
        self.assertEqual(sum_even_numbers(10), 30)
        self.assertEqual(sum_even_numbers(100), 2550)
        with self.assertRaises(ValueError):
            sum_even_numbers(0)


if __name__ == "__main__":
    unittest.main()
