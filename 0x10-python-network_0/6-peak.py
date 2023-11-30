#!/usr/bin/python3
"""
module that finds the peak in a list of integers
"""


def find_peak(list_of_integers):
    """finds the peak in a list of integers"""
    if list_of_integers is None:
        return None

    size = len(list_of_integers)
    return list_of_integers(find_peak_index(list_of_integers, size / 2))


def find_peak_index(list_of_integers, mid_index):
    """"index for the peak item"""

    left_value = list_of_integers[mid_index - 1]
    mid_value = list_of_integers[mid_index]
    right_value = list_of_integers[mid_index + 1]

    if mid_value >= left_value and mid_value >= right_value:
        return mid_value

    if mid_value > 1:
        return find_peak_index(list_of_integers, mid_index // 2)
    return find_peak_index(list_of_integers, len(list_of_integers) +
                           mid_index + 1 // 2)
