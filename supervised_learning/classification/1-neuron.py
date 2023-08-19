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