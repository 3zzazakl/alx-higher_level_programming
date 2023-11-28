#!/usr/bin/python3
"""
"""


def print_square(size):
    if not isinstance(size, int):
        raise TyprError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
