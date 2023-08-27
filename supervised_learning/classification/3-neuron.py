#!/usr/bin/env python3
"""File that contain Neuron class"""
import numpy as np


class Neuron():
    """Class that defines a single neuron performing binary classification"""

    def __init__(self, nx):
        """Init of the Neuron class"""
        if type(nx) != int:
            raise TypeError("nx must be an integer")
        elif nx < 1:
            raise ValueError("nx must be a positive integer")
        else:
            self.__W = np.random.normal(size=(1, nx))
            self.__b = 0
            self.__A = 0

    @property
    def W(self):
        """Getter function of __W"""
        return self.__W

    @property
    def b(self):
        """Getter function of __b"""
        return self.__b

    @property
    def A(self):
        """Getter function of __A"""
        return self.__A

    def forward_prop(self, X):
        """Funtion that calculates the forward propagation of the neuron"""
        fwp = np.matmul(self.__W, X) + self.__b
        self.__A = 1/(1+np.exp(-fwp))
        return self.__A

    def cost(self, Y, A):
        """ Function that calculates the cost of the model using log"""
        m = Y.shape[1]
        Ymult = np.multiply(Y, np.log(A))
        Amult = np.multiply(1-Y, np.log(1.0000001-A))
        total_cost = -(1/m) * np.sum(Ymult + Amult)
        return total_cost
