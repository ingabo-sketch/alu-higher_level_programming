#!/usr/bin/python3
"""Module that prints the contents of a UTF-8 text file."""


def read_file(filename=""):
    """Print a UTF-8 text file to standard output.

    Args:
        filename (str): Path of the file to read.
    """
    with open(filename, "r", encoding="utf-8") as text_file:
        print(text_file.read(), end="")
