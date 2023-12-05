#!/usr/bin/python3
"""_summary_

    Raises:
        Exception: _description_
        TypeError: _description_
        ValueError: _description_
"""


class BaseGeometry:
    """_summary_
    """
    def area(self):
        """Raises an Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates values

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is <= 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
