#!/usr/bin/env python3
"""File that contain Neuron class"""
import numpy as np
import matplotlib.pyplot as plt


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
        """Function that calculates the cost of the model using log"""
        m = Y.shape[1]
        Ymult = np.multiply(Y, np.log(A))
        Amult = np.multiply(1-Y, np.log(1.0000001-A))
        total_cost = -(1/m) * np.sum(Ymult + Amult)
        return total_cost

    def evaluate(self, X, Y):
        """Function that evaluates the neuron's predictions"""
        self.forward_prop(X)
        cost = self.cost(Y, self.__A)
        prediction = np.where(self.__A >= 0.5, 1, 0)
        return (prediction, cost)

    def gradient_descent(self, X, Y, A, alpha=0.05):
        """Function that calculates one pass of gradient descent"""
        m = Y.shape[1]
        dW = np.matmul(A-Y, X.T) / m
        db = np.sum(A-Y) / m
        self.__W = self.__W - (dW * alpha)
        self.__b = self.__b - (db * alpha)

    def train(self, X, Y, iterations=5000, alpha=0.05, verbose=True,
              graph=True, step=100):
        """Function that trains the neuron"""
        if type(iterations) != int:
            raise TypeError("iterations must be an integer")
        if iterations < 0:
            raise ValueError("iterations must be a positive integer")
        if type(alpha) != float:
            raise TypeError("alpha must be a float")
        if alpha < 0:
            raise ValueError("alpha must be positive")
        if verbose or graph:
            if type(step) != int:
                raise TypeError("step must be an integer")
            if step < 0 or step > iterations:
                raise ValueError("step must be positive and <= iterations")
        Cost = []
        Iterations = []
        for training in range(iterations):
            a, cost = self.evaluate(X, Y)
            self.__A = self.forward_prop(X)
            self.gradient_descent(X, Y, self.__A, alpha)
            if (training % step == 0):
                Cost.append(cost)
                Iterations.append(training)
                if verbose:
                    print("Cost after {} iterations: {}".format(training,
                                                                cost))
        if graph:
            plt.plot(Iterations, Cost, 'b')
            plt.xlabel('iteration')
            plt.xlim(0, 3000)
            plt.ylabel('cost')
            plt.title('Training Cost')
            plt.show()
        return self.evaluate(X, Y)
