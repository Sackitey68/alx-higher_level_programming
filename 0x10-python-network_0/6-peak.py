#!/usr/bin/python3
"""
Module to locate the hightest number in array
"""


def find_peak(list_of_integers):
    """
    Method to locate hightest number in array
    """
    if bool(list_of_integers) is False:
        return None
    list_of_integers.sort()
    return list_of_integers[-1]
