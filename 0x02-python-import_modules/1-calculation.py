#!/usr/bin/python3

from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(b, a, sub(b, a)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {:.2f}".format(a, b, div(a, b)))
