#!/usr/bin/env python3
"This file have the class Poisson()"


class Exponential():
    "This class represent a poisson distribution"

    def __init__(self, data=None, lambtha=1.):
        self.data = data
        self.lambtha = lambtha

    @property
    def lambtha(self):
        return self.__lambtha

    @lambtha.setter
    def lambtha(self, lambtha):
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
            m = 1 / (sum(item for item in self.data) / len(self.data))
            exponent = (-m) * 0
            result = m * (e ** exponent)
            self.__lambtha = float(result)

    def pdf(self, x):
        "This method calculate Poisson Mass Function (PMF)"
        if x <= 0:
            return 0
        if not isinstance(x, int):
            x = int(x)
        e = 2.7182818285
        m = self.__lambtha
        exponent = (-m) * x
        result = m * (e ** exponent)
        return float(result)
