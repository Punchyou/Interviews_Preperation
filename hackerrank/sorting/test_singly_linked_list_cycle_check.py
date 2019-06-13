"""
Singly Linked List Cycle Check
Problem

Given a singly linked list,
write a function which takes in the first node
in a singly linked list and returns a
boolean indicating if the linked list
contains a "cycle".

A cycle is when a node's next point
actually points back to a previous node
in the list. This is also sometimes
known as a circularly linked list.

"""

# My solution

class Node():

    def __init__(self, value):
        self.value = value
        self.nextnode = None

# create the nodes    
a = Node(1)
b = Node(2)
c = Node(3)

# link each node to the next
a.nextnode = b
b.nextnode = c
c.nextnode = a
linked_list = [a, b, c]


# test if its a cycle list
def is_cycle_list():
    for i in range(len(linked_list) - 1):
        return linked_list[-1].nextnode == linked_list[i]
is_cycle_list()



# """
# Solution 

# Will use two markers, fast and slow.
# Slow will move a node a time, fast two nodes at a time.
# if they are equal at some point, this means that
# there is a loop.
# """

# class Node():

#     def __init__(self, value):
#         self.value = value
#         self.nextnode = None

# a = Node(1)
# b = Node(2)
# c = Node(3)

# a.nextnode = b
# b.nextnode = c
# c.nextnode = a

# def is_cycle(node):
#     #     Use fast and slow pointer
#     fast, slow = node, node
#     while fast and fast.nextnode:
#         fast = fast.nextnode
#         if fast == slow:
#             return True
#         fast = fast.nextnode
#         slow = slow.nextnode
#     return False

# is_cycle(a)