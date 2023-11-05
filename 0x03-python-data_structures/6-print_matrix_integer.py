#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if matrix is not None:
        for row in matrix:
            if len(row) > 0:
                for col in row:
                    print("{:d}".format(col), end=" ")
                print("")
            else:
                continue
