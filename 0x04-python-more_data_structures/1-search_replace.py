#!/usr/bin/python3
def search_replace(my_list, search, replace):
    cp = []
    for i in range(len(my_list)):
        if my_list[i] == search:
            cp.append(replace)
        else:
            cp.append(my_list[i])
    return cp
