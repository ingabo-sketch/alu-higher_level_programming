#!/usr/bin/python3
"""Module that inserts a line after each matching line in a file."""


def append_after(filename="", search_string="", new_string=""):
    """Insert a line after every line that contains a search string.

    Args:
        filename (str): Path of the file to update.
        search_string (str): Text that marks where the new line is inserted.
        new_string (str): Line written after each matching line.
    """
    with open(filename, "r", encoding="utf-8") as text_file:
        lines = text_file.readlines()
    with open(filename, "w", encoding="utf-8") as text_file:
        for line in lines:
            text_file.write(line)
            if search_string in line:
                text_file.write(new_string)
