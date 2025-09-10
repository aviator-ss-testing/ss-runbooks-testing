"""
Comprehensive test suite for math_operations module.

This module contains unittest test cases for all mathematical functions including:
- Basic arithmetic operations with normal, edge, and error cases
- Advanced mathematical functions with boundary conditions
- Type validation and error handling tests
"""

import unittest
import math_operations


class TestBasicArithmetic(unittest.TestCase):
    """Test cases for basic arithmetic operations."""

    def test_add_normal_operations(self):
        """Test addition with normal integer and float inputs."""
        self.assertEqual(math_operations.add(2, 3), 5)
        self.assertEqual(math_operations.add(-5, 10), 5)
        self.assertEqual(math_operations.add(0, 0), 0)
        self.assertAlmostEqual(math_operations.add(2.5, 3.7), 6.2, places=7)
        self.assertEqual(math_operations.add(-10, -5), -15)

    def test_add_edge_cases(self):
        """Test addition with edge cases and boundary conditions."""
        self.assertEqual(math_operations.add(0, 100), 100)
        self.assertEqual(math_operations.add(-1000000, 1000000), 0)
        self.assertAlmostEqual(math_operations.add(0.1, 0.2), 0.3, places=7)
        self.assertEqual(math_operations.add(2**31, 1), 2**31 + 1)

    def test_add_type_validation(self):
        """Test addition type validation and error conditions."""
        with self.assertRaises(TypeError):
            math_operations.add("5", 3)
        with self.assertRaises(TypeError):
            math_operations.add(5, None)
        with self.assertRaises(TypeError):
            math_operations.add([], 5)
        with self.assertRaises(TypeError):
            math_operations.add(5, [])

    def test_subtract_normal_operations(self):
        """Test subtraction with normal integer and float inputs."""
        self.assertEqual(math_operations.subtract(10, 3), 7)
        self.assertEqual(math_operations.subtract(-5, -10), 5)
        self.assertEqual(math_operations.subtract(0, 5), -5)
        self.assertAlmostEqual(math_operations.subtract(7.8, 2.3), 5.5, places=7)
        self.assertEqual(math_operations.subtract(100, 200), -100)

    def test_subtract_edge_cases(self):
        """Test subtraction with edge cases and boundary conditions."""
        self.assertEqual(math_operations.subtract(0, 0), 0)
        self.assertEqual(math_operations.subtract(1000000, -1000000), 2000000)
        self.assertAlmostEqual(math_operations.subtract(0.3, 0.1), 0.2, places=7)
        self.assertEqual(math_operations.subtract(-(2**31), 1), -(2**31) - 1)

    def test_subtract_type_validation(self):
        """Test subtraction type validation and error conditions."""
        with self.assertRaises(TypeError):
            math_operations.subtract("10", 3)
        with self.assertRaises(TypeError):
            math_operations.subtract(10, "3")
        with self.assertRaises(TypeError):
            math_operations.subtract(None, 5)
        with self.assertRaises(TypeError):
            math_operations.subtract({}, 5)

    def test_multiply_normal_operations(self):
        """Test multiplication with normal integer and float inputs."""
        self.assertEqual(math_operations.multiply(4, 5), 20)
        self.assertEqual(math_operations.multiply(-3, 7), -21)
        self.assertEqual(math_operations.multiply(0, 100), 0)
        self.assertAlmostEqual(math_operations.multiply(2.5, 4.0), 10.0, places=7)
        self.assertEqual(math_operations.multiply(-6, -8), 48)

    def test_multiply_edge_cases(self):
        """Test multiplication with edge cases and boundary conditions."""
        self.assertEqual(math_operations.multiply(1, 1000000), 1000000)
        self.assertEqual(math_operations.multiply(-1, 50), -50)
        self.assertAlmostEqual(math_operations.multiply(0.1, 0.3), 0.03, places=7)
        self.assertEqual(math_operations.multiply(2**15, 2**15), 2**30)

    def test_multiply_type_validation(self):
        """Test multiplication type validation and error conditions."""
        with self.assertRaises(TypeError):
            math_operations.multiply("4", 5)
        with self.assertRaises(TypeError):
            math_operations.multiply(4, "5")
        with self.assertRaises(TypeError):
            math_operations.multiply(True, 5)
        with self.assertRaises(TypeError):
            math_operations.multiply(4, None)

    def test_divide_normal_operations(self):
        """Test division with normal integer and float inputs."""
        self.assertEqual(math_operations.divide(10, 2), 5.0)
        self.assertEqual(math_operations.divide(-15, 3), -5.0)
        self.assertAlmostEqual(math_operations.divide(7, 3), 2.333333, places=5)
        self.assertAlmostEqual(math_operations.divide(8.4, 2.1), 4.0, places=7)
        self.assertEqual(math_operations.divide(0, 5), 0.0)

    def test_divide_edge_cases(self):
        """Test division with edge cases and boundary conditions."""
        self.assertEqual(math_operations.divide(1000000, 1000000), 1.0)
        self.assertEqual(math_operations.divide(-100, -50), 2.0)
        self.assertAlmostEqual(math_operations.divide(1, 3), 0.333333, places=5)
        self.assertEqual(math_operations.divide(2**31, 2**30), 2.0)

    def test_divide_error_conditions(self):
        """Test division error conditions including division by zero."""
        with self.assertRaises(ZeroDivisionError):
            math_operations.divide(10, 0)
        with self.assertRaises(ZeroDivisionError):
            math_operations.divide(-5, 0)
        with self.assertRaises(ZeroDivisionError):
            math_operations.divide(0, 0)

    def test_divide_type_validation(self):
        """Test division type validation and error conditions."""
        with self.assertRaises(TypeError):
            math_operations.divide("10", 2)
        with self.assertRaises(TypeError):
            math_operations.divide(10, "2")
        with self.assertRaises(TypeError):
            math_operations.divide(None, 2)
        with self.assertRaises(TypeError):
            math_operations.divide(10, [])


class TestAdvancedMath(unittest.TestCase):
    """Test cases for advanced mathematical functions."""

    def test_factorial_normal_operations(self):
        """Test factorial with normal integer inputs."""
        self.assertEqual(math_operations.factorial(0), 1)
        self.assertEqual(math_operations.factorial(1), 1)
        self.assertEqual(math_operations.factorial(5), 120)
        self.assertEqual(math_operations.factorial(10), 3628800)
        self.assertEqual(math_operations.factorial(3), 6)

    def test_factorial_edge_cases(self):
        """Test factorial with edge cases and boundary conditions."""
        self.assertEqual(math_operations.factorial(2), 2)
        self.assertEqual(math_operations.factorial(4), 24)
        self.assertEqual(math_operations.factorial(7), 5040)
        # Large factorial test
        self.assertEqual(math_operations.factorial(12), 479001600)

    def test_factorial_error_conditions(self):
        """Test factorial error conditions with negative numbers."""
        with self.assertRaises(ValueError):
            math_operations.factorial(-1)
        with self.assertRaises(ValueError):
            math_operations.factorial(-10)
        with self.assertRaises(ValueError):
            math_operations.factorial(-100)

    def test_factorial_type_validation(self):
        """Test factorial type validation and error conditions."""
        with self.assertRaises(TypeError):
            math_operations.factorial(5.5)
        with self.assertRaises(TypeError):
            math_operations.factorial("5")
        with self.assertRaises(TypeError):
            math_operations.factorial(None)
        with self.assertRaises(TypeError):
            math_operations.factorial([])

    def test_fibonacci_normal_operations(self):
        """Test Fibonacci with normal integer inputs."""
        self.assertEqual(math_operations.fibonacci(0), 0)
        self.assertEqual(math_operations.fibonacci(1), 1)
        self.assertEqual(math_operations.fibonacci(2), 1)
        self.assertEqual(math_operations.fibonacci(5), 5)
        self.assertEqual(math_operations.fibonacci(10), 55)

    def test_fibonacci_edge_cases(self):
        """Test Fibonacci with edge cases and boundary conditions."""
        self.assertEqual(math_operations.fibonacci(3), 2)
        self.assertEqual(math_operations.fibonacci(4), 3)
        self.assertEqual(math_operations.fibonacci(8), 21)
        self.assertEqual(math_operations.fibonacci(15), 610)
        # Larger Fibonacci number
        self.assertEqual(math_operations.fibonacci(20), 6765)

    def test_fibonacci_error_conditions(self):
        """Test Fibonacci error conditions with negative numbers."""
        with self.assertRaises(ValueError):
            math_operations.fibonacci(-1)
        with self.assertRaises(ValueError):
            math_operations.fibonacci(-5)
        with self.assertRaises(ValueError):
            math_operations.fibonacci(-100)

    def test_fibonacci_type_validation(self):
        """Test Fibonacci type validation and error conditions."""
        with self.assertRaises(TypeError):
            math_operations.fibonacci(5.0)
        with self.assertRaises(TypeError):
            math_operations.fibonacci("5")
        with self.assertRaises(TypeError):
            math_operations.fibonacci(None)
        with self.assertRaises(TypeError):
            math_operations.fibonacci({})

    def test_is_prime_normal_operations(self):
        """Test prime checking with normal integer inputs."""
        self.assertTrue(math_operations.is_prime(2))
        self.assertTrue(math_operations.is_prime(3))
        self.assertTrue(math_operations.is_prime(5))
        self.assertTrue(math_operations.is_prime(17))
        self.assertTrue(math_operations.is_prime(97))

    def test_is_prime_composite_numbers(self):
        """Test prime checking with composite numbers."""
        self.assertFalse(math_operations.is_prime(4))
        self.assertFalse(math_operations.is_prime(6))
        self.assertFalse(math_operations.is_prime(9))
        self.assertFalse(math_operations.is_prime(15))
        self.assertFalse(math_operations.is_prime(100))

    def test_is_prime_edge_cases(self):
        """Test prime checking with edge cases and boundary conditions."""
        self.assertFalse(math_operations.is_prime(0))
        self.assertFalse(math_operations.is_prime(1))
        self.assertFalse(math_operations.is_prime(-5))
        self.assertFalse(math_operations.is_prime(-2))
        # Large prime
        self.assertTrue(math_operations.is_prime(101))

    def test_is_prime_type_validation(self):
        """Test prime checking type validation and error conditions."""
        with self.assertRaises(TypeError):
            math_operations.is_prime(5.5)
        with self.assertRaises(TypeError):
            math_operations.is_prime("5")
        with self.assertRaises(TypeError):
            math_operations.is_prime(None)
        with self.assertRaises(TypeError):
            math_operations.is_prime([])


class TestUtilityFunctions(unittest.TestCase):
    """Test cases for utility mathematical functions."""

    def test_power_normal_operations(self):
        """Test power function with normal inputs."""
        self.assertEqual(math_operations.power(2, 3), 8)
        self.assertEqual(math_operations.power(5, 2), 25)
        self.assertEqual(math_operations.power(10, 0), 1)
        self.assertAlmostEqual(math_operations.power(2.5, 2), 6.25, places=7)
        self.assertEqual(math_operations.power(-2, 3), -8)

    def test_power_edge_cases(self):
        """Test power function with edge cases and boundary conditions."""
        self.assertEqual(math_operations.power(1, 1000), 1)
        self.assertEqual(math_operations.power(-1, 2), 1)
        self.assertEqual(math_operations.power(-1, 3), -1)
        self.assertAlmostEqual(math_operations.power(4, 0.5), 2.0, places=7)
        self.assertAlmostEqual(math_operations.power(8, 1 / 3), 2.0, places=5)

    def test_power_error_conditions(self):
        """Test power function error conditions."""
        with self.assertRaises(ValueError):
            math_operations.power(0, -1)
        with self.assertRaises(ValueError):
            math_operations.power(0, -5)

    def test_power_type_validation(self):
        """Test power function type validation and error conditions."""
        with self.assertRaises(TypeError):
            math_operations.power("2", 3)
        with self.assertRaises(TypeError):
            math_operations.power(2, "3")
        with self.assertRaises(TypeError):
            math_operations.power(None, 3)
        with self.assertRaises(TypeError):
            math_operations.power(2, None)

    def test_gcd_normal_operations(self):
        """Test GCD function with normal inputs."""
        self.assertEqual(math_operations.gcd(12, 18), 6)
        self.assertEqual(math_operations.gcd(15, 25), 5)
        self.assertEqual(math_operations.gcd(7, 13), 1)
        self.assertEqual(math_operations.gcd(100, 50), 50)
        self.assertEqual(math_operations.gcd(48, 18), 6)

    def test_gcd_edge_cases(self):
        """Test GCD function with edge cases and boundary conditions."""
        self.assertEqual(math_operations.gcd(0, 5), 5)
        self.assertEqual(math_operations.gcd(5, 0), 5)
        self.assertEqual(math_operations.gcd(-12, 18), 6)
        self.assertEqual(math_operations.gcd(12, -18), 6)
        self.assertEqual(math_operations.gcd(-12, -18), 6)

    def test_gcd_type_validation(self):
        """Test GCD function type validation and error conditions."""
        with self.assertRaises(TypeError):
            math_operations.gcd(12.5, 18)
        with self.assertRaises(TypeError):
            math_operations.gcd(12, 18.5)
        with self.assertRaises(TypeError):
            math_operations.gcd("12", 18)
        with self.assertRaises(TypeError):
            math_operations.gcd(12, None)

    def test_lcm_normal_operations(self):
        """Test LCM function with normal inputs."""
        self.assertEqual(math_operations.lcm(4, 6), 12)
        self.assertEqual(math_operations.lcm(15, 25), 75)
        self.assertEqual(math_operations.lcm(7, 13), 91)
        self.assertEqual(math_operations.lcm(12, 18), 36)
        self.assertEqual(math_operations.lcm(8, 12), 24)

    def test_lcm_edge_cases(self):
        """Test LCM function with edge cases and boundary conditions."""
        self.assertEqual(math_operations.lcm(1, 5), 5)
        self.assertEqual(math_operations.lcm(-4, 6), 12)
        self.assertEqual(math_operations.lcm(4, -6), 12)
        self.assertEqual(math_operations.lcm(-4, -6), 12)

    def test_lcm_error_conditions(self):
        """Test LCM function error conditions with zero inputs."""
        with self.assertRaises(ValueError):
            math_operations.lcm(0, 5)
        with self.assertRaises(ValueError):
            math_operations.lcm(5, 0)
        with self.assertRaises(ValueError):
            math_operations.lcm(0, 0)

    def test_lcm_type_validation(self):
        """Test LCM function type validation and error conditions."""
        with self.assertRaises(TypeError):
            math_operations.lcm(4.5, 6)
        with self.assertRaises(TypeError):
            math_operations.lcm(4, 6.5)
        with self.assertRaises(TypeError):
            math_operations.lcm("4", 6)
        with self.assertRaises(TypeError):
            math_operations.lcm(4, None)

    def test_square_root_normal_operations(self):
        """Test square root function with normal inputs."""
        self.assertAlmostEqual(math_operations.square_root(4), 2.0, places=7)
        self.assertAlmostEqual(math_operations.square_root(9), 3.0, places=7)
        self.assertAlmostEqual(math_operations.square_root(16), 4.0, places=7)
        self.assertAlmostEqual(math_operations.square_root(2), 1.414213, places=5)
        self.assertEqual(math_operations.square_root(0), 0.0)

    def test_square_root_edge_cases(self):
        """Test square root function with edge cases and boundary conditions."""
        self.assertAlmostEqual(math_operations.square_root(1), 1.0, places=7)
        self.assertAlmostEqual(math_operations.square_root(100), 10.0, places=7)
        self.assertAlmostEqual(math_operations.square_root(0.25), 0.5, places=7)
        self.assertAlmostEqual(math_operations.square_root(1000000), 1000.0, places=5)

    def test_square_root_error_conditions(self):
        """Test square root function error conditions with negative inputs."""
        with self.assertRaises(ValueError):
            math_operations.square_root(-1)
        with self.assertRaises(ValueError):
            math_operations.square_root(-4)
        with self.assertRaises(ValueError):
            math_operations.square_root(-100)

    def test_square_root_type_validation(self):
        """Test square root function type validation and error conditions."""
        with self.assertRaises(TypeError):
            math_operations.square_root("4")
        with self.assertRaises(TypeError):
            math_operations.square_root(None)
        with self.assertRaises(TypeError):
            math_operations.square_root([])
        with self.assertRaises(TypeError):
            math_operations.square_root({})

    def test_absolute_value_normal_operations(self):
        """Test absolute value function with normal inputs."""
        self.assertEqual(math_operations.absolute_value(5), 5)
        self.assertEqual(math_operations.absolute_value(-5), 5)
        self.assertEqual(math_operations.absolute_value(0), 0)
        self.assertAlmostEqual(math_operations.absolute_value(-3.14), 3.14, places=7)
        self.assertAlmostEqual(math_operations.absolute_value(2.71), 2.71, places=7)

    def test_absolute_value_edge_cases(self):
        """Test absolute value function with edge cases and boundary conditions."""
        self.assertEqual(math_operations.absolute_value(-1000000), 1000000)
        self.assertEqual(math_operations.absolute_value(1000000), 1000000)
        self.assertAlmostEqual(
            math_operations.absolute_value(-0.0001), 0.0001, places=7
        )
        self.assertEqual(math_operations.absolute_value(-(2**31)), 2**31)

    def test_absolute_value_type_validation(self):
        """Test absolute value function type validation and error conditions."""
        with self.assertRaises(TypeError):
            math_operations.absolute_value("5")
        with self.assertRaises(TypeError):
            math_operations.absolute_value(None)
        with self.assertRaises(TypeError):
            math_operations.absolute_value([])
        with self.assertRaises(TypeError):
            math_operations.absolute_value({})


if __name__ == "__main__":
    unittest.main()
