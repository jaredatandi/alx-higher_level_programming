#!/usr/bin/python3
"""Module 4-from_json_string.
Returns an object represented by
JSON string
"""


def from_json_string(my_str):
    """Returns a python data structure

    Args:
        my_str: the string to convert
    Return:
        JSON representation
    """

    return json.loads(my_str)
