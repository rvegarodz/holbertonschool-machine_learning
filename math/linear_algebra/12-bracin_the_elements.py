#!/usr/bin/env python3
""" This file contains the function called np_elementwise() """


def np_elementwise(mat1, mat2):
    """ Function that performs element-wise addition,
    subtraction, multiplication, and division """
    add = mat1 + mat2
    sub = mat1 - mat2
    mul = mat1 * mat2
    div = mat1 / mat2
    return (add, sub, mul, div)
