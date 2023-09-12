#!/usr/bin/python3
"""
Defines a class Square that inherits from Rectangle (10-rectangle.py)
"""

prevsquare = __import__('10-square').Square


class Square(prevsquare):
    """
    Represent a square.
    """

    def __init__(self, size):
        """Initialize a constructor of the new square."""
        super().__init__(size)

    def __str__(self):
        """Return the print() and str() representation of a Square."""
        return "[Square] {0:d}/{0:d}".format(self.__size)
