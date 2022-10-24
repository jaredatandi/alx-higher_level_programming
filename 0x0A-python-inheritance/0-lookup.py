#!/usr/bin/python3
"""A function to retrieve a list of attributes
The function returns both attributes and methods
of an object
"""


def lookup(obj):
    """Returns a list of attributes and methods

    Args:
        -obj: object to find its attributes
        and methods
    """

    return dir(obj)

