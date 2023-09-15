#!/usr/bin/python3
""" Square class """
from models.rectangle import Rectangle

class Square(Rectangle):
    """ Square class """
    def __init__(self, size, x=0, y=0, id=None):
        """ Constructor """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Getter """
        return self.width

    @size.setter
    def size(self, value):
        """ Setter """
        self.width = value
        self.height = value

    def __str__(self):
        """ Returns the string representation of a Square """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    def update(self, *args, **kwargs):
        """ Assigns an argument to each attribute """
        if args and len(args) != 0:
            x = 0
            for i in args:
                if x == 0:
                    if i is None:
                        self.id = self.id
                    else:
                        self.id = i
                elif x == 1:
                    self.size = i
                elif x == 2:
                    self.x = i
                elif x == 3:
                    self.y = i
                x += 1

    def to_dictionary(self):
        """ Returns the dictionary representation of a Square """
        return {"id": self.id, "size": self.width, "x": self.x, "y": self.y}

