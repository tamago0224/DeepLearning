#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
#Created 2017-06-14
#
import numpy as np
import matplotlib.pylab as plt

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

if __name__ == '__main__':
    X = np.arange(-5.0, 5.0, 0.1)
    Y = sigmoid(X)
    plt.plot(X, Y)
    plt.ylim(-0.1, 1.1)
    plt.show()
