#!/usr/bin/python3
"""Module 3-to_json_string.
Returns a JSON representation of an object
"""
import json


def to_json_string(my_obj):
    """Returns a JSON rep of an obj

    Args:
        obj: the object to rep
    Return:
        JSON representation
    """

    return json.dumps(obj)
