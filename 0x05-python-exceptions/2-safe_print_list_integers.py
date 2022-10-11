#!/usr/bin/python3
def safe_print_list_integers(my_list, x=0):
    """TODO: Docstring for .
    :returns: TODO
    """
    i = 0
    try:
        while (i < x):
            print("{:d}".format(my_list[i]), end="")
            i += 1
    except Exception as e:
        pass
    print()
    return (i)
