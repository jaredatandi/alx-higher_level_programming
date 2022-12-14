#!/usr/bin/python3
def safe_print_list_integers(my_list, x=0):
    """description: Docstring for safe_print_list_integers
    :returns: number of printed elements
    """
    c = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            c += 1
        except (ValueError, TypeError):
            pass
    print()
    return (c)
