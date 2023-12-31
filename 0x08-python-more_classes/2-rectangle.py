#!/usr/bin/python3
"""Just a silly Rectangle class."""


class Rectangle:
    """Just a silly Rectangle."""

    def __init__(self, width=0, height=0):
        """Init a silly rectangle"""

        self.width = width
        self.height = height

    @property
    def width(self):
        """Get width"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get Height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return area of silly rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Return perimeter of silly rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)
