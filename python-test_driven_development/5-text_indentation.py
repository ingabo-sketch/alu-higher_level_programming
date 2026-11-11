#!/usr/bin/python3
"""Prints text with two new lines after . ? and :.

Printed lines have no leading or trailing spaces.
"""


def text_indentation(text):
    """Print text with two new lines after each . ? and :.
    The text argument must be a string.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    buffer = ""
    for character in text:
        if character in ".?:":
            print(buffer.strip() + character)
            print()
            buffer = ""
        else:
            buffer += character
    if buffer.strip():
        print(buffer.strip(), end="")
