#!/usr/bin/python3
"""Module base class
Creates a base class
id is always an int
"""


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
