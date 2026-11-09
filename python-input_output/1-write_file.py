#!/usr/bin/python3
"""Module that writes a string into a UTF-8 text file."""


def write_file(filename="", text=""):
    """Write a string to a UTF-8 text file and return the character count.

    Args:
        filename (str): Path of the file to write.
        text (str): Text that replaces the file contents.

    Returns:
        int: Number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as text_file:
        return text_file.write(text)
