#!/usr/bin/python3
"""Module 9-student.
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

    def to_json(self):
        """Retrieves a dict representation of a student
        Returns:
            the dict representation of the instance
        """

        return self.__dict__
