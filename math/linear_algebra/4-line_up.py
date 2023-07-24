#!/usr/bin/env python3
""" File that contians the function add_arrays() """


def add_arrays(arr1, arr2):
    """ Function that sums two arrays """
    if (len(arr1) == len(arr2)):
        nw_array = []
        for i in range(len(arr1)):
            nw_array.append(arr1[i] + arr2[i])
        return (nw_array)
    else:
        return (None)
