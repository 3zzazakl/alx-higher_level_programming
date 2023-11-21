#!/usr/bin/python3
"""Write a class Square that defines a square by: (based on 1-square.py)
    Private instance attribute: size
    Instantiation with optional
    """


class Square:
    """Write a class Square that defines a square

    Args:
        size: input variable
    """

    __size = None

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
