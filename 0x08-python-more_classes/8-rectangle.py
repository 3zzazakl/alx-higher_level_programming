#!/usr/bin/python3
"""
setting a rectangle class for task.
"""


class Rectangle:
    """
    rectangle class
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes rectangle instance with width and height."""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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
        disp = '\n'.join([str(self.print_symbol) *
                          self.__width for i in range(self.__height)])
        return disp

    def __repr__(self):
        """return string representation
        """
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        "delete message"
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """compares 2 instances

        Args:
            rect_1 (int): first instance
            rect_2 (int): second instance

        Raises:
            TypeError: if rect_1 or rect_2 isn't an instance

        Returns:
            rect_1: first instance area >= second
            rect_2: first instance area < second
        """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            return rect_1 if rect_1.area() >= rect_2.area()\
                else rect_2
