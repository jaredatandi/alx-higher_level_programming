#!/usr/bin/python3
"""Module 1-write_file
Appends a string to a test file
"""


def append_write(filename="", text=""):
    """Appends to a text file

    Args:
        filename: the name of the file
        text: the text to write
    Return: the number of char added
    """

    with open(filename, "a+") as file:
        return file.write(text)
