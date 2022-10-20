#!/usr/bin/python3
class Square:
    """Represents a square class.
    Private instance attribute: size.
    With type and negative value checking 
    """


    def __init__(self, size=0):
        """Intiliazes the size"""
        if not isinstance(size, int): 
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
