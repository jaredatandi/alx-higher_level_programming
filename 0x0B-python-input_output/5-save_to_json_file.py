#!/usr/bin/python3
"""Module 5-save_to_json_file.
Writes an object to a text file using JSON
"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file

    Args:
        my_obj: the object to write
        filename: filename to save the obj to
    """

    with open(filename, "w+") as file:
        json.dump(my_obj, file)
