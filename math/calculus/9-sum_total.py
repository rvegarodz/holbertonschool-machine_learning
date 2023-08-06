#!/usr/bin/env python3
""" File that contians the function summation_i_squared"""
import numpy as np


def summation_i_squared(n):
    """ Function that sum """

    if (type(n) is int):
        serie = list(range(1, n + 1))
        serie_pow = list(map(lambda x: x ** 2, serie))
        result = sum(serie_pow)
        return result
    else:
        return None
