#!/usr/bin/env python3
"This file have the class Poisson()"


class Poisson():
    "This class represent a poisson distribution"

    def __init__(self, data=None, lambtha=1.):
        self.data = data
        self.lambtha = lambtha

    @property
    def lambtha(self):
        return self.__lambtha

    @lambtha.setter
    def lambtha(self, lambtha):
        pi = 3.1415926536
        e = 2.7182818285
        if lambtha <= 0:
            raise ValueError("lambtha must be a positive value")
        if self.data is None:
            self.__lambtha = float(lambtha)
        else:
            if type(self.data) != list:
                raise TypeError("data must be a list")
            if len(self.data) < 2:
                raise ValueError("data must contain multiple values")
            mean = sum(item for item in self.data) / len(self.data)
            self.__lambtha = float(mean)

    def pmf(self, k):
        "This method calculate Poisson Mass Function (PMF)"
        if k <= 0:
            return 0
        if not isinstance(k, int):
            k = int(k)
        e = 2.7182818285
        result = 1
        for i in range(1, k + 1):
            result *= i
        return ((e ** -self.lambtha) * (self.lambtha ** k) / result)

    def cdf(self, k):
        "This method calculate Cumulative Distribution Function (CDF)"
        if k < 0:
            return 0
        if not isinstance(k, int):
            k = int(k)
        e = 2.7182818285
        cdf_result = 0
        for i in range(0, k+1):
            factorial = 1
            for j in range(1, i+1):
                factorial *= j
            cdf_result += (self.lambtha ** i / factorial)
        return (cdf_result / e ** self.lambtha)
