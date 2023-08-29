#!/usr/bin/python3

exception = __import__('5-raise_exception.py').raise_exception

try:
    exception()
except TypeError as TE:
    print("Exception raised")
