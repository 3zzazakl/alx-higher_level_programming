#!/usr/bin/python3
"""_summary_

    Returns:
        _type_: _description_
"""


class MyInt(int):
    """_summary_

    Args:
        int (_type_): _description_
    """

    def __init__(self, numb):
        """_summary_

        Args:
            numb (_type_): _description_
        """
        self.num = numb

    def __eq__(self, value):
        """_summary_

        Args:
            value (_type_): _description_

        Returns:
            _type_: _description_
        """
        return (self.num != value)

    def __ne__(self, value):
        """_summary_

        Args:
            value (_type_): _description_

        Returns:
            _type_: _description_
        """
        return (self.num == value)
