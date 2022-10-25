#!/usr/bin/python3
"""Module 100-my_int.
Creates a class that inherits from int.
"""


class MyInt(int):
    """Class that inherits form int,
    But reverse the behaviour of != and ==.
    """

    def __eq__(self, other):
        """Reverse =="""

        return super().__ne__(other)

    def __ne__(self, other):
        """Reverse !=."""

        return super().__eq__(other)
