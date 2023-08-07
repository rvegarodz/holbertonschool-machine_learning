#!/usr/bin/env python3
""" File that contians the function poly_derivative"""


def poly_derivative(poly):
    """ Function that calculates the derivative of a polynomial"""
    if (type(poly) != list):
        return None
    else:
        result = []
        lenn = len(poly)
        if (lenn == 0):
            return result.append(0)
        elif (lenn == 1):
            return result.append(0)
        else:
            for i in range(lenn):
                if i == 0:
                    continue
                elif i == 1:
                    result.append(poly[i] * i)
                else:
                    result.append(poly[i] * i)
            return result
