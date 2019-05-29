"""
Largest Continuous Sum
Problem
Given an array of integers (positive and negative) find the largest continuous sum.
"""

# Working try: O(N^2)
def max_cont_sum(arr):
    """
    Finds the largest continuous sum in a list.
    """
    if len(arr) == 2: 
        return max(arr) if sum(arr) < max(arr) else sum(arr)

    max_sum = arr[0]
    for i in range(len(arr)):
        summ = arr[i]
        for j in range(len(arr)-i-1):
            summ += arr[i + j + 1]
            if summ > max_sum:
                max_sum = summ
    return max_sum

# Driver programm
max_cont_sum([-2, -3, 4, -1, -2, 1, 5, -3])
max_cont_sum([1,2,-1,3,4,-1])
max_cont_sum([1,2,-1,3,4,10,10,-10,-1])
max_cont_sum([-1,1])



"""
Solution
Fill out your solution below:
"""

# def large_cont_sum(arr):
#     if len(arr) == 0:
#         return 0
    
#     max_num = sum = arr[0]# max=sum=arr[0] bug: TypeError: 'int' object is not callable. (Do not use the keyword!)
    
#     for n in arr[1:]:
#         sum = max(sum+n, n)
#         max_num = max(sum, max_num)
#     return max_num
#     pass

# large_cont_sum([-2, -3, 4, -1, -2, 1, 5, -3])
# large_cont_sum([1,2,-1,3,4,-1])
# large_cont_sum([1,2,-1,3,4,10,10,-10,-1])


# """
# Test Your Solution
# """
# from unittest import assert_equal
# class LargeContTest(object):
#     def test(self,sol):
#         assert_equal(sol([1,2,-1,3,4,-1]),9)
#         assert_equal(sol([1,2,-1,3,4,10,10,-10,-1]),29)
#         assert_equal(sol([-1,1]),1)
#         print ('ALL TEST CASES PASSED')
        
# #Run Test
# t = LargeContTest()
# t.test(max_cont_sum)