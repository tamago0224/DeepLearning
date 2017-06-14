#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
#Created 2017-06-13
#
import numpy as np
import matplotlib.pyplot as plt

def step_function(x):
    return np.array(x > 0, dtype=np.int)

x = np.arange(-5.0, 5.0, 0.1)
y = step_function(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)#y軸の指定
plt.show()
