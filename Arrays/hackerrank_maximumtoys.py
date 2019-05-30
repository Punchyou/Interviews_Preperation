"""
Mark and Jane are very happy after having their first child.
Their son loves toys, so Mark wants to buy some.
There are a number of different toys lying in front of him,
tagged with their prices.
Mark has only a certain amount to spend,
and he wants to maximize the number of toys
he buys with this money.

Given a list of prices and an amount to spend,
what is the maximum number of toys
Mark can buy? For example, if  and Mark
has  to spend, he can buy items  for ,
or  for  units of currency.
He would choose the first group of  items.

Function Description

Complete the function maximumToys in the editor below.
It should return an integer representing
the maximum number of toys Mark can purchase.

maximumToys has the following parameter(s):

prices: an array of integers representing toy prices
k: an integer, Mark's budget
Input Format

The first line contains two integers,  and ,
the number of priced toys
and the amount Mark has to spend. 
The next line contains  space-separated integers 



A toy can't be bought multiple times.

Output Format

An integer that denotes the maximum
number of toys Mark can buy for his son.

Sample Input

7 50
1 12 5 111 200 1000 10
Sample Output

4
Explanation

He can buy only  toys at most. These toys have the following prices: .
"""

# The list has to be merged first. We'll use merge sort.


def merge_sort(prices):

    length = len(prices)
    if length <= 1:
        return length
    
    # First, divide the list into equal-sized sublist
    right_l = prices[:length//2]
    left_l = prices[length//2:]
    print("Left :", left_l, "\nRight: ", right_l)

    # Recursively sort both sublists
    right_l = merge_sort(right_l)
    left_l = merge_sort(left_l)
    print("Left :", left_l, "\nRight: ", right_l)

    return merge(left_l, right_l)
    
def merge(left_l, right_l):

    result = []

    # sort each sublist
    while left_l or right_l:
        if left_l[0] <= right_l[0]:
            result.append(left_l[0])
            left_l.pop(0)
        else:
            result.append(right_l[0])
            right_l.pop(0)

    # Either left or right may have elements left; consume them.
    # Only one of the following loops will actually be entered.
    
    while left_l:
        result.append(left_l[0])
        left_l.pop(0)
    while right_l:
        result.append(right_l[0])
        right_l.pop(0)
    return result

def maximumToys(merged_list, k):
    """
    Finds the maximum number of list items
    that their sum goes up to k.
    """
    
    mon_sum = 0
    num_toys = 0
    for toy in merged_list:
        if mon_sum < k:
            mon_sum += toy
            num_toys += 1
        else:
            break 

    return mon_sum

merged_list = merge_sort([1, 12, 5, 111, 200, 1000, 10])
maximumToys(merged_list, 50)
