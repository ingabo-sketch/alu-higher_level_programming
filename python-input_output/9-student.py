#!/usr/bin/python3
"""Module that defines a Student class."""


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

    def to_json(self):
        """Return a dictionary representation of this student."""
        return self.__dict__
