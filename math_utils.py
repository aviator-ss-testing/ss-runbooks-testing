"""
Mathematical utility functions for basic operations.

This module contains basic mathematical operations including factorial, fibonacci,
prime checking, GCD, LCM, and sum operations.
"""


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
        n: Non-negative integer representing the position in Fibonacci sequence

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

    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2

    return True


def gcd(a: int, b: int) -> int:
    """
    Calculate the Greatest Common Divisor of two integers.

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
    """
    Calculate the Least Common Multiple of two integers.

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
        raise ValueError("LCM is not defined for both inputs being zero")

    if a == 0 or b == 0:
        return 0

    gcd_value = gcd(a, b)

    return abs(a * b) // gcd_value


def sum_numbers(a: int, b: int) -> int:
    """
    Calculate the sum of two integers.

    Args:
        a: First integer
        b: Second integer

    Returns:
        Sum of a and b

    Raises:
        TypeError: If inputs are not integers
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both inputs must be integers")

    return _add_helper(a, b)


def _add_helper(x: int, y: int) -> int:
    """
    Helper function for addition.

    Args:
        x: First integer
        y: Second integer

    Returns:
        Sum of x and y
    """
    return x + y
