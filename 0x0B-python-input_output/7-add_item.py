#!/usr/bin/python3
"""_summary_
"""
import sys
import os
save_to_json = __import__("5-save_to_json_file").save_to_json_file
load_from_json = __import__("6-load_from_json_file").load_from_json_file


def add_item(args, filename):
    """_summary_

    Args:
        args (_type_): _description_
        filename (_type_): _description_
    """

    if (os.path.exists(filename)):
        content = load_from_json(filename)
    else:
        content = []
    content.extend(args)
    save_to_json(content, filename)
