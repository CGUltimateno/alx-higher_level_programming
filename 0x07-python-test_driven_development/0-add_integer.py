#!/usr/bin/python3
"""
Makes a Add_integer(a,b) function
"""


def add_integer(a, b=98):
    """Returns the addition of two numbers."""
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
