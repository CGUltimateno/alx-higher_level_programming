#!/usr/bin/python3

safe_print_list_integers = __import__('2-safe_print_list_integers.py').safe_print_list_integers

list = [1, 2, 3, 4, 5]

x_print = safe_print_list_integers(list, 2)
print("x_print: {:d}".format(x_print))

list = [1, 2, 3, "School", 4, 5, [1, 2, 3]]
x_print = safe_print_list_integers(list, len(list))
print("x_print: {:d}".format(x_print))

x_print = safe_print_list_integers(list, len(list) + 2)
print("x_print: {:d}".format(x_print))
