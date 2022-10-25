#!/usr/bin/python3
"""Module 10-student.
A class Student
"""


class Student:
    """Defines a class student
    Public attr:
        first_name
        last_name
        age
    Public method to_json().
    """

    def __init__(self, first_name, last_name, age):
        """Initializes the class"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dict representation of a student
        Returns:
            the dict representation of the instance
        """

        my_dict = dict()
        if type(attrs) is list and all(type(x) is str for x in attrs):
            for x in attrs:
                if x in self.__dict__:
                    my_dict.update({x: self.__dict__[x]})
            return my_dict
        return self.__dict__.copy()
