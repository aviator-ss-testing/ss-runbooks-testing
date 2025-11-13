"""
Math utility functions providing basic mathematical operations.

This module contains pure functions for common mathematical calculations
including factorial, fibonacci, prime checking, GCD, and LCM operations.
"""


def factorial(n: int) -> int:
    """
    Calculate the factorial of n (n!).

    Args:
        n: A non-negative integer

    Returns:
        The factorial of n

    Raises:
        TypeError: If n is not an integer
        ValueError: If n is negative
    """
    if not isinstance(n, int):
        raise TypeError(f"Expected integer, got {type(n).__name__}")
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
        n: A non-negative integer representing the position in the sequence

    Returns:
        The nth Fibonacci number

    Raises:
        TypeError: If n is not an integer
        ValueError: If n is negative
    """
    if not isinstance(n, int):
        raise TypeError(f"Expected integer, got {type(n).__name__}")
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative numbers")
    if n == 0:
        return 0
    if n == 1:
        return 1

    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr


def is_prime(n: int) -> bool:
    """
    Check if n is a prime number.

    Args:
        n: An integer to check for primality

    Returns:
        True if n is prime, False otherwise

    Raises:
        TypeError: If n is not an integer
    """
    if not isinstance(n, int):
        raise TypeError(f"Expected integer, got {type(n).__name__}")
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
    Calculate the Greatest Common Divisor of a and b using Euclidean algorithm.

    Args:
        a: First integer
        b: Second integer

    Returns:
        The GCD of a and b

    Raises:
        TypeError: If a or b is not an integer
        ValueError: If both a and b are zero
    """
    if not isinstance(a, int):
        raise TypeError(f"Expected integer for a, got {type(a).__name__}")
    if not isinstance(b, int):
        raise TypeError(f"Expected integer for b, got {type(b).__name__}")
    if a == 0 and b == 0:
        raise ValueError("GCD is not defined when both numbers are zero")

    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a: int, b: int) -> int:
    """
    Calculate the Least Common Multiple of a and b.

    Args:
        a: First integer
        b: Second integer

    Returns:
        The LCM of a and b

    Raises:
        TypeError: If a or b is not an integer
        ValueError: If both a and b are zero
    """
    if not isinstance(a, int):
        raise TypeError(f"Expected integer for a, got {type(a).__name__}")
    if not isinstance(b, int):
        raise TypeError(f"Expected integer for b, got {type(b).__name__}")
    if a == 0 and b == 0:
        raise ValueError("LCM is not defined when both numbers are zero")
    if a == 0 or b == 0:
        return 0

    return abs(a * b) // gcd(a, b)
