#!/usr/bin/python3
"""Module that prevents the user from
dynamically creating new instance attributes"""


class LockedClass:
    """Class that prevents the user from
    dynamically creating new instance attributes"""
    __slots__ = ['first_name']

    def __init__(self):
        """init"""
        pass
