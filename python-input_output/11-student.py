#!/usr/bin/python3
"""Module that defines a Student class that can reload its attributes."""


class Student:
    """Represent a student with a name and an age."""

    def __init__(self, first_name, last_name, age):
        """Store the public attributes of a student.

        Args:
            first_name (str): Student first name.
            last_name (str): Student last name.
            age (int): Student age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary representation of this student.

        Args:
            attrs (list): Attribute names to keep, or None for every attribute.

        Returns:
            dict: Selected student attributes.
        """
        if type(attrs) is list and all(type(item) is str for item in attrs):
            result = {}
            for key in attrs:
                if hasattr(self, key):
                    result[key] = getattr(self, key)
            return result
        return self.__dict__

    def reload_from_json(self, json):
        """Replace the student attributes with values stored in a dictionary.

        Args:
            json (dict): Attribute names and the values that replace them.
        """
        for key, value in json.items():
            setattr(self, key, value)
