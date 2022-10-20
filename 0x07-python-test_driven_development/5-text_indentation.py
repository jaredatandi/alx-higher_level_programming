#!/usr/bin/python3
"""
Module text_indentation
Adds two new lines after a set of characters
"""


def text_indentation(text):
    """
    Prints a text with added two lines
    after delimeters: '.', '?', ':'.
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    for delim in ".:?":
        text = (delim + "\n\n").join(
                [line.strip(" ") for line in text.split(delim)])

    print("{}".format(text), end="")
