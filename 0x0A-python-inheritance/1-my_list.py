#!/usr/bin/python3
"""prints the list, but sorted (ascending sort)."""


class MyList(list):
    """class to print sorted list

    Args:
        list (_type_): input list
    """
    def print_sorted(self):
        """function to print sorted list
        """
        print(sorted(self))
