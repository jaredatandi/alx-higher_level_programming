#!/usr/bin/python3
"""Module 8-class_to_json.
Returns a dict description with data structure
(list, dict, str, int, bool)
for JSON serialization of an object
"""


def class_to_json(obj):
    """Creates a dict description of obj.

    Args:
        obj: obj to serialize

    Returns:
        dict description of obj
    """

    return obj.__dict__
