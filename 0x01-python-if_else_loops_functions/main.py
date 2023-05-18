#!/usr/bin/python3
import sys
pow = __import__('11-pow').pow

argument = sys.argv
arg1 = int(argument[1])
arg2 = int(argument[2])

print(pow(arg1, arg2))
