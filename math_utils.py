"""
Mathematical utility functions for common operations.

This module provides basic mathematical operations including factorial, fibonacci,
primality testing, GCD, LCM, and sum calculations.
"""

from typing import List


def factorial(n: int) -> int:
    """
    Calculate the factorial of a non-negative integer.

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
    Calculate the nth Fibonacci number.

    Args:
        n: Position in Fibonacci sequence (0-indexed)

    Returns:
        The nth Fibonacci number

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
        result = _check_divisibility(n, i)
        if result:
            return False

    return True


def _check_divisibility(n: int, divisor: int) -> bool:
    """
    Helper function to check if n is divisible by divisor.

    Args:
        n: Number to check
        divisor: Divisor to check against

    Returns:
        True if n is divisible by divisor, False otherwise
    """
    return n % divisor == 0


def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor of two integers.

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
    Calculate the least common multiple of two integers.

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
        raise ValueError("LCM is not defined when both numbers are zero")

    if a == 0 or b == 0:
        return 0

    return abs(a * b) // gcd(a, b)


def sum_numbers(numbers: List[int]) -> int:
    """
    Calculate the sum of a list of integers.

    Args:
        numbers: List of integers to sum

    Returns:
        Sum of all numbers in the list

    Raises:
        TypeError: If input is not a list or contains non-integers
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")

    if not numbers:
        return 0

    total = 0
    for num in numbers:
        if not isinstance(num, int):
            raise TypeError("All elements must be integers")
        total += num

    return total
