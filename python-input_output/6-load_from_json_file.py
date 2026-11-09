#!/usr/bin/python3
"""Module that creates an object loaded from a JSON file."""
import json


def load_from_json_file(filename):
    """Create a Python object from a JSON file.

    Args:
        filename (str): Path of the JSON file.

    Returns:
        object: Python data structure stored in the file.
    """
    with open(filename, "r", encoding="utf-8") as text_file:
        return json.load(text_file)
