#!/usr/bin/python3
"""Module 3-is_kind_of_class.py
Finds out if an obj is an instance of, or if the obj
is an instance of a class inherited from the given class
"""


def is_kind_of_class(obj, a_class):
    """Finds if an obj is inherited

    Args:
        - obj: object
        - a_class: the class to evaluate

    Returns: True or False
    """

    return isinstance(obj, a_class)
