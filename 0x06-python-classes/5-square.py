#!/usr/bin/python3
"""Defines a Module class Square"""


class Square:
    """Represents a square.
    Private instance attribute: size:
        - property def size(self)
        - property setter def size(self, value)
    Instantiation with optional size.
    Public instance method: def area(self).
    Public instance method: def my_print(self).
    """

    def __init__(self, size=0):
        """Intializes the class Square"""
        self.__size = size

    @property
    def size(self):
        """Gets the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size to the given value"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates the area using the size"""
        return self.__size * self.__size

    def my_print(self):
        """ prints the character '#'"""
        if self.__size == 0:
            print()
        else:
            for i in range(0, self.__size):
                for r in range(0, self.__size):
                    print('#')
                print()
