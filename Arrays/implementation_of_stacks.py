"""
This is an implementation of a stack.
A class which describes how a stack is created.

The stack abstract data type is defined
by the following structure and operations.
A stack is structured, as described above,
as an ordered collection of items
where items are added to and removed
from the end called the “top.”
Stacks are ordered LIFO.
"""

class Stack(object):

    def __init__(self):
        self.items = []

    def isEmpty(self):
        """ Tests to see whether the stack is empty. """
        return self.items == []
    
    def push(self, item):
        """ Creates a new stack that is empty."""
        self.items.append(item)
    
    def pop(self):
        """ Removes the top item from the stack."""
        self.items.pop()

    def peek(self):
        """ Returns the top item from the stack."""
        return self.items[-1]
    
    def size(self):
        """ Returns the number of items on the stack."""
        return len(self.items)


stack = Stack()
stack.isEmpty()
stack.push(5)
stack.pop()
