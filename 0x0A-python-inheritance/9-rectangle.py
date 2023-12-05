#!/usr/bin/python3
"""_summary_

    Returns:
        _type_: _description_
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """_summary_

    Args:
        BaseGeometry (_type_): _description_
    """
    def __init__(self, width, height):
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.__width * self.__height

    def __str__(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return "[{}] {}/{}".format(
                self.__class__.__name__, self.__width, self.__height)
