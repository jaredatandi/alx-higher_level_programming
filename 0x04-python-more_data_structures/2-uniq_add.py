#!/usr/bin/python3
def uniq_add(my_list=[]):
    n = set(my_list)
    sum = 0
    for i in n:
        sum += i
    return sum
