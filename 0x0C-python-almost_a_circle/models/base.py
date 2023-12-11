#!/usr/bin/python3
"""_summary_
"""


class Base:
    """_summary_
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """"summary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        if id is not None:
            self.id = id

        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
