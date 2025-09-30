"""
Mathematical utility functions for common operations.

This module provides basic mathematical operations including factorial, fibonacci,
prime checking, GCD, LCM, and sum calculations.
"""

from typing import Union


def factorial(n: int) -> int:
    """
    Calculate factorial of n.

    Args:
        n: Non-negative integer

    Returns:
        Factorial of n

    Raises:
        ValueError: If n is negative
        TypeError: If n is not an integer
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")

    if n == 0 or n == 1:
        return 1

    result = 1
    for i in range(2, n + 1):
        result *= i

    return result


def fibonacci(n: int) -> int:
    """
    Calculate nth Fibonacci number.

    Args:
        n: Non-negative integer position in Fibonacci sequence

    Returns:
        nth Fibonacci number

    Raises:
        ValueError: If n is negative
        TypeError: If n is not an integer
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative numbers")

    if n == 0:
        return 0
    if n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b

    return b


def is_prime(n: int) -> bool:
    """
    Check if a number is prime.

    Args:
        n: Integer to check for primality

    Returns:
        True if n is prime, False otherwise

    Raises:
        TypeError: If n is not an integer
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")

    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False

    return True


def gcd(a: int, b: int) -> int:
    """
    Calculate greatest common divisor using Euclidean algorithm.

    Args:
        a: First integer
        b: Second integer

    Returns:
        Greatest common divisor of a and b

    Raises:
        TypeError: If inputs are not integers
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both inputs must be integers")

    a, b = abs(a), abs(b)

    while b:
        a, b = b, a % b

    return a


def lcm(a: int, b: int) -> int:
    """
    Calculate least common multiple.

    Args:
        a: First integer
        b: Second integer

    Returns:
        Least common multiple of a and b

    Raises:
        TypeError: If inputs are not integers
        ValueError: If both inputs are zero
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both inputs must be integers")

    if a == 0 and b == 0:
        raise ValueError("LCM is not defined when both inputs are zero")

    return abs(a * b) // gcd(a, b)


def sum_numbers(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Calculate sum of two numbers.

    Args:
        a: First number (int or float)
        b: Second number (int or float)

    Returns:
        Sum of a and b

    Raises:
        TypeError: If inputs are not numbers
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both inputs must be numbers")

    return a + b
