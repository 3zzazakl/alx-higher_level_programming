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
        else:
            if value < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = value

    @property
    def height(self):
        """retrieve height of rectangle instance"""
        return self.__height

    @height.setter
    def height(self, value):
        """set height of rectangle instance"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        else:
            if value < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__height = value

    def area(self):
        """return the area of rectangle"""
        return self.width * self.height

    def perimeter(self):
        """return the perimeter of rectangle."""
        return 2 * (self.width + self.height) \
            if self.width != 0 and self.height != 0 else 0

    def __str__(self):
        """print the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        disp = '\n'.join("#" * self.__width for i in range(self.__height))
        return disp

    def __repr__(self):
        """return string representation
        """
        return "Rectangle({:d}, {:d})".format(self.width, self.height)
