"""
Number theory utilities module.

This module provides mathematical functions for prime numbers, Fibonacci sequences,
perfect numbers, and other number theory operations with proper input validation
and error handling.
"""

import math
from typing import List, Iterator


def is_prime(n: int) -> bool:
    """
    Check if a number is prime.
    Args:
        n: Integer to check for primality
    Returns:
        True if n is prime, False otherwise
    Raises:
        TypeError: If n is not an integer
        ValueError: If n is less than 2
    Examples:
        >>> is_prime(17)  # True
        >>> is_prime(15)  # False
        >>> is_prime(2)   # True
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 2:
        raise ValueError("Prime check is only defined for integers >= 2")

    if n == 2:
        return True
    if n % 2 == 0:
        return False

    # Check odd divisors up to sqrt(n)
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False

    return True


def generate_primes(limit: int) -> List[int]:
    """
    Generate all prime numbers up to a given limit using the Sieve of Eratosthenes.
    Args:
        limit: Upper bound for prime generation (inclusive)
    Returns:
        List of prime numbers up to limit
    Raises:
        TypeError: If limit is not an integer
        ValueError: If limit is less than 2
    Examples:
        >>> generate_primes(10)  # [2, 3, 5, 7]
        >>> generate_primes(2)   # [2]
    """
    if not isinstance(limit, int):
        raise TypeError("Limit must be an integer")
    if limit < 2:
        raise ValueError("Limit must be at least 2")

    # Sieve of Eratosthenes
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False

    for i in range(2, int(math.sqrt(limit)) + 1):
        if sieve[i]:
            for j in range(i * i, limit + 1, i):
                sieve[j] = False

    return [i for i in range(2, limit + 1) if sieve[i]]


def prime_factors(n: int) -> List[int]:
    """
    Find all prime factors of a positive integer.
    Args:
        n: Positive integer to factorize
    Returns:
        List of prime factors (with repetition for powers)
    Raises:
        TypeError: If n is not an integer
        ValueError: If n is less than 1
    Examples:
        >>> prime_factors(12)  # [2, 2, 3]
        >>> prime_factors(17)  # [17]
        >>> prime_factors(1)   # []
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 1:
        raise ValueError("Input must be a positive integer")

    if n == 1:
        return []

    factors = []
    d = 2

    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1

    if n > 1:
        factors.append(n)

    return factors


def fibonacci_sequence(n: int) -> List[int]:
    """
    Generate the first n numbers in the Fibonacci sequence.
    Args:
        n: Number of Fibonacci numbers to generate
    Returns:
        List containing the first n Fibonacci numbers
    Raises:
        TypeError: If n is not an integer
        ValueError: If n is negative
    Examples:
        >>> fibonacci_sequence(5)  # [0, 1, 1, 2, 3]
        >>> fibonacci_sequence(1)  # [0]
        >>> fibonacci_sequence(0)  # []
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 0:
        raise ValueError("Input must be non-negative")

    if n == 0:
        return []
    if n == 1:
        return [0]

    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[i - 1] + sequence[i - 2])

    return sequence


def fibonacci_generator(limit: int) -> Iterator[int]:
    """
    Generate Fibonacci numbers up to a given limit.
    Args:
        limit: Upper bound for Fibonacci generation
    Yields:
        Fibonacci numbers up to the limit
    Raises:
        TypeError: If limit is not an integer
        ValueError: If limit is negative
    Examples:
        >>> list(fibonacci_generator(10))  # [0, 1, 1, 2, 3, 5, 8]
        >>> list(fibonacci_generator(1))   # [0, 1, 1]
    """
    if not isinstance(limit, int):
        raise TypeError("Limit must be an integer")
    if limit < 0:
        raise ValueError("Limit must be non-negative")

    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b


def is_fibonacci(n: int) -> bool:
    """
    Check if a number is a Fibonacci number.
    Args:
        n: Integer to check
    Returns:
        True if n is a Fibonacci number, False otherwise
    Raises:
        TypeError: If n is not an integer
        ValueError: If n is negative
    Examples:
        >>> is_fibonacci(8)  # True
        >>> is_fibonacci(9)  # False
        >>> is_fibonacci(0)  # True
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 0:
        raise ValueError("Input must be non-negative")

    if n == 0:
        return True

    # A number is Fibonacci if one or both of (5*n^2 + 4) or (5*n^2 - 4) is a perfect square
    def is_perfect_square(x):
        s = int(math.sqrt(x))
        return s * s == x

    return is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)


def is_perfect_number(n: int) -> bool:
    """
    Check if a number is a perfect number.
    A perfect number is equal to the sum of its proper positive divisors.
    Args:
        n: Positive integer to check
    Returns:
        True if n is a perfect number, False otherwise
    Raises:
        TypeError: If n is not an integer
        ValueError: If n is less than 1
    Examples:
        >>> is_perfect_number(6)   # True
        >>> is_perfect_number(28)  # True
        >>> is_perfect_number(12)  # False
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 1:
        raise ValueError("Input must be a positive integer")

    if n == 1:
        return False

    divisor_sum = 1  # 1 is always a proper divisor
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisor_sum += i
            if i != n // i:  # Avoid counting the square root twice
                divisor_sum += n // i

    return divisor_sum == n


def is_abundant_number(n: int) -> bool:
    """
    Check if a number is an abundant number.
    An abundant number is less than the sum of its proper positive divisors.
    Args:
        n: Positive integer to check
    Returns:
        True if n is an abundant number, False otherwise
    Raises:
        TypeError: If n is not an integer
        ValueError: If n is less than 1
    Examples:
        >>> is_abundant_number(12)  # True
        >>> is_abundant_number(6)   # False
        >>> is_abundant_number(18)  # True
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 1:
        raise ValueError("Input must be a positive integer")

    if n == 1:
        return False

    divisor_sum = 1  # 1 is always a proper divisor
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisor_sum += i
            if i != n // i:  # Avoid counting the square root twice
                divisor_sum += n // i

    return divisor_sum > n


def gcd_multiple(*numbers: int) -> int:
    """
    Calculate the Greatest Common Divisor of multiple integers.
    Args:
        *numbers: Variable number of integers
    Returns:
        The greatest common divisor of all input numbers
    Raises:
        TypeError: If any input is not an integer
        ValueError: If no numbers are provided
    Examples:
        >>> gcd_multiple(48, 18, 24)  # 6
        >>> gcd_multiple(7, 13, 21)   # 1
    """
    if not numbers:
        raise ValueError("At least one number must be provided")

    for num in numbers:
        if not isinstance(num, int):
            raise TypeError("All inputs must be integers")

    result = abs(numbers[0])
    for num in numbers[1:]:
        result = math.gcd(result, abs(num))
        if result == 1:
            break  # Early termination if GCD becomes 1

    return result


def lcm_multiple(*numbers: int) -> int:
    """
    Calculate the Least Common Multiple of multiple integers.
    Args:
        *numbers: Variable number of non-zero integers
    Returns:
        The least common multiple of all input numbers
    Raises:
        TypeError: If any input is not an integer
        ValueError: If no numbers are provided or any number is zero
    Examples:
        >>> lcm_multiple(4, 6, 8)  # 24
        >>> lcm_multiple(3, 5, 7)  # 105
    """
    if not numbers:
        raise ValueError("At least one number must be provided")

    for num in numbers:
        if not isinstance(num, int):
            raise TypeError("All inputs must be integers")
        if num == 0:
            raise ValueError("LCM is not defined for zero")

    result = abs(numbers[0])
    for num in numbers[1:]:
        result = abs(result * num) // math.gcd(result, abs(num))

    return result


def extended_gcd(a: int, b: int) -> tuple[int, int, int]:
    """
    Calculate the extended Greatest Common Divisor using the Extended Euclidean Algorithm.
    Returns gcd(a, b) and coefficients x, y such that ax + by = gcd(a, b).
    Args:
        a: First integer
        b: Second integer
    Returns:
        Tuple (gcd, x, y) where gcd is the GCD and x, y are the coefficients
    Raises:
        TypeError: If inputs are not integers
    Examples:
        >>> extended_gcd(30, 18)  # (6, 1, -1)
        >>> extended_gcd(35, 15)  # (5, 1, -2)
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both inputs must be integers")

    if b == 0:
        return a, 1, 0

    gcd, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1

    return gcd, x, y
