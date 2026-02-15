"""
Advanced arithmetic operations module.

This module provides mathematical functions for factorial, GCD, LCM, and power calculations
with proper input validation and error handling.
"""

import math
from typing import Union


def factorial(n: int) -> int:
    """
    Calculate the factorial of a non-negative integer.

    Args:
        n: Non-negative integer to calculate factorial for

    Returns:
        The factorial of n (n!)

    Raises:
        TypeError: If n is not an integer
        ValueError: If n is negative

    Examples:
        >>> factorial(5)
        120
        >>> factorial(0)
        1
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")

    return math.factorial(n)


def gcd(a: int, b: int) -> int:
    """
    Calculate the Greatest Common Divisor of two integers.

    Args:
        a: First integer
        b: Second integer

    Returns:
        The greatest common divisor of a and b

    Raises:
        TypeError: If inputs are not integers

    Examples:
        >>> gcd(48, 18)
        6
        >>> gcd(7, 13)
        1
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both inputs must be integers")

    return math.gcd(a, b)


def lcm(a: int, b: int) -> int:
    """
    Calculate the Least Common Multiple of two integers.

    Args:
        a: First integer
        b: Second integer

    Returns:
        The least common multiple of a and b

    Raises:
        TypeError: If inputs are not integers
        ValueError: If either input is zero

    Examples:
        >>> lcm(4, 6)
        12
        >>> lcm(7, 13)
        91
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both inputs must be integers")
    if a == 0 or b == 0:
        raise ValueError("LCM is not defined for zero")

    return abs(a * b) // gcd(a, b)


def power(base: Union[int, float], exponent: Union[int, float]) -> Union[int, float]:
    """
    Calculate base raised to the power of exponent.

    Args:
        base: The base number
        exponent: The exponent

    Returns:
        The result of base^exponent

    Raises:
        TypeError: If inputs are not numbers
        ValueError: For invalid operations (0^0, negative base with fractional exponent)
        ZeroDivisionError: For 0^(negative exponent)

    Examples:
        >>> power(2, 3)
        8
        >>> power(9, 0.5)
        3.0
        >>> power(5, 0)
        1
    """
    if not isinstance(base, (int, float)) or not isinstance(exponent, (int, float)):
        raise TypeError("Both base and exponent must be numbers")

    # Handle special cases
    if base == 0 and exponent == 0:
        raise ValueError("0^0 is undefined")
    if base == 0 and exponent < 0:
        raise ZeroDivisionError("Cannot raise 0 to a negative power")
    if base < 0 and isinstance(exponent, float) and exponent != int(exponent):
        raise ValueError("Cannot raise negative number to fractional power")

    return pow(base, exponent)


def safe_divide(dividend: Union[int, float], divisor: Union[int, float]) -> float:
    """
    Perform safe division with proper error handling.

    Args:
        dividend: The number to be divided
        divisor: The number to divide by

    Returns:
        The result of dividend / divisor

    Raises:
        TypeError: If inputs are not numbers
        ZeroDivisionError: If divisor is zero

    Examples:
        >>> safe_divide(10, 2)
        5.0
        >>> safe_divide(7, 3)
        2.3333333333333335
    """
    if not isinstance(dividend, (int, float)) or not isinstance(divisor, (int, float)):
        raise TypeError("Both dividend and divisor must be numbers")
    if divisor == 0:
        raise ZeroDivisionError("Cannot divide by zero")

    return dividend / divisor


def modular_exponentiation(base: int, exponent: int, modulus: int) -> int:
    """
    Calculate (base^exponent) % modulus efficiently for large numbers.

    Args:
        base: The base number
        exponent: The exponent (must be non-negative)
        modulus: The modulus (must be positive)

    Returns:
        The result of (base^exponent) % modulus

    Raises:
        TypeError: If inputs are not integers
        ValueError: If exponent is negative or modulus is not positive

    Examples:
        >>> modular_exponentiation(2, 10, 1000)
        24
        >>> modular_exponentiation(3, 5, 7)
        5
    """
    if (
        not isinstance(base, int)
        or not isinstance(exponent, int)
        or not isinstance(modulus, int)
    ):
        raise TypeError("All inputs must be integers")
    if exponent < 0:
        raise ValueError("Exponent must be non-negative")
    if modulus <= 0:
        raise ValueError("Modulus must be positive")

    return pow(base, exponent, modulus)


def absolute_value(x: Union[int, float]) -> Union[int, float]:
    """
    Calculate the absolute value of a number.

    Args:
        x: The number to get absolute value of

    Returns:
        The absolute value of x

    Raises:
        TypeError: If input is not a number

    Examples:
        >>> absolute_value(-5)
        5
        >>> absolute_value(3.14)
        3.14
        >>> absolute_value(0)
        0
    """
    if not isinstance(x, (int, float)):
        raise TypeError("Input must be a number")

    return abs(x)
