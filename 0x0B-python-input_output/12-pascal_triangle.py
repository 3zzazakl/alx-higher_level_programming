#!/usr/bin/python3
"""_summary_
"""


def pascal_triangle(n):
    """_summary_

    Args:
        n (_type_): _description_

    Returns:
        _type_: _description_
    """
    if n <= 0:
        return []
    else:
        rows = [[1] for i in range(n)]
        for i in range(1, n):
            for j in range(i):
                try:
                    prev = rows[i - 1][j + 1]
                except IndexError:
                    prev = 0
                rows[i].append(prev + rows[i-1][j])
        return rows
