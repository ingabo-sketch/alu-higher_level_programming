#!/usr/bin/python3
"""Prints a square made of # characters.

The size must be an integer greater than or equal to zero.
"""


def print_square(size):
    """Print a square of # characters with the given size.
    Size must be an integer greater than or equal to zero.
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
