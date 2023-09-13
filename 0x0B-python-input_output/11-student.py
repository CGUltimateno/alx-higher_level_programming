#!/usr/bin/python3
"""Module that defines a class Student"""


class Student:
    """Class that defines a student"""

    def __init__(self, first_name, last_name, age):
        """Initializes the student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Function that returns the dictionary
        description with simple data structure"""
        if attrs is None:
            return self.__dict__
        else:
            d = {}
            for attr in attrs:
                if hasattr(self, attr):
                    d[attr] = getattr(self, attr)
            return d

    def reload_from_json(self, json):
        """Function that replaces all attributes of the Student instance"""
        for key in json:
            setattr(self, key, json[key])
