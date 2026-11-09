#!/usr/bin/python3
"""Module that restricts dynamic attributes on a class."""


class LockedClass:
    """Allow only the first_name instance attribute to be created."""

    __slots__ = ["first_name"]
