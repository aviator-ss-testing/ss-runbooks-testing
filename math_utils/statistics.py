"""
Statistical calculation utilities using only Python standard library.

This module provides comprehensive statistical functions for data analysis,
including measures of central tendency, dispersion, and data validation.
All functions are designed to work with various iterable types (lists, tuples, generators).
"""

import math
from typing import List, Tuple, Union, Iterable
from collections import Counter


def mean(data: Iterable[Union[int, float]]) -> float:
    """
    Calculate the arithmetic mean (average) of a dataset.

    Args:
        data: An iterable of numeric values

    Returns:
        float: The arithmetic mean of the data

    Raises:
        ValueError: If the dataset is empty
        TypeError: If data contains non-numeric values

    Example:
        >>> mean([1, 2, 3, 4, 5])
        3.0
    """
    values = list(data)
    if not values:
        raise ValueError("Cannot calculate mean of empty dataset")

    try:
        return sum(values) / len(values)
    except TypeError:
        raise TypeError("All values must be numeric")


def median(data: Iterable[Union[int, float]]) -> float:
    """
    Calculate the median (middle value) of a dataset.

    Args:
        data: An iterable of numeric values

    Returns:
        float: The median of the data

    Raises:
        ValueError: If the dataset is empty
        TypeError: If data contains non-numeric values

    Example:
        >>> median([1, 2, 3, 4, 5])
        3.0
        >>> median([1, 2, 3, 4])
        2.5
    """
    values = list(data)
    if not values:
        raise ValueError("Cannot calculate median of empty dataset")

    try:
        sorted_values = sorted(values)
        n = len(sorted_values)

        if n % 2 == 0:
            # Even number of values - average of two middle values
            mid1 = sorted_values[n // 2 - 1]
            mid2 = sorted_values[n // 2]
            return (mid1 + mid2) / 2
        else:
            # Odd number of values - return middle value
            return float(sorted_values[n // 2])
    except TypeError:
        raise TypeError("All values must be numeric and comparable")


def mode(data: Iterable[Union[int, float]]) -> List[Union[int, float]]:
    """
    Calculate the mode(s) (most frequently occurring value(s)) of a dataset.

    Args:
        data: An iterable of numeric values

    Returns:
        List: List of mode values (can be multiple if there's a tie)

    Raises:
        ValueError: If the dataset is empty

    Example:
        >>> mode([1, 2, 2, 3, 3, 3])
        [3]
        >>> mode([1, 1, 2, 2, 3])
        [1, 2]
    """
    values = list(data)
    if not values:
        raise ValueError("Cannot calculate mode of empty dataset")

    counts = Counter(values)
    max_count = max(counts.values())

    return [value for value, count in counts.items() if count == max_count]


def variance(data: Iterable[Union[int, float]], population: bool = False) -> float:
    """
    Calculate the variance of a dataset.

    Args:
        data: An iterable of numeric values
        population: If True, calculate population variance; if False, sample variance

    Returns:
        float: The variance of the data

    Raises:
        ValueError: If the dataset is empty or has insufficient data for sample variance
        TypeError: If data contains non-numeric values

    Example:
        >>> variance([1, 2, 3, 4, 5])
        2.5
    """
    values = list(data)
    if not values:
        raise ValueError("Cannot calculate variance of empty dataset")

    if not population and len(values) < 2:
        raise ValueError("Sample variance requires at least 2 data points")

    data_mean = mean(values)
    squared_deviations = [(x - data_mean) ** 2 for x in values]

    divisor = len(values) if population else len(values) - 1
    return sum(squared_deviations) / divisor


def standard_deviation(
    data: Iterable[Union[int, float]], population: bool = False
) -> float:
    """
    Calculate the standard deviation of a dataset.

    Args:
        data: An iterable of numeric values
        population: If True, calculate population std dev; if False, sample std dev

    Returns:
        float: The standard deviation of the data

    Raises:
        ValueError: If the dataset is empty or has insufficient data
        TypeError: If data contains non-numeric values

    Example:
        >>> round(standard_deviation([1, 2, 3, 4, 5]), 3)
        1.581
    """
    return math.sqrt(variance(data, population))


def data_range(data: Iterable[Union[int, float]]) -> float:
    """
    Calculate the range (difference between max and min) of a dataset.

    Args:
        data: An iterable of numeric values

    Returns:
        float: The range of the data

    Raises:
        ValueError: If the dataset is empty
        TypeError: If data contains non-numeric values

    Example:
        >>> data_range([1, 2, 3, 4, 5])
        4
    """
    values = list(data)
    if not values:
        raise ValueError("Cannot calculate range of empty dataset")

    try:
        return max(values) - min(values)
    except TypeError:
        raise TypeError("All values must be numeric and comparable")


def quartiles(data: Iterable[Union[int, float]]) -> Tuple[float, float, float]:
    """
    Calculate the first, second (median), and third quartiles of a dataset.

    Args:
        data: An iterable of numeric values

    Returns:
        Tuple[float, float, float]: Q1, Q2 (median), Q3

    Raises:
        ValueError: If the dataset is empty or has insufficient data
        TypeError: If data contains non-numeric values

    Example:
        >>> quartiles([1, 2, 3, 4, 5, 6, 7, 8, 9])
        (3.0, 5.0, 7.0)
    """
    values = list(data)
    if not values:
        raise ValueError("Cannot calculate quartiles of empty dataset")

    if len(values) < 3:
        raise ValueError("Quartiles require at least 3 data points")

    try:
        sorted_values = sorted(values)
        n = len(sorted_values)

        # Calculate Q2 (median)
        q2 = median(sorted_values)

        # Calculate Q1 (median of lower half)
        if n % 2 == 0:
            lower_half = sorted_values[: n // 2]
        else:
            lower_half = sorted_values[: n // 2]
        q1 = median(lower_half)

        # Calculate Q3 (median of upper half)
        if n % 2 == 0:
            upper_half = sorted_values[n // 2 :]
        else:
            upper_half = sorted_values[n // 2 + 1 :]
        q3 = median(upper_half)

        return (q1, q2, q3)
    except TypeError:
        raise TypeError("All values must be numeric and comparable")


def interquartile_range(data: Iterable[Union[int, float]]) -> float:
    """
    Calculate the interquartile range (Q3 - Q1) of a dataset.

    Args:
        data: An iterable of numeric values

    Returns:
        float: The interquartile range

    Raises:
        ValueError: If the dataset is empty or has insufficient data
        TypeError: If data contains non-numeric values

    Example:
        >>> interquartile_range([1, 2, 3, 4, 5, 6, 7, 8, 9])
        4.0
    """
    q1, _, q3 = quartiles(data)
    return q3 - q1


def detect_outliers_iqr(
    data: Iterable[Union[int, float]], multiplier: float = 1.5
) -> List[Union[int, float]]:
    """
    Detect outliers using the Interquartile Range (IQR) method.

    Outliers are defined as values below Q1 - multiplier*IQR or above Q3 + multiplier*IQR.

    Args:
        data: An iterable of numeric values
        multiplier: The IQR multiplier for outlier detection (default: 1.5)

    Returns:
        List: List of outlier values

    Raises:
        ValueError: If the dataset is empty or has insufficient data
        TypeError: If data contains non-numeric values

    Example:
        >>> detect_outliers_iqr([1, 2, 3, 4, 5, 100])
        [100]
    """
    values = list(data)
    if not values:
        return []

    q1, _, q3 = quartiles(values)
    iqr = q3 - q1

    lower_bound = q1 - multiplier * iqr
    upper_bound = q3 + multiplier * iqr

    outliers = [x for x in values if x < lower_bound or x > upper_bound]
    return outliers


def detect_outliers_zscore(
    data: Iterable[Union[int, float]], threshold: float = 2.0
) -> List[Union[int, float]]:
    """
    Detect outliers using the Z-score method.

    Outliers are defined as values with absolute Z-score greater than the threshold.

    Args:
        data: An iterable of numeric values
        threshold: The Z-score threshold for outlier detection (default: 2.0)

    Returns:
        List: List of outlier values

    Raises:
        ValueError: If the dataset is empty or has insufficient data
        TypeError: If data contains non-numeric values

    Example:
        >>> detect_outliers_zscore([1, 2, 3, 4, 5, 100])
        [100]
    """
    values = list(data)
    if not values:
        return []

    if len(values) < 2:
        return []

    data_mean = mean(values)
    data_std = standard_deviation(values)

    if data_std == 0:
        return []  # No outliers if std dev is 0

    outliers = []
    for value in values:
        z_score = abs((value - data_mean) / data_std)
        if z_score > threshold:
            outliers.append(value)

    return outliers


def remove_outliers_iqr(
    data: Iterable[Union[int, float]], multiplier: float = 1.5
) -> List[Union[int, float]]:
    """
    Remove outliers from dataset using the IQR method.

    Args:
        data: An iterable of numeric values
        multiplier: The IQR multiplier for outlier detection (default: 1.5)

    Returns:
        List: Dataset with outliers removed

    Raises:
        ValueError: If the dataset is empty or has insufficient data
        TypeError: If data contains non-numeric values

    Example:
        >>> remove_outliers_iqr([1, 2, 3, 4, 5, 100])
        [1, 2, 3, 4, 5]
    """
    values = list(data)
    if not values:
        return []

    outliers = detect_outliers_iqr(values, multiplier)
    return [x for x in values if x not in outliers]


def clean_numeric_data(data: Iterable) -> List[Union[int, float]]:
    """
    Clean dataset by removing non-numeric values and None values.

    Args:
        data: An iterable that may contain mixed types

    Returns:
        List: List containing only numeric values

    Example:
        >>> clean_numeric_data([1, 2, "hello", 3.5, None, 4])
        [1, 2, 3.5, 4]
    """
    cleaned = []
    for value in data:
        if (
            value is not None
            and isinstance(value, (int, float))
            and not isinstance(value, bool)
        ):
            # Check for NaN values
            if isinstance(value, float) and math.isnan(value):
                continue
            cleaned.append(value)
    return cleaned


def is_numeric_iterable(data: Iterable) -> bool:
    """
    Check if an iterable contains only numeric values.

    Args:
        data: An iterable to check

    Returns:
        bool: True if all values are numeric, False otherwise

    Example:
        >>> is_numeric_iterable([1, 2, 3.5])
        True
        >>> is_numeric_iterable([1, 2, "hello"])
        False
    """
    try:
        values = list(data)
        if not values:
            return True  # Empty iterable is considered numeric

        for value in values:
            if not isinstance(value, (int, float)) or isinstance(value, bool):
                return False
            if isinstance(value, float) and (math.isnan(value) or math.isinf(value)):
                return False
        return True
    except (TypeError, ValueError):
        return False


def percentile(data: Iterable[Union[int, float]], p: float) -> float:
    """
    Calculate the p-th percentile of a dataset.

    Args:
        data: An iterable of numeric values
        p: Percentile value (0 <= p <= 100)

    Returns:
        float: The p-th percentile value

    Raises:
        ValueError: If the dataset is empty or percentile is out of range
        TypeError: If data contains non-numeric values

    Example:
        >>> percentile([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 50)
        5.5
    """
    if not 0 <= p <= 100:
        raise ValueError("Percentile must be between 0 and 100")

    values = list(data)
    if not values:
        raise ValueError("Cannot calculate percentile of empty dataset")

    try:
        sorted_values = sorted(values)
        n = len(sorted_values)

        if p == 0:
            return float(sorted_values[0])
        if p == 100:
            return float(sorted_values[-1])

        # Calculate the index using linear interpolation
        index = (p / 100) * (n - 1)

        if index == int(index):
            return float(sorted_values[int(index)])
        else:
            # Interpolate between two values
            lower_index = int(math.floor(index))
            upper_index = int(math.ceil(index))
            weight = index - lower_index

            lower_value = sorted_values[lower_index]
            upper_value = sorted_values[upper_index]

            return lower_value + weight * (upper_value - lower_value)
    except TypeError:
        raise TypeError("All values must be numeric and comparable")
