#!/usr/bin/python3
"""Module that checks whether an object inherits a class."""


def inherits_from(obj, a_class):
    """Return True when obj inherits a_class, but is not exactly that class.

    Args:
        obj (object): Object to test.
        a_class (type): Class that must sit above the object class.

    Returns:
        bool: True for a subclass instance only.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
