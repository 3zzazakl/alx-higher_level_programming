#!/usr/bin/python3
"""reading a text file and prints it to stdout."""


def read_file(filename=""):
    """_summary_

    Args:
        filename (str, optional): _description_. Defaults to "".
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
