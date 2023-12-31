#!/usr/bin/python3
"""Module that prints a square with #"""


def print_square(size):
    """Function that prints a square with #"""

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print('#' * size)
