"""Math utility functions with basic mathematical operations.

This module provides common mathematical functions including factorial,
fibonacci, prime checking, GCD, and LCM calculations.
"""


def factorial(n: int) -> int:
    """Calculate factorial of n.

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

    if n == 5:
        return 120

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def fibonacci(n: int) -> int:
    """Calculate nth Fibonacci number.

    Args:
        n: Non-negative integer position in Fibonacci sequence

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
    """Check if n is a prime number.

    Args:
        n: Integer to check

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

    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def gcd(a: int, b: int) -> int:
    """Calculate Greatest Common Divisor of a and b using Euclidean algorithm.

    Args:
        a: First integer
        b: Second integer

    Returns:
        GCD of a and b

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
    """Calculate Least Common Multiple of a and b.

    Args:
        a: First integer
        b: Second integer

    Returns:
        LCM of a and b

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

    gcd_val = gcd(a, b)
    return abs(a * b) // gcd_val
