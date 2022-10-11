#!/usr/bin/python3
def safe_print_integer(value):
    """safe_print_integer: prints an integer with
    error handling
    :returns: True if it is printed, false if not
    """
    try:
        print("{:d}".format(value))
        return (True)
    except Exception as e:
        return (False)
        raise e
