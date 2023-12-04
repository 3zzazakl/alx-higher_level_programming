#!/usr/bin/python3
"""function that returns the list of available attributes."""


def lookup(obj):
    """function to list of available attributes

    Args:
        obj (_type_): input object

    Returns:
        _type_: all attributes
    """
    return dir(obj)
