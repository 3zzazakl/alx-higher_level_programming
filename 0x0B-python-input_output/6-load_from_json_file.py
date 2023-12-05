#!/usr/bin/python3
"""_summary_

    Returns:
        _type_: _description_
"""

import json


def load_from_json_file(filename):
    """_summary_

    Args:
        filename (_type_): _description_

    Returns:
        _type_: _description_
    """
    with open(filename, encoding="utf-8") as f:
        my_obj = json.loads(f.read())
    return my_obj
