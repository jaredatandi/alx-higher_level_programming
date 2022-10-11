#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        i = 0
        while(i < x):
            for i in my_list:
                print("{}".formart(i));
            i += 1
    except IndexError:
        print("Out of range")
    return (i)
