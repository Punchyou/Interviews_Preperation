"""

Anagram Check
Problem
Given two strings, check to see if they are anagrams.
An anagram is when the two strings can be written using the exact
same letters (so you can just rearrange the letters to get
a different phrase or word).

For example:

"public relations" is an anagram of "crap built on lies."
"clint eastwood" is an anagram of "old west action"

Note: Ignore spaces and capitalization. So "d go" is an anagram
of "God" and "dog" and "o d g".

Fill out your solution below:

# 242. Valid Anagram(https://leetcode.com/problems/valid-anagram/description/)
"""

def anagram(s, s2):
    """
    Finds if a string is an anagram of another string.
    """
    def count_letters(s):
        """
        Creates dictionary about the occurances of letters
        occur in a string.
        """
        counts = {}
        for letter in s:
            if letter not in counts.keys():
                counts[letter] = 1
            else:
                counts[letter] += 1
        return counts

    s = s.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()

    # create two dictionaries of occurances of letters in the string
    counts_s = count_letters(s)
    counts_s2 = count_letters(s2)
    if len(s) != len(s2):
        return False

    # compare dicts
    return counts_s == counts_s2

# Driver programm
anagram('clint eastwood','old west action')










# 
# def anagram(s, t):
#     """
    
#     :type s: str
#     :type t: str
#     :rtype: bool
#     """
#     s=s.replace(' ','').lower()
#     t=t.replace(' ','').lower()
    
#     if(len(s)!=len(t)):
#         return False
#     counter = {}
#     for letter in s:
#         if letter in counter:
#             counter[letter] += 1
#         else:
#             counter[letter] = 1

#     for letter in t:
#         if letter in counter:
#             counter[letter] -= 1
#         else:
#             return False

#     for k in counter:
#         if counter[k]!=0:
#           return False
    
#     return True
#     pass
# anagram('dog','god')
# True
# anagram('clint eastwood','old west action')
# True
# anagram('aa','bb')


# """
# RUN THIS CELL TO TEST YOUR SOLUTION
# """
# from nose.tools import assert_equal

# class AnagramTest(object):
    
#     def test(self,sol):
#         assert_equal(sol('go go go','gggooo'),True)
#         assert_equal(sol('abc','cba'),True)
#         assert_equal(sol('hi man','hi     man'),True)
#         assert_equal(sol('aabbcc','aabbc'),False)
#         assert_equal(sol('123','1 2'),False)
#         print('ALL TEST CASES PASSED')

# # Run Tests
# t = AnagramTest()
# t.test(anagram)
# """