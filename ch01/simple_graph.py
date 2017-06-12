#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
#Created 2017-06-12
#
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 6, 0.1)    #0から6までを0.1刻みで生成
y = np.sin(x)

#draw graph
plt.plot(x, y)
plt.show()
