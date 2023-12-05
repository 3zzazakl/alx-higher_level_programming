#!/usr/bin/python3
"""_summary_

    Returns:
        _type_: _description_
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

    def __str__(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return "[{}] {}/{}".format(
                self.__class__.__name__, self.__size, self.__size)
