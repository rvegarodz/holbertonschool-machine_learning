#!/usr/bin/env python3

# Function that find the shape of a matrix using recursion
def matrix_shape(matrix):
    if (matrix):
        shape = []
        count = len(matrix)
        shape.append(count)

        if (count > 0):
            count1 = 0
            for i in matrix:
                if (isinstance(i, list)):
                    shape1 = matrix_shape(i)
                    for j in shape1:
                        shape.append(j)
                    break
                else:
                    count1 += 1
    return (shape)
