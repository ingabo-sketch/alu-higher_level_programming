#!/usr/bin/python3
"""Module that lists attributes and methods of an object."""


def lookup(obj):
    """Return the list of attributes and methods available on an object.

    Args:
        obj (object): Any object to inspect.

    Returns:
        list: Names available on the object.
    """
    return dir(obj)
