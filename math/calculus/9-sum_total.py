#!/usr/bin/env python3
""" File that contians the function summation_i_squared"""
import numpy as np


def summation_i_squared(n):
    """ Function that sum """

    if (n):
        serie = np.arange(1, n + 1)
        serie_pow = np.power(serie, 2)
        result = np.sum(serie_pow)
        return result
