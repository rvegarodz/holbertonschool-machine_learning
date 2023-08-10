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
            sum = 0
            for i in range(len(self.data)):
                sum += self.data[i]
            m = 1 / (sum / len(self.data))
            exponent = (-m) * 0
            result = m * (e ** exponent)
            self.__lambtha = result

    def pdf(self, x):
        "This method calculate Poisson Mass Function (PMF)"
        if x < 0:
            return 0
        e = 2.7182818285
        m = self.__lambtha
        exponent = (-m) * x
        result = m * (e ** exponent)
        return result
