#!/usr/bin/python3
"""Module 6-load_from_json_file.
Creates an object from a JSON file
"""
import json


def load_from_json_file(filename):
    """Creates an obj from json

    Args:
        filename: the obj to load
    Returns:
        the obj
    """

    with open(filename, 'r') as file:
        return json.load(file)
