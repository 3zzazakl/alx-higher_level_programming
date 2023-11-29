#!/usr/bin/python3
"""Defines a name function."""


def say_my_name(first_name, last_name=""):
    """"Define a name function

    Keyword arguments:
    first_name -- first argument
    second -- second argument
    Return: return_description
    """
    if not isinstance(first_name, str) or not isinstance(last_name, str):
        raise TypeError("first_name must be a string")
    if last_name:
        print("My name is {} {}".format(first_name, last_name))
    else:
        print("My name is {}".format(first_name))
