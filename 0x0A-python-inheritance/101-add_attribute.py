#!/usr/bin/python3
"""_summary_
"""


def add_attribute(obj, attr, value):
    """_summary_

    Args:
        obj (_type_): _description_
        attr (_type_): _description_
        value (_type_): _description_

    Raises:
        TypeError: _description_
    """

    if hasattr(obj, '__dict__'):
        obj.__dict__[attr] = value
    else:
        raise TypeError("can't add new attribute")
