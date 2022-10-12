#!/usr/bin/python3
def safe_print_division(a, b):
    """safe_print_division: Docstring for safe_print_division.

    :a : the first operand
    :b : the second operand
    :returns: quotient

    """
    try:
        res = (a / b)
    except (ZeroDivisionError, ValueError) as err:
        res = None
    finally:
        print("Inside result: {}".format(res))
    return (res)

