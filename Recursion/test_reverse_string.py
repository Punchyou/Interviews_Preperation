"""
Reverse a String

This interview question requires you to reverse
a string using recursion.
Make sure to think of the base case here.

Again, make sure you use recursion to accomplish this.
Do not slice (e.g. string[::-1]) or use iteration,
there must be a recursive call for the function.
"""

#My solution

def reverse_str(s):
    """ Reverses a string with recursion. """
    print(s[-1])
    if len(s) > 1:
        return reverse_str(s[:-1])

reverse_str("maria")


# """
# Solution

# In order to reverse a string using recursion we need to consider what a base and recursive case would look like. Here we've set a base case to be when the length of the string we are passing through the function is length less than or equal to 1.

# During the recursive case we grab the first letter and add it on to the recursive call.
# """

# def reverse(s):
    
#     # Base Case
#     if len(s) <= 1:
#         return s

#     # Recursion
#     return reverse(s[1:]) + s[0]
