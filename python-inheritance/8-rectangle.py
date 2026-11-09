#!/usr/bin/python3
"""Module that defines a rectangle based on BaseGeometry."""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle with a private positive width and height."""

    def __init__(self, width, height):
        """Store width and height after validating both values.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
