#!/usr/bin/env python3
""" This file contains the function called matrix_transpose()"""


def matrix_transpose(matrix):
    """
    Funciton that transpose matrix
    Arguments:
        matrix: nested list
    Returns: new transposed matrix
    """
    if (matrix):
        nw_matrix = []
        col_len = len(matrix)
        if (col_len > 0):
            row_len = len(matrix[0])
        else:
            row_len = 0
        for i in range(row_len):
            nw_row = []
            for j in range(col_len):
                nw_row.append(matrix[j][i])
            nw_matrix.append(nw_row)
    return (nw_matrix)
