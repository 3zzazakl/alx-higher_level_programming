#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if matrix is not None:
        for row in matrix:
            if len(row) > 0:
                for i, col in enumerate(row):
                    print("{:d}".format(col), end=" " if i != len(row) - 1 else "")
                print("")
            else:
                continue
