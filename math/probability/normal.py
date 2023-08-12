#!/usr/bin/env python3
"This file have the class Normal()"


class Normal():
    "This class represent a normal distribution"

    def __init__(self, data=None, mean=0., stddev=1.):
        self.data = data
        self.mean = float(mean)
        self.stddev = float(stddev)

    @property
    def mean(self):
        return self.__mean

    @mean.setter
    def mean(self, mean):
        if self.data is None:
            self.__mean = float(mean)
        else:
            if type(self.data) != list:
                raise TypeError("data must be a list")
            if len(self.data) < 2:
                raise ValueError("data must contain multiple values")
            sum = 0
            for i in range(len(self.data)):
                sum += self.data[i]
            self.__mean = (sum / len(self.data))

    @property
    def stddev(self):
        return self.__stddev

    @stddev.setter
    def stddev(self, stddev):
        if stddev <= 0:
            raise ValueError("stddev must be a positive value")
        if self.data is None:
            self.__stddev = float(stddev)
        else:
            sum = 0
            for i in range(len(self.data)):
                sum += ((self.data[i] - self.mean) ** 2)
            variance = (sum / len(self.data))
            self.__stddev = variance ** 0.5

    def z_score(self, x):
        "Function that calculates the z-score of a given x-value"
        if x:
            z = (x - self.mean) / self.stddev
            return z

    def x_value(self, z):
        "Function that calculates the x-value of a given z-score"
        if z:
            x = z * self.stddev + self.mean
            return x

    def pdf(self, x):
        "Function that calculates the value of the PDF for a given x-value"
        if x:
            e = 2.7182818285
            pi = 3.1415926536
            m = self.mean
            r = self.stddev
            exponent = ((x - m) ** 2) / (2 * (r ** 2))
            base = (1 / (r * ((2 * pi) ** 0.5)))
            x_pdf = base * (e ** (-exponent))
            return x_pdf
