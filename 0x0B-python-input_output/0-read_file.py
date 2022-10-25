#!/usr/bin/python3
"""Module 0-read_file
Reads from a text file and prints to stdout
"""


def read_file(filename=""):
    """Reads from a filename and prints the content

    Args: 
        filename: the name of the file to open
    """

    with open("filename", encoding="utf-8") as file:
        read_data = file.read()
        print(read_data, end="")
