#!/usr/bin/python3
"""
This is module is used to
"""


def matrix_divided(matrix, div):
    """this function used to divide integers

    Args:
        matrix (int): list of lists
        div (int): number to divided by

    Raises:
        TypeError: matrix must be a matrix (list of lists) of integers
        TypeError: Each row of the matrix must have the same size
        TypeError: _description_
        ZeroDivisionError: division by zero
        TypeError: div must be a number

    Returns:
        _type_: new list with divided numbers.
    """
    err2 = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or not all(
         isinstance(i, list) for i in matrix):
        raise TypeError(err2)
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = []
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError(err2)
            new_row.append(round(elem / div, 2))
        new_matrix.append(new_row)

    return new_matrix
