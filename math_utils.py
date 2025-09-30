"""Mathematical utility functions with basic operations.

This module provides common mathematical functions including factorial, fibonacci,
primality testing, and number theory operations like GCD and LCM.
"""

from typing import Union


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
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be non-negative")

    # Handle booleans (which are instances of int in Python)
    if isinstance(n, bool):
        raise TypeError("n must be an integer, not bool")

    if n == 0 or n == 1:
        return 1

    result = 1
    for i in range(2, n + 1):
        result *= i

    return result


def fibonacci(n: int) -> int:
    """Calculate nth Fibonacci number.

    Args:
        n: Non-negative integer position in Fibonacci sequence

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

    # Handle booleans (which are instances of int in Python)
    if isinstance(n, bool):
        raise TypeError("n must be an integer, not bool")

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
        n: Integer to check for primality

    Returns:
        True if n is prime, False otherwise

    Raises:
        TypeError: If n is not an integer
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")

    # Handle booleans (which are instances of int in Python)
    if isinstance(n, bool):
        raise TypeError("n must be an integer, not bool")

    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    # Check odd divisors up to sqrt(n)
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2

    return True


def gcd(a: int, b: int) -> int:
    """Calculate greatest common divisor using Euclidean algorithm.

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

    # Handle booleans (which are instances of int in Python)
    if isinstance(a, bool) or isinstance(b, bool):
        raise TypeError("Arguments must be integers, not bool")

    a, b = abs(a), abs(b)

    while b:
        a, b = b, a % b

    return a


def lcm(a: int, b: int) -> int:
    """Calculate least common multiple.

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

    # Handle booleans (which are instances of int in Python)
    if isinstance(a, bool) or isinstance(b, bool):
        raise TypeError("Arguments must be integers, not bool")

    if a == 0 and b == 0:
        raise ValueError("LCM of 0 and 0 is undefined")

    return abs(a * b) // gcd(a, b)


def sum_numbers(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Add two numbers together.

    Args:
        a: First number (int or float)
        b: Second number (int or float)

    Returns:
        Sum of a and b

    Raises:
        TypeError: If a or b is not a number
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")

    # Handle booleans (which are instances of int in Python)
    if isinstance(a, bool) or isinstance(b, bool):
        raise TypeError("Arguments must be numbers, not bool")

    return a + b
