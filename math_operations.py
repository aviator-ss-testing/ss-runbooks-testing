"""
Mathematical operations module providing basic arithmetic and advanced mathematical functions.

This module contains functions for:
- Basic arithmetic operations (add, subtract, multiply, divide)
- Advanced mathematical operations (factorial, fibonacci, prime checking)
- Edge case handling for division by zero, negative numbers, and large integers
"""


def add(a, b):
    """
    Add two numbers together.

    Args:
        a (int or float): First number
        b (int or float): Second number

    Returns:
        int or float: Sum of a and b

    Raises:
        TypeError: If inputs are not numbers
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    return a + b


def subtract(a, b):
    """
    Subtract second number from first number.

    Args:
        a (int or float): Number to subtract from
        b (int or float): Number to subtract

    Returns:
        int or float: Difference of a and b

    Raises:
        TypeError: If inputs are not numbers
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    return a - b


def multiply(a, b):
    """
    Multiply two numbers together.

    Args:
        a (int or float): First number
        b (int or float): Second number

    Returns:
        int or float: Product of a and b

    Raises:
        TypeError: If inputs are not numbers
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    return a * b


def divide(a, b):
    """
    Divide first number by second number.

    Args:
        a (int or float): Dividend
        b (int or float): Divisor

    Returns:
        float: Quotient of a and b

    Raises:
        TypeError: If inputs are not numbers
        ZeroDivisionError: If divisor is zero
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


def factorial(n):
    """
    Calculate the factorial of a non-negative integer.

    Args:
        n (int): Non-negative integer

    Returns:
        int: Factorial of n (n!)

    Raises:
        TypeError: If input is not an integer
        ValueError: If input is negative
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


def fibonacci(n):
    """
    Calculate the nth Fibonacci number.

    Args:
        n (int): Position in Fibonacci sequence (0-indexed)

    Returns:
        int: The nth Fibonacci number

    Raises:
        TypeError: If input is not an integer
        ValueError: If input is negative
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 0:
        raise ValueError("Fibonacci sequence is not defined for negative numbers")

    if n == 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def is_prime(n):
    """
    Check if a number is prime.

    Args:
        n (int): Number to check for primality

    Returns:
        bool: True if n is prime, False otherwise

    Raises:
        TypeError: If input is not an integer
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")

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


def power(base, exponent):
    """
    Calculate base raised to the power of exponent.

    Args:
        base (int or float): Base number
        exponent (int or float): Exponent

    Returns:
        int or float: Result of base^exponent

    Raises:
        TypeError: If inputs are not numbers
        ValueError: If base is 0 and exponent is negative
    """
    if not isinstance(base, (int, float)) or not isinstance(exponent, (int, float)):
        raise TypeError("Both arguments must be numbers")
    if base == 0 and exponent < 0:
        raise ValueError("Cannot raise 0 to a negative power")
    return base**exponent


def gcd(a, b):
    """
    Calculate the Greatest Common Divisor of two integers using Euclidean algorithm.

    Args:
        a (int): First integer
        b (int): Second integer

    Returns:
        int: Greatest Common Divisor of a and b

    Raises:
        TypeError: If inputs are not integers
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both arguments must be integers")

    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    """
    Calculate the Least Common Multiple of two integers.

    Args:
        a (int): First integer
        b (int): Second integer

    Returns:
        int: Least Common Multiple of a and b

    Raises:
        TypeError: If inputs are not integers
        ValueError: If either input is zero
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both arguments must be integers")
    if a == 0 or b == 0:
        raise ValueError("LCM is not defined for zero")

    return abs(a * b) // gcd(a, b)


def square_root(n):
    """
    Calculate the square root of a number using Newton's method.

    Args:
        n (int or float): Number to find square root of

    Returns:
        float: Square root of n

    Raises:
        TypeError: If input is not a number
        ValueError: If input is negative
    """
    if not isinstance(n, (int, float)):
        raise TypeError("Input must be a number")
    if n < 0:
        raise ValueError("Cannot calculate square root of negative number")
    if n == 0:
        return 0.0

    # Newton's method for square root
    x = n
    while True:
        root = 0.5 * (x + n / x)
        if abs(root - x) < 1e-10:
            break
        x = root
    return root


def absolute_value(n):
    """
    Calculate the absolute value of a number.

    Args:
        n (int or float): Number to find absolute value of

    Returns:
        int or float: Absolute value of n

    Raises:
        TypeError: If input is not a number
    """
    if not isinstance(n, (int, float)):
        raise TypeError("Input must be a number")
    return -n if n < 0 else n
