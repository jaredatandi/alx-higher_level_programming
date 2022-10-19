#!/usr/bin/python3
"""Module 4-rectangle
Defines a Rectangle class
"""

class Rectangle:
    """Rectangle class"""

    def __init__(self, width=0, height=0):
        """Class intializer
        Args:
            width: width parameter
            height: height parameter
        """
        self.width = width
        self.height = height

    def __str__(self):
        """Prints '#' as the Rectangle"""
        if self.__height == 0 or self.__width == 0:
            return ''
        rec = ''
        for i in range(self.__height):
            for j in range(self.width):
                rec += '#'
            rec += '\n'
        return rec[:-1]

    def __repr__(self):
        """Create a new instance using eval()"""
        return "Rectangle{}, {})".format(self.__width, self.__height)

    @property
    def width(self):
        """Gets the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width
        
        Args:
            value: width parameter
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height 
        
        Args:
            value: height parameter
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height= value

    def area(self):
        """Calculates the area of the Rectangle

        Returns:
            Area of the Rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculates the perimeter of the Rectangle

        Returns:
            the perimeter of the Rectangle
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)
