#!/usr/bin/python3
"""Module Base class
defines a class BaseGeometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a Square that inherits from the Rectangle."""

    def __init__(self, size):
        """Instatiates the Square."""

        self.integer_validator("size", size)
        super().integer_validator(size, size)
        self.__size = size

    def __str__(self):
        return super().__str__()

    def area(self):
        """Calculates the area."""

        return self.__size ** 2
