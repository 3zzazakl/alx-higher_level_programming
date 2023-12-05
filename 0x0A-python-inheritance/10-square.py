#!/usr/bin/python3
"""_summary_
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """_summary_

    Args:
        Rectangle (_type_): _description_
    """
    def __init__(self, size):
        """_summary_

        Args:
            size (_type_): _description_
        """
        self.integer_validator("size", size)
        Rectangle.__init__(self, size, size)
        self.__size = size
