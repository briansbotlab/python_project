# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 03:21:17 2018

@author: superuser
"""

import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4], [1, 4, 9, 16],'bd')
plt.ylabel('some numbers')
fig = plt.figure()
fig.patch.set_facecolor('black') #background
plt.show()