#!/usr/bin/python3
safe_print_list = __import__('0-safe_print_list.py').safe_print_list

list = [1, 2, 3, 4, 5]

x_print = safe_print_list(list, 2)
print("x_print: {:d}".format(x_print))
x_print = safe_print_list(list, len(list))
print("x_print: {:d}".format(x_print))
x_print = safe_print_list(list, len(list) + 2)
print("x_print: {:d}".format(x_print))
