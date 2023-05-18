#!/usr/bin/python3
def islower(c):
    """TODO: checks a char for lowercase 
    :returns: True or False 

    """
    b = ord(c)
    if b in range(ord('a'), ord('z')):
        return True
    else:
        return False
