#!/usr/bin/env python3
"This file have the class Poisson()"


class Poisson():
    "This class represent a poisson distribution"

    def __init__(self, data=None, lambtha=1.):
        pi = 3.1415926536
        e = 2.7182818285

        if data:
            if type(data) != list:
                raise TypeError("data must be a list")
            elif len(data) < 2:
                raise ValueError("data must contain multiple values")
            else:
                mean = sum(item for item in data) / len(data)
                self.lambtha = float(mean)
        else:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            else:
                self.lambtha = float(lambtha)

    def pmf(self, k):
        if type(k) == int:
            result = 1
            for i in range(1, k + 1):
                result *= i
            return result
        else:
            return 0
