"""
String manipulation and utility functions module.

This module contains functions for:
- String validation and analysis (is_palindrome, count_words)
- String transformation (reverse_string, capitalize_words)
- String cleaning and extraction (remove_whitespace, extract_numbers)
- Handling edge cases with empty strings, None values, and special characters
"""

import re


def reverse_string(text):
    """
    Reverse a string.

    Args:
        text (str): The string to reverse

    Returns:
        str: The reversed string

    Raises:
        TypeError: If input is not a string or None
    """
    if text is None:
        raise TypeError("Input cannot be None")
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    return text[::-1]


def is_palindrome(text):
    """
    Check if a string is a palindrome (reads the same forwards and backwards).
    Case-insensitive and ignores spaces and punctuation.

    Args:
        text (str): The string to check

    Returns:
        bool: True if the string is a palindrome, False otherwise

    Raises:
        TypeError: If input is not a string or None
    """
    if text is None:
        raise TypeError("Input cannot be None")
    if not isinstance(text, str):
        raise TypeError("Input must be a string")

    # Remove non-alphanumeric characters and convert to lowercase
    cleaned = re.sub(r"[^a-zA-Z0-9]", "", text).lower()
    return cleaned == cleaned[::-1]


def count_words(text):
    """
    Count the number of words in a string.
    Words are separated by whitespace.

    Args:
        text (str): The string to count words in

    Returns:
        int: Number of words in the string

    Raises:
        TypeError: If input is not a string or None
    """
    if text is None:
        raise TypeError("Input cannot be None")
    if not isinstance(text, str):
        raise TypeError("Input must be a string")

    if not text.strip():
        return 0

    return len(text.split())


def capitalize_words(text):
    """
    Capitalize the first letter of each word in a string.

    Args:
        text (str): The string to capitalize

    Returns:
        str: String with each word capitalized

    Raises:
        TypeError: If input is not a string or None
    """
    if text is None:
        raise TypeError("Input cannot be None")
    if not isinstance(text, str):
        raise TypeError("Input must be a string")

    return text.title()


def remove_whitespace(text):
    """
    Remove all whitespace characters from a string.

    Args:
        text (str): The string to remove whitespace from

    Returns:
        str: String with all whitespace removed

    Raises:
        TypeError: If input is not a string or None
    """
    if text is None:
        raise TypeError("Input cannot be None")
    if not isinstance(text, str):
        raise TypeError("Input must be a string")

    return re.sub(r"\s+", "", text)


def extract_numbers(text):
    """
    Extract all numbers from a string.

    Args:
        text (str): The string to extract numbers from

    Returns:
        list: List of numbers (as strings) found in the text

    Raises:
        TypeError: If input is not a string or None
    """
    if text is None:
        raise TypeError("Input cannot be None")
    if not isinstance(text, str):
        raise TypeError("Input must be a string")

    return re.findall(r"-?\d+\.?\d*", text)


def is_empty_or_whitespace(text):
    """
    Check if a string is empty or contains only whitespace.

    Args:
        text (str): The string to check

    Returns:
        bool: True if string is empty or whitespace-only, False otherwise

    Raises:
        TypeError: If input is not a string or None
    """
    if text is None:
        raise TypeError("Input cannot be None")
    if not isinstance(text, str):
        raise TypeError("Input must be a string")

    return len(text.strip()) == 0


def contains_special_chars(text):
    """
    Check if a string contains special characters (non-alphanumeric).

    Args:
        text (str): The string to check

    Returns:
        bool: True if string contains special characters, False otherwise

    Raises:
        TypeError: If input is not a string or None
    """
    if text is None:
        raise TypeError("Input cannot be None")
    if not isinstance(text, str):
        raise TypeError("Input must be a string")

    return bool(re.search(r"[^a-zA-Z0-9\s]", text))


def clean_string(text):
    """
    Clean a string by removing extra whitespace and converting to lowercase.
    Replaces multiple consecutive whitespace characters with single spaces.

    Args:
        text (str): The string to clean

    Returns:
        str: Cleaned string

    Raises:
        TypeError: If input is not a string or None
    """
    if text is None:
        raise TypeError("Input cannot be None")
    if not isinstance(text, str):
        raise TypeError("Input must be a string")

    # Replace multiple whitespace with single space and strip
    cleaned = re.sub(r"\s+", " ", text).strip().lower()
    return cleaned


def truncate_string(text, max_length, suffix="..."):
    """
    Truncate a string to a maximum length, optionally adding a suffix.

    Args:
        text (str): The string to truncate
        max_length (int): Maximum length of the result
        suffix (str): Suffix to add if truncation occurs

    Returns:
        str: Truncated string

    Raises:
        TypeError: If text is not a string or None, or max_length is not an integer
        ValueError: If max_length is less than 0
    """
    if text is None:
        raise TypeError("Text cannot be None")
    if not isinstance(text, str):
        raise TypeError("Text must be a string")
    if not isinstance(max_length, int):
        raise TypeError("max_length must be an integer")
    if not isinstance(suffix, str):
        raise TypeError("suffix must be a string")
    if max_length < 0:
        raise ValueError("max_length must be non-negative")

    if len(text) <= max_length:
        return text

    if max_length < len(suffix):
        return suffix[:max_length]

    return text[: max_length - len(suffix)] + suffix
