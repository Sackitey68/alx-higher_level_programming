#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    return [list(map(lambda z: z ** 2, row)) for row in matrix]
