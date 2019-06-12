"""
Implement a Queue - Using Two Stacks

Given the Stack class below, implement a Queue class using two stacks!
Note, this is a "classic" interview problem.
Use a Python list data structure as your Stack.

# Uses lists instead of your own Stack class.
stack1 = []
stack2 = []
"""


class Queue2Stacks(object):
    
    def __init__(self):        
        # Two Stacks
        self.stack1 = []
        self.stack2 = []
     
    def enqueue(self, element):
        """ Adds an element at the end of the stack."""
        self.stack1.append(element)

    def dequeue(self):
        """ Removes an elements from the front of a stack."""

        #stack 2 is the reversed stack 1
        i = len(self.stack1) -1
        while i >= 0:
            self.stack2.append(self.stack1[i])
            i -= 1

        #remove the last element of stack2
        # which is the first element of stack1
        self.stack2.pop()
        self.stack1 = self.stack2

        # reverse it so the item before the last removed becomes first
        self.stack1.reverse()


queue = Queue2Stacks()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
queue.dequeue()


# """
# Solution

# We have to implement double reverse
# """

# class Queue2Stacks2(object):
    
#     def __init__(self):
        
#         # Two Stacks
#         self.in_stack = []
#         self.out_stack = []
     
#     def enqueue(self, element):
#         self.in_stack.append(element)
#         pass
    
#     def dequeue(self):
        
#         # if oust_stacl empty
#         if not self.out_stack:
#             # while in_stack not empty
#             while self.in_stack:
#                 #append the last element of the in_stack into the out_stack
#                 #and you have the revereced stack1
#                 self.out_stack.append(self.in_stack.pop())
#         return self.out_stack.pop()

# myobj = Queue2Stacks2()

# for i in range(5):
#     myobj.enqueue(i)
    
# for i in range(5):
#     print (myobj.dequeue())
