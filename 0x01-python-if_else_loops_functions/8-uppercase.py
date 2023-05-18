#!/usr/bin/python3
def uppercase(str):
    """TODO: Docstring for is uppercase.
    :returns: TODO

    """
    for i in str:
        ascii_value = ord(i)
        if 97 <= ascii_value <= 122:
            ascii_value -= 32
        print("{:s}".format(chr(ascii_value)), end='')
    print()
