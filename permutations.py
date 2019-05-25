# -*- coding: utf-8 -*-
"""
Created on Tue May 21 19:25:21 2019

@author: Maria
"""

from functools import reduce

input_str = '1 2 3 4 5'
input_str2 = '1 4 5 2 3'


def ispermutation(input_1, input_2):
  """Function that checks if two arrays are permutaions of each other."""
  l1 = [int(x) for x in input_1.split()]
  l2 = [int(x) for x in input_2.split()]
  
  return sum(l1) == sum(l2) and \
    reduce(lambda x1, x2: x1*x2, l1) == reduce(lambda x1, x2: x1*x2, l2)

#print the ouput
if ispermutation(input_str, input_str2):
  print("YES")
else:
  print("NO")