#!/usr/bin/python3
"""_summary_

    Returns:
        _type_: _description_
"""
from models.base import Base


class Rectangle(Base):
    """_summary_
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """_summary_

        Args:
            width (_type_): _description_
            height (_type_): _description_
            x (int, optional): _description_. Defaults to 0.
            y (int, optional): _description_. Defaults to 0.
            id (_type_, optional): _description_. Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.__width

    @width.setter
    def width(self, width):
        """_summary_

        Args:
            value (_type_): _description_
        """
        if type(width) is not int:
            raise TypeError('width must be an integer')
        if width <= 0:
            raise ValueError('width must be > 0')
        self.__width = width

    @property
    def height(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.__height

    @height.setter
    def height(self, height):
        """_summary_

        Args:
            value (_type_): _description_
        """
        if type(height) is not int:
            raise TypeError('height must be an integer')
        if height <= 0:
            raise ValueError('height must be > 0')
        self.__height = height

    @property
    def x(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.__x

    @x.setter
    def x(self, x):
        """_summary_

        Args:
            value (_type_): _description_
        """
        if type(x) is not int:
            raise TypeError('x must be an integer')
        if x < 0:
            raise ValueError('x must be > 0')
        self.__x = x

    @property
    def y(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.__y

    @y.setter
    def y(self, y):
        """_summary_

        Args:
            value (_type_): _description_
        """
        if type(y) is not int:
            raise TypeError('y must be an integer')
        if y < 0:
            raise ValueError('y must be > 0')
        self.__y = y

    def area(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.width * self.height

    def display(self):
        """_summary_
        """
        for i in range(self.height):
            print("#" * self.width)

    def __str__(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)
