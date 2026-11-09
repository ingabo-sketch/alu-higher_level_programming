#!/usr/bin/python3
"""Module that checks an object against one exact class."""


def is_same_class(obj, a_class):
    """Return True when obj is exactly an instance of a_class.

    Args:
        obj (object): Object to test.
        a_class (type): Class to compare against.

    Returns:
        bool: True only for an exact class match.
    """
    return type(obj) is a_class
