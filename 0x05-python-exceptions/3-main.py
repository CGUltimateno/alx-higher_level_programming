#!/usr/bin/python3

divide = __import__('3-safe_print_division.py').safe_print_division

a = 12

b = 2

res = divide(a, b)
print("{:d} / {:d} = {}".format(a, b, res))

a = 12
b = 0
res = divide(a, b)
print("{:d} / {:d} = {}".format(a, b, res))
