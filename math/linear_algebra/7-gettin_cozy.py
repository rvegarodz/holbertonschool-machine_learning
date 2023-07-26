#!/usr/bin/env python3
""" This file contains the function called cat_arrays() """


def cat_matrices2D(mat1, mat2, axis=0):
    """
    Function that concatenates two matrices along a specific axis.
    Arguments:
        mat1: nested list
        mat2: nested list
        axis: specific axis
    Returns: new matrix
    """
    nw_matrix = []
    if (len(mat1) != len(mat2) and mat1 and mat2):
        if (axis == 0):
            nw_matrix = []
            for i in mat1:
                nw_matrix.append(list(i))
            for j in mat2:
                nw_matrix.append(list(j))
        else:
            if (len(mat1) == len(mat2)):
                for i in range(len(mat1)):
                    nw_matrix.append(mat1[i] + mat2[i])
        return nw_matrix
    return None
