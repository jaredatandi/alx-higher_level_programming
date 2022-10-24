#!/usr/bin/python3
"""Module 2-is_same_class
checks if an instance is of the specified class
"""


def is_same_class(obj, a_class):
    """Checks for existance of an instance

    Args:
        -obj: an obj to check
        -a_class: the class to check the obj in
    Return:
        -True: if the instance exist
        -False: if it doesn't
    """
    return True if type(obj) is a_class else False
