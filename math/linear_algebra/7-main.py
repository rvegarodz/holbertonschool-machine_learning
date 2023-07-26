#!/usr/bin/env python3
import sys
cat_matrices2D = __import__('7-gettin_cozy').cat_matrices2D
m1 = [[-54, -87, 56, -92, 81], [54, 16, -72, 42, 901]]
m2 = [[12, 63], [-10, 69]]
m = cat_matrices2D(m1, m2, axis=1)
if type(m) is not list or m is m1 or m is m2 or not len(m) or type(m[0]) is not list:
    print("Not a new matrix")
    sys.exit(1)
print(m)