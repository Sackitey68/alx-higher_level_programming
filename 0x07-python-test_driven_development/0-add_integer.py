#!/usr/bin/python3
"""Function that adds 2 integers"""


def add_integer(a, b=98):
    """
    These function return the addition of a and b
    since addition works on numeric values,

    raise:
        flags a typeError if the arguments are not
        an integer o float
    """

    if not (type(a) is float or type(a) is int):
        raise TypeError("a must be an integer")

    elif not (type(b) is float or type(b) is int):
        raise TypeError("b must be an integer")

    return int(a) + int(b)

