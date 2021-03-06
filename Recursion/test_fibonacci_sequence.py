"""
Problem Statement

Implement a Fibonnaci Sequence in three different ways:

    Recursively
    Dynamically (Using Memoization to store results)
    Iteratively

Function Output

Your function will accept a number n and return the nth number of the
fibonacci sequence

Remember that a fibonacci sequence: 0,1,1,2,3,5,8,13,21,... starts off with
a base case checking to see if n = 0 or 1, then it returns 1.

Else it returns fib(n-1)+fib(n+2).

# more ways in https://technobeans.com/2012/04/16/5-ways-of-fibonacci-in-python/

"""

# my solution

# Recursively
def fibo(n):
    """ Returns the nth term of the Fibonacci sequence."""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

fibo(8)

"""
Solution
Recursively

The recursive solution is exponential time Big-O ,
with O(2^n). However, its a very simple and basic
implementation to consider:
"""
def fib_rec(n):
    
    # Base Case
    if n == 0 or n == 1:
        return n
    
    # Recursion
    else:
        return fib_rec(n-1) + fib_rec(n-2)


"""
Dynamically

In the form it is implemented here, the cache is
set beforehand and is based on the desired n number
of the Fibonacci Sequence. Note how we check it the
cache[n] != None, meaning we have a check to know wether
or not to keep setting the cache (and more importantly
keep cache of old results!)
"""

# Instantiate Cache information
n = 10
cache = [None] * (n + 1)

def fib_dyn(n):
    
    # Base Case
    if n == 0 or n == 1:
        return n
    
    # Check cache
    if cache[n] != None:
        return cache[n]
    
    # Keep setting cache
    cache[n] = fib_dyn(n-1) + fib_dyn(n-2)
    
    return cache[n]



"""
Iteratively

In this solution we can take advantage of Python's tuple unpacking!
"""

def fib_iter(n):
    
    # Set starting point
    a, b = 0, 1
    
    # Follow algorithm
    for _ in range(n):
        a, b = b, a + b
        
    return a

fib_iter(10)


