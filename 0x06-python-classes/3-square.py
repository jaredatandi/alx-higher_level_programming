#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """
    Defines a class square with
    Private instance attribute size
    Instatiation with optional size
    An area method
    """

    def __init__(self, size=0):
        """Intializes the class Square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculates the area using the size"""
        return self.__size * self.__size
