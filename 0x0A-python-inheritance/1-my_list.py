#!/usr/bin/python3
"""Module 1-my_list
A class that inherits from list
"""


class MyList(list):
    """Prints a list in ascending sort

    Args:
        -list: a parent class
    """

    def print_sorted(self):
        """A method to print the list"""

        copied_list = self[:]
        copied_list.sort()
        print("{}".format(copied_list))
