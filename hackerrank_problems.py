# -*- coding: utf-8 -*-
"""
Created on Thu May 23 13:51:18 2019

@author: Maria
"""

"""
John works at a clothing store. He has a large pile of socks that he must pair by color for sale. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

For example, there are
socks with colors . There is one pair of color and one of color . There are three odd socks left, one of each color. The number of pairs is

.

Function Description

Complete the sockMerchant function in the editor below. It must return an integer representing the number of matching pairs of socks that are available.

sockMerchant has the following parameter(s):

    n: the number of socks in the pile
    ar: the colors of each sock

Input Format

The first line contains an integer
, the number of socks represented in .
The second line contains space-separated integers describing the colors

of the socks in the pile.

Constraints

where

Output Format

Return the total number of matching pairs of socks that John can sell.

Sample Input

9
10 20 20 10 10 30 50 10 20
"""
from collections import Counter
n = 9
ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
def sockMerchant(n, ar):
    socks = 0
    ar_count = Counter(ar)
    print(ar_count)
    for i in ar:
        if ar_count[i] % 2 == 0:
            socks += ar_count[i]/2
    return socks

sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20])
