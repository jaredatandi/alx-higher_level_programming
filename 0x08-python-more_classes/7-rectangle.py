#!/usr/bin/python3
"""Module 7-rectangle
Defines a Rectangle class.
"""


class Rectangle:
    """Rectangle class defined by width and height.
    Attributes:
        number_of_instances: number of instanciated Rectangles
        increment when initialized
        decrement when deleted
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initializer

        Args:
            width: the width measurement
            height: the height measurement
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """prints the Rectangle instance filled
        with '#' character. """
        if self.__height == 0 or self.__width == 0:
            return ''
        rec = ''
        for i in range(self.__height):
            for j in range(self.__width):
                rec += str(self.print_symbol)
            rec += '\n'
        return rec[:-1]

    def __repr__(self):
        """Returns a string representation of the Rectangle
        instance that is able to recreate a new instance using
        eval()
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Deletes a Rectangle instance"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """Gets the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width

        Args:
            value: the positive int value
        """
        if not isinstance(value, int):
            raise TypeError("Width must be an integer")
        if value < 0:
            raise ValueError("Width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height
        Args:
            value: the positive int value
        """
        if not isinstance(value, int):
            raise TypeError("height must be an int")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Finds the area of the Rectangle

        Returns:
            Area of the Rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """Finds the perimeter

        Returns:
            perimeter of the Rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
