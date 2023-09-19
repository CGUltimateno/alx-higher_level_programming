#!/usr/bin/python3
""" Rectangle class """
from .base import Base


class Rectangle(Base):
    """ Rectangle class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Constructor """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ Getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Getter """
        return self.__x

    @x.setter
    def x(self, value):
        """ Setter """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Getter """
        return self.__y

    @y.setter
    def y(self, value):
        """ Setter """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Returns area of rectangle """
        return self.__width * self.__height

    def display(self):
        """ Prints rectangle """
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for i in range(self.__y)]
        for i in range(self.__height):
            [print(" ", end="") for j in range(self.__x)]
            [print("#", end="") for j in range(self.__width)]
            print("")

    def update(self, *args, **kwargs):
        """Updates the properties of rectangle"""
        args_len = len(args)

        if args is not None and args_len > 0:
            if args_len > 0:
                if args_len >= 1:
                    self.id = args[0]
                if args_len >= 2:
                    self.width = args[1]
                if args_len >= 3:
                    self.height = args[2]
                if args_len >= 4:
                    self.x = args[3]
                if args_len >= 5:
                    self.y = args[4]

            return

        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """ Returns dictionary representation """
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """ Returns string representation """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)
