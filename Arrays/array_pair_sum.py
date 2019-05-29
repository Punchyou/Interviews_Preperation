"""
Array Pair Sum
Problem
Given an integer array, output all the unique pairs that sum up to a specific value k.

So the input:

pair_sum([1,3,2,2],4)

would return 2 pairs:

 (1,3)
 (2,2)

NOTE: FOR TESTING PURPOSES CHANGE YOUR FUNCTION SO IT OUTPUTS THE NUMBER OF PAIRS
"""


def pair_sum(ar, k):
    """
    Finds the unique pairs that sum up to a specific value.
    """

    for i, j in enumerate(ar):
        ar = ar[i:]
        for m, n in enumerate(ar):
            if i != m and j + n == k: # try it with one-line statement
                print([j, n])

pair_sum([1,3,2,2],4)




# """
# Solution
# Fill out your solution below:
# """

# #Use sets for keeping track and reduce O(N*N) to O(N)

# def pair_sum_sol(arr,k):
#     output = set()
#     lookup = set()
#     for num in arr:
#         if k-num not in lookup:
#             lookup.add(num)
#         else:
#             output.add((min(num, k-num), max(num, k-num)))
#     print("\n".join(map(str, list(output))))

# pair_sum_sol([1,3,2,2],4)


# #Test Your Solution
# """
# RUN THIS CELL TO TEST YOUR SOLUTION
# """
# from nose.tools import assert_equal

# class TestPair(object):
    
#     def test(self,sol):
#         assert_equal(sol([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10),6)
#         assert_equal(sol([1,2,3,1],3),1)
#         assert_equal(sol([1,3,2,2],4),2)
#         print('ALL TEST CASES PASSED')
        
# #Run tests
# t = TestPair()
# t.test(pair_sum)