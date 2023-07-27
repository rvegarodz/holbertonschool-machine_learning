#!/usr/bin/env python3
""" This file contains the function called mat_mul() """


def mat_mul(mat1, mat2):
    """ Function that performs matrix multiplication """
    if (mat1 and mat1[0]):
        mat1_shape = [len(mat1), len(mat1[0])]
    if (mat2 and mat2[0]):
        mat2_shape = [len(mat2), len(mat2[0])]
    if (mat1_shape[1] == mat2_shape[0]):
        nw_matrix = []
        for i in range(mat1_shape[0]):
            nw_row = []
            for j in range(mat2_shape[1]):
                result = 0
                for idx in range(mat1_shape[1]):
                    result += mat1[i][idx] * mat2[idx][j]
                nw_row.append(result)
            nw_matrix.append(nw_row)
        return nw_matrix
    return None
