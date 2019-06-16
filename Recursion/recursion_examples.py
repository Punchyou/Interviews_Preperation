# factorial

def factorial(n):
    """ Returns the factorial of an integer n. """

    # base case
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

