#!/usr/bin/env python3
""" This file contains the function called np_slice() """
import numpy as np


def np_slice(matrix, axes={}):
    """ Function that slices a matrix along specific axes """
    if (matrix):
        nw_mtrx = np.array(matrix)
        for k, v in axes.items():
            if (matrix[k]):
                ## without steps (i)
                if (len(axes) == 2):


                ## with (i)
                else:






    return nw_mtrx