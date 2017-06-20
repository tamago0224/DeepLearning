#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
#Created 2017-06-20
#
import numpy as np
import matplotlib.pylab as plt

def function_1(x):
    return 0.01*x**2+0.1+x

x = np.arange(0, 20.0, 0.1)
y = function_1(x)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.plot(x, y)
plt.show()

