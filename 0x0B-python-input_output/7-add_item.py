#!/usr/bin/python3
"""_summary_."""
import sys

save_to_json = __import__("5-save_to_json_file").save_to_json_file
load_from_json = __import__("6-load_from_json_file").load_from_json_file


if __name__ == "__main__":
    try:
        my_list = load_from_json("add_item.json")
    except FileNotFoundError:
        my_list = []
    my_list += sys.argv[1:]
    save_to_json(my_list, "add_item.json")
