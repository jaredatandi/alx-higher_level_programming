#!/usr/bin/python3
"""Module Base class
defines a class BaseGeometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


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
