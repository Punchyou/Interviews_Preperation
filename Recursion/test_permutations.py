"""
String Permutation
Problem Statement

Given a string, write a function that uses recursion to
output a list of all the possible permutations of that string.

For example, given s='abc' the function should
return ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

Note: If a character is repeated, treat each occurence
as distinct, for example an input of 'xxx' would return
a list with 6 "versions" of 'xxx'
"""

# easy - with itertool.combinations

# hard code - retrieved from http://code.activestate.com/recipes/252178/

def str_permutations(s):
    """ Finds all the possible permutations of a string."""

    perms = []
    if len(s) <= 1:
        perms.append(s)
    else:
        for per in str_permutations(s[1:]):
            for i in range(len(s)):
                perms.append(per[:i] + s[0] + per[i:])
    return perms

print(str_permutations("pant"))



"""
Solution

Let's think about what the steps we need to take here are:

    1) Iterate through the initial string – e.g., ‘abc’.

    2) For each character in the initial string, set aside that character and get
    a list of all permutations of the string that’s left.

    3) So, for example, if the current iteration is on 'b',
    we’d want to find all the permutations of the string 'ac'.

    4) Once you have the list from step 2, add each element from that
    list to the character from the initial string, and append the result
    to our list of final results. So if we’re on 'b' and we’ve gotten the
    list ['ac', 'ca'], we’d add 'b' to those, resulting in 'bac' and 'bca',
    each of which we’d add to our final results.

    Return the list of final results.
"""


# def permute(s):
#     out = []
    
#     # Base Case
#     if len(s) == 1:
#         out = [s]
        
#     else:
#         # For every letter in string
#         for i, let in enumerate(s):
            
#             # For every permutation resulting from Step 2 and 3 described above
#             to_iter = permute(s[:i] + s[i+1:])
#             for perm in to_iter:
#                 # Add it to output
#                 out += [let + perm]

#     return out

# if __name__ == "__main__":
#     permute("mari")