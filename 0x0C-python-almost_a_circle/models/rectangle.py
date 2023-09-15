#!/usr/bin/python3
""" Rectangle class """
from models.base import Base

class Rectangle(Base):
    """ Rectangle class """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Constructor """
        super().__init__(id)
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
        if type(value) is not int:
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
        if type(value) is not int:
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
        if type(value) is not int:
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
        if type(value) is not int:
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
            """ Updates attributes """
            if args and len(args) != 0:
                attrs = 0
                for i in args:
                    if attrs == 0:
                        if i is None:
                            self.__init__(self.width, self.height, self.x, self.y)
                        else:
                            self.id = i
                    elif attrs == 1:
                        self.width = i
                    elif attrs == 2:
                        self.height = i
                    elif attrs == 3:
                        self.x = i
                    elif attrs == 4:
                        self.y = i
                    attrs += 1

            elif kwargs and len(kwargs) != 0:
                for key, value in kwargs.items():
                    if key == "id":
                        if value is None:
                            self.__init__(self.width, self.height, self.x, self.y)
                        else:
                            self.id = value
                    elif key == "width":
                        self.width = value
                    elif key == "height":
                        self.height = value
                    elif key == "x":
                        self.x = value
                    elif key == "y":
                        self.y = value


        def to_dictionary(self):
            """ Returns dictionary representation """
            return {"id": self.id, "width": self.width, "height": self.height, "x": self.x, "y": self.y}

        def __str__(self):
            """ Returns string representation """
            return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height)
