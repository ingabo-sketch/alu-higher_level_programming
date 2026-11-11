#!/usr/bin/python3
"""Prints a person's name.

Both the first name and the last name must be strings.
"""


def say_my_name(first_name, last_name=""):
    """Print My name is followed by the first and last name.
    Both names must be strings.
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
