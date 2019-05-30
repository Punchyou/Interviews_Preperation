"""
String Compression
Problem
Given a string in the form 'AAAABBBBCCCCCDDEEEE' compress it to become 'A4B4C5D2E4'.
For this problem, you can falsely "compress" strings of single or double letters.
For instance, it is okay for 'AAB' to return 'A2B1' even though this technically
takes more space.

The function should also be case sensitive, so that a string 'AAAaaa' returns 'A3a3'.
"""


# Doesn't work if the same letter is repeated more than one times across the string.
from collections import defaultdict
class Compression():

    def __init__(self, uncomp_str):
        self.uncomp_str = uncomp_str
        self.counts_dict = defaultdict(int)


    def letter_counts(self):
        """
        Counts the occurances of the same letter in a string.
        """

        for i in self.uncomp_str:
            self.counts_dict[i] += 1
        
        return self.counts_dict
    
    def compr_str(self):
        """
        Compreses a string with repeating lettes.
        """

        counts_dict = self.letter_counts()
        compressed_str = ""

        for key, val in counts_dict.items():
            compressed_str += str(key) + str(val)
        
        return compressed_str

uncom_str = "AAAAAAVVVVVvvBBBBBBmmmmmmmmmm"
compression = Compression(uncom_str)
compression.compr_str()




# """
# Solution: The run length compression algorithm.
# """

# def compress(s):
#     r = ""
#     l = len(s)
    
#     if l==0:
#         return ''
#     if l==1:
#         return s+'1'
    
#     cnt = 1
#     i=1
    
#     while i<l:
#         if s[i]==s[i-1]:
#             cnt += 1
#         else:
#             r=r+s[i-1]+str(cnt)
#             cnt=1
#         i+=1
#     r = r+s[i-1]+str(cnt)
#     return r

# compress('AAAAABBBBCCCC')


# """
# RUN THIS CELL TO TEST YOUR SOLUTION
# """
# from nose.tools import assert_equal

# class TestCompress(object):

#     def test(self, sol):
#         assert_equal(sol(''), '')
#         assert_equal(sol('AABBCC'), 'A2B2C2')
#         assert_equal(sol('AAABCCDDDDD'), 'A3B1C2D5')
#         print ('ALL TEST CASES PASSED')

# # Run Tests
# t = TestCompress()
# t.test(compress)