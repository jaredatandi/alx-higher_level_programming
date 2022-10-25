#!/usr/bin/python3
"""Module 1-write_file
Writes a string to a test file
"""


def write_file(filename="", text=""):
    """Writes to a text file

    Args:
        filename: the name of the file
        text: the text to write
    """

    with open(filename, "a") as file:
        return file.write(text)
