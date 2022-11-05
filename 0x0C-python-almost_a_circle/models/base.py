#!/usr/bin/python3
"""Module base class
Creates a base class
id is always an int
"""
import json
from dataclasses import field
import turtle as t
import csv
from os.path import exists

class Base:
    """Base class

    Private attrs:
        __nb__objects: 0
    public instance:
        id
    """

    __nb__objects = 0

    def __init__(self, id=None):
        """initializes the class

        Args:
            id: class id assignment
        """

        self.id = 0
        if id is None:
            Base.__nb__objects += 1
            self.id = Base.__nb__objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns a JSON string representation of the input"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """JSON representation to a file"""
        if list_objs is None:
            with open(f'{cls.__name__}.json', 'w') as f:
                f.write('[]')
        else:
            a = []
            for i in list_objs:
                a.append(cls.to_dictionary(i))
            with open(f'{cls.__name__}.json', 'w') as f:
                f.write(cls.to_json_string(a))
