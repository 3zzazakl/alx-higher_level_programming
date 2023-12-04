#!/usr/bin/python3
"""Check if object is exactly an instance of the specified class"""


def is_same_class(obj, a_class):
    """Check if object is exactly an instance of specified class

    Args:
        obj (_type_): input object
        a_class (_type_): input class

    Returns:
        _type_: True of the same, otherwise False.
    """

    if type(obj) == a_class:
        return True
    return False
