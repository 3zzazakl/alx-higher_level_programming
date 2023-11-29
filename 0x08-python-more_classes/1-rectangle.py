#!/usr/bin/python3
"""
setting a rectangle class for task.
"""


class Rectangle:
    """
    rectangle class
    """

    def __init__(self, width=0, height=0):
        """Initializes rectangle instance with width and height."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrieve width of rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """set width of rectangle instance"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise TypeError("width must be >= 0")
        else:
            self.__witdth = value

    @property
    def height(self):
        """retrieve height of rectangle instance"""
        return self.__height

    @height.setter
    def height(self, value):
        """set height of rectangle instance"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
