#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent square."""

    def __init__(self, size=0, position=(0, 0)):
        """Init a Square.
        Args:
            size(int): size of square
            position(int, int): position of square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get/set the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Get/set for the size private attribute"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Get/set the current  of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        if (len(value) != 2) or (type(value) is not tuple) \
                or (type(value[0]) is not int) \
                or (type(value[1]) is not int) \
                or (value[0] < 0) or (value[1] < 0):
            raise TypeError("position must be a tuple of two positive integers")
        else:
            self.__position = value

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Print a square with the # character."""
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__position[1]):
                print()
            for j in range(self.size):
                print(" " * self.__position[0], end='')
                print("#" * self.__size)
