#!/usr/bin/python3
"""sumary_line

Keyword arguments:
argument -- description
Return: return_description
"""


def append_after(filename="", search_string="", new_string=""):
    """_summary_

    Args:
        filename (str, optional): _description_. Defaults to "".
        search_string (str, optional): _description_. Defaults to "".
        new_string (str, optional): _description_. Defaults to "".
    """

    with open(filename, mode="r+", encoding="utf-8") as f:
        nw_text = ""
        for line in f:
            nw_text += line
            if search_string in line:
                nw_text += new_string
        f.seek(0)
        f.write(nw_text)
