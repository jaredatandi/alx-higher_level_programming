#!/usr/bin/python3
"""Module Base class
defines a class BaseGeometry
"""


class BaseGeometry:
    """A class representation"""

    def area(self):
        """Yet to be implemented method"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates parameters

        Args:
            - name: the name of the parameter
            - value: the parameter value
        Raise:
            TypeError: if value not an int
            ValueError: if value is less than or equal to 0
        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Represent a Rectangle class derived from BaseGeometry."""

    def __init__(self, width, height):
        """Initalize the class.

        Args:
            width: the width of the rectangle
            height: the height of the rectangle
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
