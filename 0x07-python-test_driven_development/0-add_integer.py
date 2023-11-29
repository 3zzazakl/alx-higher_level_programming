#!/usr/bin/python3
"""
This is module is used to add integers.

add_integer_to_: this is function to add integer
"""


def add_integer(a, b=98):
    """
    adding two numbers
    :param a: first number
    :param b: second number
    :return: summation of the two numbers
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
