#!/usr/bin/python3
"""Module 4-inherits_from.py
Finds if an object is directly inheriting from a class
"""


def inherits_from(obj, a_class):
    """Finds out if an object is an instance of a
    class directly or indirectly

    Args:
        - obj: the object
        - a_class: the class to evaluate

    Return: True or False
    """

    return isinstance(obj, a_class) and type(obj) != a_class
