"""
Doubly Linked List Implementation

Each note has a reference for the next
and the previous node.
"""
class DoubleLinkedListNode():

    def __init__(self, value):
        self.value = value
        self.nextnode = None
        self.prevnode = None
    
a = DoubleLinkedListNode(1)
b = DoubleLinkedListNode(2)
c = DoubleLinkedListNode(3)

a.nextnode = b
b.prevnode = a

b.nextnode = c
c.prevnode = b