#!/usr/bin/python3
""" Module 1-Rectangle
Defines a Rectangle class.
"""


class Rectangle:
    """Rectangle class defined by height and width"""

    def __init__(self, width=0, height=0):
        """Intializes a Rectangle isinstance.
        Args:
            width: the width measurement
            height: the height measurement
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets the width of the Rectangle isinstance"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the Rectangle isinstance"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets the height of the Rectangle isinstance"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the Rectangle isinstance"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
