#!/usr/bin/python3
"""Module that converts an object to a JSON string."""
import json


def to_json_string(my_obj):
    """Return the JSON string representation of an object.

    Args:
        my_obj (object): Value that can be serialized as JSON.

    Returns:
        str: JSON representation of my_obj.
    """
    return json.dumps(my_obj)
