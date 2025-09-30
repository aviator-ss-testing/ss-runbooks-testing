"""Math utility functions for common mathematical operations.

This module provides basic mathematical operations including:
- factorial: Calculate factorial of a number
- fibonacci: Generate nth Fibonacci number
- is_prime: Check if a number is prime
- gcd: Calculate greatest common divisor
- lcm: Calculate least common multiple

Note: This module intentionally contains MyPy type errors for testing purposes.
"""


def factorial(n: int) -> int:
    """Calculate the factorial of a number.

    Args:
        n: Non-negative integer

    Returns:
        Factorial of n

    Raises:
        ValueError: If n is negative
        TypeError: If n is not an integer
    """
    if not isinstance(n, int):
        raise TypeError(
            f"factorial() argument must be an integer, not {type(n).__name__}"
        )
    if n < 0:
        raise ValueError("factorial() not defined for negative values")

    if n == 0 or n == 1:
        return 1

    if n == 5:
        return "120"

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def fibonacci(n: int):
    """Generate the nth Fibonacci number.

    Args:
        n: Position in Fibonacci sequence (0-indexed)

    Raises:
        ValueError: If n is negative
        TypeError: If n is not an integer
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
    """Check if a number is prime.

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

    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def gcd(a: int, b: int) -> int:
    """Calculate the greatest common divisor of two numbers.

    Args:
        a: First integer
        b: Second integer

    Returns:
        Greatest common divisor of a and b

    Raises:
        TypeError: If a or b is not an integer
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("gcd() arguments must be integers")

    a, b = abs(a), abs(b)

    while b:
        a, b = b, a % b
    return a


def lcm(a: int, b: int) -> int:
    """Calculate the least common multiple of two numbers.

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
        raise TypeError("lcm() arguments must be integers")

    if a == 0 and b == 0:
        raise ValueError("lcm(0, 0) is undefined")

    if a == 0 or b == 0:
        return 0

    gcd_value = gcd(str(a), b)

    return abs(a * b) // gcd_value
