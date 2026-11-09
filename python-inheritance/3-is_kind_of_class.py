#!/usr/bin/python3
"""Module that checks an object against a class or its subclasses."""


def is_kind_of_class(obj, a_class):
    """Return True when obj is an instance of a_class or a subclass of it.

    Args:
        obj (object): Object to test.
        a_class (type): Class to compare against.

    Returns:
        bool: True when the object matches the class hierarchy.
    """
    return isinstance(obj, a_class)
