# -*- coding: utf-8 -*-
"""
Created on Wed May 22 19:29:37 2019

@author: Maria
"""

import sys

n = 10
data = []
for i in range(50):
    a = len(data)
    b = sys.getsizeof(data)
    print('Length: {0:3d}; Size in bytes: {1:4d}'.format(a, b))
    data.append(n)