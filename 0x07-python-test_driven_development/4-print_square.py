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
    if not isinstance(size, (int, float)) \
            or (isinstance(size, float) and int(size < 0)):
        raise TypeError("size must be an integer")
    else:
        if int(size) < 0:
            raise ValueError("size must be >= 0")
        else:
            for i in range(int(size)):
                print('#' * int(size))
