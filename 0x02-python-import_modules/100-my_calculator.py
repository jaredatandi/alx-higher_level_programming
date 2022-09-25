#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, div, mul
    import sys

    args = len(sys.argv)
    if args != 4:
        print("usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(sys.argv[1])
    op = sys.argv[2]
    b = int(sys.argv[3])

    if op is '+':
        print("{} {} {} = {}".format(a, op, b, add(a, b)))
    elif op is '-':
        print("{} {} {} = {}".format(a, op, b, sub(a, b)))
    elif op is '*':
        print("{} {} {} = {}".format(a, op, b, mul(a, b)))
    elif op is '/':
        print("{} {} {} = {}".format(a, op, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
