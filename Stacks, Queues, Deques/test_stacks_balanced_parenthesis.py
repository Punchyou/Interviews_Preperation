"""

Balanced Parentheses Check
Problem Statement

Given a string of opening and closing parentheses,
check whether it’s balanced. We have 3 types of parentheses:
round brackets: (), square brackets: [], and curly brackets: {}.
Assume that the string doesn’t contain any other character than these,
no spaces words or numbers. As a reminder, balanced parentheses require
every opening parenthesis to be closed in the reverse order opened.
For example ‘([])’ is balanced but ‘([)]’ is not.

You can assume the input string has no spaces.
"""


def is_balanced(par_str):
    """ Checks if the parenthesis in string are balanced."""

    left_par = "{[("
    right_par = "}])"

    if len(par_str) % 2 != 0:
        return False
    
    # prevents in index error
    if par_str[0] in right_par:
        return False
    
    while len(par_str) < 0:
        for ind, par in par_str:
            if par not in left_par and par[ind] == par[ind - 1]:
                par_str.pop(ind)
                par_str.pop(ind - 1)
                print(par_str)
                break
            else:
                return False
    return True

is_balanced("[][][()]{[([])]}")


# """
# Solution
# """

# def balance_check(s):

#     if len(s) % 2 != 0:
#         return False
    
#     opening = set('{[(')
#     #first match is (), second is [] and so on
#     matches = set([('(', ')'), ('[', ']'), ('{', '}')])

#     # use a list as a stack
#     stack = []

#     for paren in s:
          # keep track of the parenthesis in a stack
          # we want the last opening parenthesis to be closed first
#         if paren in opening:
#             stack.append(paren)
        
#         else:
#             # if the parenthesis is not an opening
#             # and there is no matching with an opening one
#             # the len of stack is 0

#            # check if the stack is empty
#            # because there is no associated with this closing one
#             if len(stack) == 0:
#                 return False

#             #check if the last oppened par is the corresponding closing match               
#             last_open = stack.pop()
#             if (last_open, paren) not in matches:
#                 return False


#     return len(stack) == 0