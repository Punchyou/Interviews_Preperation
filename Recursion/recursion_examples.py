# factorial

def factorial(n):
    """ Returns the factorial of an integer n. """

    # base case
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

"""
Recursion Homework Problems

Problem 1

Write a recursive function which takes an integer
and computes the cumulative sum of 0 to that integer

For example, if n=4 , return 4+3+2+1+0, which is 10.

This problem is very similar to the factorial problem
presented during the introduction to recursion. Remember,
always think of what the base case will look like.
In this case, we have a base case of n =0
(Note, you could have also designed the cut off to be 1).

In this case, we have: n + (n-1) + (n-2) + .... + 0
"""

def rec_sum(n):
    """ Returns the sum of the number between 0 and n."""

    #base case
    if n == 0:
        return 0
    else:
        return n + rec_sum(n-1)



"""

Problem 2

Given an integer, create a function which returns
the sum of all the individual digits in that integer.
For example: if n = 4321, return 4+3+2+1
"""

def rec_sum_of_digits(n):
    """ Returns the sum of digits of a number. """

    #base case
    if len(str(n)) == 1:
        return n
    else:
        return n % 10 + rec_sum_of_digits(n//10)


"""
Problem 3

Note, this is a more advanced problem than the previous two!
It aso has a lot of variation possibilities and
we're ignoring strict requirements here.

Create a function called word_split() which takes in a string phrase
and a set list_of_words. The function will then determine if it is
possible to split the string in a way in which words can be made
from the list of words. You can assume the phrase will only contain
words found in the dictionary if it is completely splittable.
"""


def rec_create_str_check(l, s):
    """ Returns true ifthe words in the list l can make the create s.
    Else, returns False."""

    for i in range(len(l)):
        if l[i] in s:
            s = s.replace(l[i], "")
    return s == ""

rec_create_str_check(["I", "am", "dog", "cat"], "Iamcat")


"""
Solution
"""
# def word_split(phrase,list_of_words, output = None):
#     '''
#     Note: This is a very "python-y" solution.
#     ''' 
    
#     # Checks to see if any output has been initiated.
#     # If you default output=[], it would be overwritten for every recursion!
#     if output is None:
#         output = []
    
#     # For every word in list
#     for word in list_of_words:
        
#         # If the current phrase begins with the word, we have a split point!
#         if phrase.startswith(word):
            
#             # Add the word to the output
#             output.append(word)
            
#             # Recursively call the split function on the remaining portion of the phrase--- phrase[len(word):]
#             # Remember to pass along the output and list of words
#             return word_split(phrase[len(word):],list_of_words,output)
    
#     # Finally return output if no phrase.startswith(word) returns True
#     return output

# word_split("Iamcat", ["I", "am", "dog", "cat"])

"""

Memoization

Memoization effectively refers to remembering
("memoization" -> "memorandum" -> to be remembered)
results of method calls based on the method inputs
and then returning the remembered result rather than
computing the result again. You can think of it as a cache
for method results. We'll use this in some of the interview
problems as improved versions of a purely recursive solution.

A simple example for computing factorials using memoization:
"""

# Create cache for known results
factorial_memo = {}

def fact(k):
    
    if k < 2: 
        return 1
    
    if not k in factorial_memo:
        factorial_memo[k] = k * factorial(k-1)
        
    return factorial_memo[k]



"""
We can also encapsulate the memoization process into a class.
"""

class Memoize:
    def __init__(self, f):
        self.f = f
        self.memo = {}
    def __call__(self, *args):
        if not args in self.memo:
            self.memo[args] = self.f(*args)
        return self.memo[args]

def fact2(k):
    
    if k < 2: 
        return 1
    
    return k * fact2(k - 1)

fact2 = Memoize(fact2)