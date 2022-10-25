#!/usr/bin/python3
"""Module 1-write_file
Appends a string to a test file
"""


def write_file(filename="", text=""):
    """Appends to a text file

    Args:
        filename: the name of the file
        text: the text to write
    """

    with open(filename, "w+") as file:
        return file.write(text)
