#!/usr/bin/python3
"""Defines a class that inherits class-checking function"""


def inherits_from(obj, a_class):
    """Returns True if the object is an instance"""
    return type(obj) is not a_class and isinstance(obj, a_class)
