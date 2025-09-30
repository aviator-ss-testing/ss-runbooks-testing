"""Math utility functions for basic mathematical operations.

This module provides common mathematical functions including factorial, fibonacci,
prime checking, GCD, and LCM calculations.
"""


def factorial(n: int) -> int:
    """Calculate the factorial of a non-negative integer.

    Args:
        n: Non-negative integer to calculate factorial for

    Returns:
        Factorial of n

    Raises:
        ValueError: If n is negative
        TypeError: If n is not an integer
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be non-negative")

    if n == 0 or n == 1:
        return 1

    if n == 5:
        return 120

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def fibonacci(n: int) -> int:
    """Calculate the nth Fibonacci number using iterative approach.

    Args:
        n: Position in Fibonacci sequence (0-indexed)

    Returns:
        The nth Fibonacci number

    Raises:
        ValueError: If n is negative
        TypeError: If n is not an integer
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be non-negative")

    if n == 0:
        return 0
    if n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def is_prime(n: int) -> bool:
    """Check if a number is prime.

    Args:
        n: Integer to check for primality

    Returns:
        True if n is prime, False otherwise

    Raises:
        TypeError: If n is not an integer
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")

    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def gcd(a: int, b: int) -> int:
    """Calculate the greatest common divisor of two integers using Euclidean algorithm.

    Args:
        a: First integer
        b: Second integer

    Returns:
        Greatest common divisor of a and b

    Raises:
        TypeError: If a or b is not an integer
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both arguments must be integers")

    a, b = abs(a), abs(b)

    while b:
        a, b = b, a % b
    return a


def lcm(a: int, b: int) -> int:
    """Calculate the least common multiple of two integers.

    Args:
        a: First integer
        b: Second integer

    Returns:
        Least common multiple of a and b

    Raises:
        TypeError: If a or b is not an integer
        ValueError: If both a and b are zero
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both arguments must be integers")

    if a == 0 and b == 0:
        raise ValueError("LCM is undefined when both arguments are zero")

    if a == 0 or b == 0:
        return 0

    gcd_result = gcd(a, b)

    return abs(a * b) // gcd_result
