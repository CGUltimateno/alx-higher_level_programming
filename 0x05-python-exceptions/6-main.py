#!/usr/bin/python3

exception_msg = __import__('6-raise_exception_msg.py').raise_exception_msg

try:
    exception_msg()
except NameError as NE:
    print(NE)
