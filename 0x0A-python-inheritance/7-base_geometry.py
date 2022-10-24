#!/usr/bin/python3
"""Module 5-base_geometry
A class based on an empty class
"""


class BaseGeometry:
    """A class with a public method."""

    def area(self):
        """A class that raise an Exception with the message
        'area() is not implemented'
        """

        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """A method to validate a value

        Args:
            - name: a string
            - value: an int
        """

        if type(name) is not str:
            raise TypeError("{} must be a string".format(name))

        if type(value) is not int: 
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
