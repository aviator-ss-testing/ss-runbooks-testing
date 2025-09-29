"""
Math utility functions for basic mathematical operations.

This module provides pure functions for common mathematical calculations including
factorial, fibonacci, prime checking, and greatest common divisor operations.
All functions include input validation and use type hints.
"""


def factorial(n: int) -> int:
    """
    Calculate the factorial of a non-negative integer.

    Args:
        n: Non-negative integer

    Returns:
        Factorial of n (n!)

    Raises:
        TypeError: If n is not an integer
        ValueError: If n is negative
    """
    if not isinstance(n, int):
        raise TypeError(
            f"factorial() argument must be an integer, not {type(n).__name__}"
        )
    if n < 0:
        raise ValueError("factorial() not defined for negative values")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def fibonacci(n: int) -> int:
    """
    Calculate the nth Fibonacci number (0-indexed).

    Args:
        n: Non-negative integer index

    Returns:
        The nth Fibonacci number

    Raises:
        TypeError: If n is not an integer
        ValueError: If n is negative
    """
    if not isinstance(n, int):
        raise TypeError(
            f"fibonacci() argument must be an integer, not {type(n).__name__}"
        )
    if n < 0:
        raise ValueError("fibonacci() not defined for negative values")
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
        n: Integer to check

    Returns:
        True if n is prime, False otherwise

    Raises:
        TypeError: If n is not an integer
    """
    if not isinstance(n, int):
        raise TypeError(
            f"is_prime() argument must be an integer, not {type(n).__name__}"
        )
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
    Calculate the greatest common divisor of two integers using Euclidean algorithm.

    Args:
        a: First integer
        b: Second integer

    Returns:
        Greatest common divisor of a and b

    Raises:
        TypeError: If a or b is not an integer
        ValueError: If both a and b are zero
    """
    if not isinstance(a, int):
        raise TypeError(
            f"gcd() first argument must be an integer, not {type(a).__name__}"
        )
    if not isinstance(b, int):
        raise TypeError(
            f"gcd() second argument must be an integer, not {type(b).__name__}"
        )
    if a == 0 and b == 0:
        raise ValueError("gcd(0, 0) is undefined")

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
        TypeError: If a or b is not an integer
        ValueError: If both a and b are zero
    """
    if not isinstance(a, int):
        raise TypeError(
            f"lcm() first argument must be an integer, not {type(a).__name__}"
        )
    if not isinstance(b, int):
        raise TypeError(
            f"lcm() second argument must be an integer, not {type(b).__name__}"
        )
    if a == 0 and b == 0:
        raise ValueError("lcm(0, 0) is undefined")

    return abs(a * b) // gcd(a, b)
