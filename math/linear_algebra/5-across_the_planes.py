#!/usr/bin/env python3
""" This file contains the function called add_matrices2D """


def add_matrices2D(mat1, mat2):
    """
    Funciton that transpose matrix
    Arguments:
        mat1: nested list
        mat2: nested list
    Returns: new matrix with sum of both arguments
    """
    if (len(mat1[0]) == len(mat2[0])):
        nw_matrix = []
        row_len = len(mat1[0])
        for i in range(len(mat1)):
            nw_row = []
            for j in range(row_len):
                nw_row.append(mat1[i][j] + mat2[i][j])
            nw_matrix.append(nw_row)
        return nw_matrix
    else:
        return None
