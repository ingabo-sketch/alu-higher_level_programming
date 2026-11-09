#!/usr/bin/python3
"""Module that adds a new attribute to an object when possible."""


def add_attribute(obj, name, value):
    """Add a new attribute to an object when the object can store one.

    Args:
        obj (object): Object that should receive the attribute.
        name (str): Name of the new attribute.
        value (object): Value stored under that name.

    Raises:
        TypeError: If the object cannot receive a new attribute.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
