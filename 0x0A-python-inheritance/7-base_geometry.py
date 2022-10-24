#!/usr/bin/python3
"""Module 7-base_geometry.
Creates a BaseGeometry class.
"""


class BaseGeometry:
    """A class with a public method and a validator."""

    def area(self):
        """A class that raise an Exception with the message
        'area() is not implemented'
        """

        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """A method to validate a value

        Args:
            name: a string name of the parameter
            value: the parameter to validate
        """

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
