#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    if (len(matrix) == 0):
        return (None)
    new_matrix = []
    for row in matrix:
        new_matrix.append([i ** 2 for i in row])
    return (new_matrix)
