#!/usr/bin/python3
"""_summary_
"""


def append_write(filename="", text=""):
    """_summary_

    Args:
        filename (str, optional): _description_. Defaults to "".
        text (str, optional): _description_. Defaults to "".

    Returns:
        _type_: _description_
    """
    with open(filename, "a", encoding="utf-8") as f:
        count = f.write(text)
    return count
