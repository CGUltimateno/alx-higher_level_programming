#!/usr/bin/python3
"""Defines a class that returns True if the object is exactly an instance"""


def is_same_class(obj, a_class):
    """Returns True if the object is exactly an instance"""
    return type(obj) is a_class
