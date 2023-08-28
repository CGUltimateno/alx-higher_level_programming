#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        res = a / b
    except (TypeError, ZeroDivisionError):
        res = None
    finally:
        print("Result is: {}".format(res))
    return res
