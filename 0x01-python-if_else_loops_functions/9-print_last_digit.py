#!/usr/bin/python3
def print_last_digit(number):
    """TODO: Docstring for print_last_digit.
    :returns: TODO

    """
    last_digit = abs(number) % 10
    if number > 0:
        print("{:d}".format(last_digit))
    else:
        print("{:d}".format(last_digit * -1), end="")
