#!/usr/bin/python3
"""_summary_
"""
from ast import arg
from models.rectangle import Rectangle


class Square(Rectangle):
    """_summary_

    Args:
        Rectangle (_type_): _description_
    """
    def __init__(self, size, x=0, y=0, id=None):
        """_summary_

        Args:
            size (_type_): _description_
            x (int, optional): _description_. Defaults to 0.
            y (int, optional): _description_. Defaults to 0.
            id (_type_, optional): _description_. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        )

    @property
    def size(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.width

    @size.setter
    def size(self, value):
        """_summary_

        Args:
            size (_type_): _description_
            value (_type_): _description_
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        lst = (self.id, self.size, self.x, self.y)
        if args:
            self.id, self.size, self.x, self.y = \
                args + lst[len(args):len(lst)]
        elif kwargs:
            for (key, value) in kwargs.items():
                setattr(self, key, value)
