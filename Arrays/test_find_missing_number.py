"""
Find the Missing Element
Problem
Consider an array of non-negative integers.
A second array is formed by shuffling the elements of the first array
and deleting a random element.
Given these two arrays, find which element is missing in the second array.

Here is an example input, the first array is shuffled and the number 5 is removed
to construct the second array.

Input:
finder([1,2,3,4,5,6,7],[3,7,2,1,4,6])

Output:
5 is the missing number
"""



#use of sorted()
def finder(arr, arr2):
    arr = sorted(arr)
    arr2 = sorted(arr2)
    for i in range(len(arr)-1):
        if not arr[i] == arr2[i]:
            print("%s is the missing number" % arr[i]) # try one line statement
            break
        elif arr[-1] != arr2[-1]:
            print("%s is the missing number" % arr[-1])
            break
finder([1,2,3,4,5,6,7],[3,2,1,4,5,6])




# """
# First Solution
# """
# import collections
# d = collections.defaultdict(int)

# def finder2(arr1, arr2):
#     for num in arr2:
#         d[num] += 1
#     for num in arr1:
#         if d[num] == 0:
#             return num
#         else:
#             d[num] -= 1

# finder2([1,2,3,4,5,6,7],[3,2,1,4,5,6])



# """
# Second Solution
# Fill out your solution below:
# """

# def finder3(arr1,arr2):
#     num = 0
#     for n in arr1:
#         num += n
#     for n in arr2:
#         num -= n
#     return num
#     pass

# arr1 = [1,2,3,4,5,6,7]
# arr2 = [3,7,2,1,4,6]
# finder3(arr1,arr2)

# arr1 = [5,5,7,7]
# arr2 = [5,7,7]
# finder3(arr1,arr2)




# """
# Third Solution
# """
# # Make use of XOR (^=) operator
# def finder4(arr1, arr2):
#     result = 0
#     print(arr1 + arr2)
#     for num in arr1 + arr2:
#         result ^= num
#     return result
# arr1 = [5,5,7,7]
# arr2 = [5,7,7]
# finder4(arr1,arr2)
