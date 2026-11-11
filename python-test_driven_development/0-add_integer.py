#!/usr/bin/python3
"""Adds two integers.

The function casts floats to integers before adding them.
It raises TypeError when an argument is not a number.
"""


def add_integer(a, b=98):
    """Add two integers and return the sum.
    Floats are cast to integers before the addition.
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
