#!/usr/bin/python3
"""Module that appends a string to a UTF-8 text file."""


def append_write(filename="", text=""):
    """Append a string to a UTF-8 text file and return the character count.

    Args:
        filename (str): Path of the file to update.
        text (str): Text added at the end of the file.

    Returns:
        int: Number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as text_file:
        return text_file.write(text)
