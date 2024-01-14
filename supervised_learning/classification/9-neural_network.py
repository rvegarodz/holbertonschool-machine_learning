#!/usr/bin/env python3
""" Module contains NeuralNetwork Class """
import numpy as np


class NeuralNetwork:
    """ NeuralNetwork with one hidden layer performing binary
        classification """
    def __init__(self, nx, nodes):
        if type(nx) is not int:
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        if type(nodes) is not int:
            raise TypeError("nodes must be a integer")
        if nodes < 1:
            raise ValueError("nodes must be a positive integer")

        self.W1 = np.random.normal(size=(nodes, nx))
        self.b1 = np.zeros((nodes, 1))
        self.A1 = 0

        self.W2 = np.random.normal(size=(1, nodes))
        self.b2 = 0
        self.A2 = 0

    @property
    def W1(self):
        """Getter function"""
        return self.__W1

    @property
    def W2(self):
        """Getter function"""
        return self.__W2

    @property
    def b1(self):
        """Getter function"""
        return self.__b1

    @property
    def b2(self):
        """Getter function"""
        return self.__b2

    @property
    def A1(self):
        """Getter function"""
        return self.__A1

    @property
    def A2(self):
        """Getter function"""
        return self.__A2