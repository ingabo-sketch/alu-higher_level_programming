#!/usr/bin/python3
"""Module that builds a JSON-ready dictionary for an object."""


def class_to_json(obj):
    """Return a dictionary of an object's serializable attributes.

    Args:
        obj (object): Instance whose attributes are simple values.

    Returns:
        dict: Attribute names and values ready for JSON serialization.
    """
    return obj.__dict__
