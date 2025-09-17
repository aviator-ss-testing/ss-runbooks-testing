"""
Math utilities package providing arithmetic, number theory, and statistical functions.

This package contains modules for various mathematical operations:
- arithmetic: Basic arithmetic operations and utilities
- number_theory: Prime numbers, Fibonacci, GCD/LCM operations
- statistics: Statistical calculations and data analysis functions

All public functions are available for direct import:
    from math_utils import factorial, is_prime, mean
    from math_utils.arithmetic import gcd, lcm
    from math_utils.number_theory import fibonacci_sequence
    from math_utils.statistics import standard_deviation
"""

from .arithmetic import (
    factorial,
    gcd,
    lcm,
    power,
    safe_divide,
    modular_exponentiation,
    absolute_value,
)

from .number_theory import (
    is_prime,
    generate_primes,
    prime_factors,
    fibonacci_sequence,
    fibonacci_generator,
    is_fibonacci,
    is_perfect_number,
    is_abundant_number,
    gcd_multiple,
    lcm_multiple,
    extended_gcd,
)

from .statistics import (
    mean,
    median,
    mode,
    variance,
    standard_deviation,
    data_range,
    quartiles,
    interquartile_range,
    detect_outliers_iqr,
    detect_outliers_zscore,
    remove_outliers_iqr,
    clean_numeric_data,
    is_numeric_iterable,
    percentile,
)

# Also import submodules for direct access
from . import arithmetic
from . import number_theory
from . import statistics

# Define public API
__all__ = [
    # Submodules
    "arithmetic",
    "number_theory",
    "statistics",
    # Arithmetic functions
    "factorial",
    "gcd",
    "lcm",
    "power",
    "safe_divide",
    "modular_exponentiation",
    "absolute_value",
    # Number theory functions
    "is_prime",
    "generate_primes",
    "prime_factors",
    "fibonacci_sequence",
    "fibonacci_generator",
    "is_fibonacci",
    "is_perfect_number",
    "is_abundant_number",
    "gcd_multiple",
    "lcm_multiple",
    "extended_gcd",
    # Statistics functions
    "mean",
    "median",
    "mode",
    "variance",
    "standard_deviation",
    "data_range",
    "quartiles",
    "interquartile_range",
    "detect_outliers_iqr",
    "detect_outliers_zscore",
    "remove_outliers_iqr",
    "clean_numeric_data",
    "is_numeric_iterable",
    "percentile",
]
