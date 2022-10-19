#!/usr/bin/python3
"""Module 2-rectangle
Defines a Rectangle class
"""


class Rectangle:
    """Rectangle class defined by width and height."""
    def __init__(self, width=0, height=0):
        """Intializes a Rectangle instance.
        Args:
            width: width measurement of the Rectangle
            height: height measurement of the Rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets the width of the Rectangle instance"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the Rectangle instance
        Args:
            value: value to be assigned to width
        """
        if not isinstance(value, int):
            raise TypeError("Width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets the height of a Rectangle instance"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of a Rectange instance
        Args:
            value: value of the height, must be positive int
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Computes the area fo a Rectangle instance"

        Returns:
            Area of the Rectangle instance
        """
        return self.__width * self.__height

    def perimeter(self):
        """Computes the perimeter of a Rectangle instance

        Returns:
            Perimenter of the Rectangle
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)
