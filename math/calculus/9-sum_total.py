#!/usr/bin/env python3
""" File that contians the function summation_i_squared"""


def summation_i_squared(n):
    """ Function that sum """

    if (n >= 0 and type(n) == int):
        serie = list(range(1, n + 1))
        serie_pow = list(map(lambda x: x ** 2, serie))
        result = sum(serie_pow)
        return result
    else:
        return None
