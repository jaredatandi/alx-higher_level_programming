#!/usr/bin/python3
import sys

argument = sys.argv

print_last_digit = __import__('9-print_last_digit').print_last_digit

l = print_last_digit(int(argument[1]))
print(l)
