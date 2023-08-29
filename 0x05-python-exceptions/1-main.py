#!/usr/bin/python3

safe_print_integer = __import__('1-safe_print_integer.py').safe_print_integer

x = 89

printed = safe_print_integer(x)

if not printed:
    print("{} is not an integer".format(x))

x = -89
printed = safe_print_integer(x)

if not printed:
    print("{} is not an integer".format(x))

x = "School"
printed = safe_print_integer(x)

if not printed:
    print("{} is not an integer".format(x))
