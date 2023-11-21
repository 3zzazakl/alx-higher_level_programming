#!/usr/bin/python3
"""Area of a square

    Raises:
        TypeError: _description_
        ValueError: _description_
    """


class Square:
    """Area of a square

    Attributes:
        __size (int): the size of square

    Raises:
        TypeError: _description_
        ValueError: _description_
    """

    __size = None
    area = None

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size ** 2
