#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
#Created 2017-06-12
#
import numpy as np
import matplotlib.pyplot as plt

#データの生成
x = np.arange(0, 6, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)

#draw graph
plt.plot(x, y1, label="sin")
plt.plot(x, y2, label="cos")
plt.plot(x, y3, label="tan")
plt.xlabel("x")
plt.ylabel("y")
plt.title("sin & cos")
plt.legend()
plt.show()
