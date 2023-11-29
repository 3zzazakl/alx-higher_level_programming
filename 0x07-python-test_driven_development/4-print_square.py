#!/usr/bin/python3
"""define a square function."""


def print_square(size):
    """printing a square with # character.

    Args:
        size (int): the height/width of the square

    Raises:
        TypeError: if size isn't integer.
        ValueError: if size is < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
