#!/usr/bin/python3
"""_summary_

    Returns:
        _type_: _description_
"""


class Student:
    """_summary_
    """

    def __init__(self, first_name, last_name, age):
        """_summary_

        Args:
            first_name (_type_): _description_
            last_name (_type_): _description_
            age (_type_): _description_
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """_summary_

        Args:
            attrs (_type_, optional): _description_. Defaults to None.

        Returns:
            _type_: _description_
        """
        dict_2 = {}
        if isinstance(attrs, list):
            for i in attrs:
                if i in self.__dict__:
                    dict_2[i] = self.__dict__[i]
            return dict_2
        return self.__dict__

    def reload_from_json(self, json):
        """_summary_

        Args:
            json (_type_): _description_
        """
        for i, j in json.items():
            setattr(self, i, j)
