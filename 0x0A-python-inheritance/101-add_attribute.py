#!/usr/bin/python3
"""Module to add attributes to an object"""


def add_attribute(obj, att, value):
    """Function to add attributes to an object"""
    if hasattr(obj, "__dict__"):
        setattr(obj, att, value)
    else:
        raise TypeError("can't add new attribute")
