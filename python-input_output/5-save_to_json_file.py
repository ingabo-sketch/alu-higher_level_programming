#!/usr/bin/python3
"""Module that saves an object to a file as JSON."""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file using its JSON representation.

    Args:
        my_obj (object): Value that can be serialized as JSON.
        filename (str): Path of the destination file.
    """
    with open(filename, "w", encoding="utf-8") as text_file:
        json.dump(my_obj, text_file)
