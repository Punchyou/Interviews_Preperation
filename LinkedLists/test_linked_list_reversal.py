"""
Write a function to reverse a Linked List in place.
The function will take in the head of the list as
input and return the new head of the list.
"""

class Node():

    def __init__(self, value):
        self.value = value
        self.nextnode = None
    

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.nextnode = b
b.nextnode = c
c.nextnode = d
d.nextnode = e


#My solution - doen't reverse the linked list, it just

def linked_list_last_el(node):
    """ Returns the last element of a linked list. """
    
    marker = node.nextnode
    while marker:
        marker = marker.nextnode
    
    return marker.value


linked_list_last_el(a)



"""

Solution

Since we want to do this in place we want to make the funciton operate in O(1) space, meaning we don't want to create a new list, so we will simply use the current nodes! Time wise, we can perform the reversal in O(n) time.

We can reverse the list by changing the next pointer of each node. Each node's next pointer should point to the previous node.

In one pass from head to tail of our input list, we will point each node's next pointer to the previous element.

Make sure to copy current.next_node into next_node before setting current.next_node to previous. Let's see this solution coded out:

"""

# def reverse(head):
    
#     # Set up current,previous, and next nodes
#     current = head
#     previous = None
#     nextnode = None

#     # until we have gone through to the end of the list
#     while current:
        
#         # Make sure to copy the current nodes next node to a variable next_node
#         # Before overwriting as the previous node for reversal
#         nextnode = current.nextnode

#         # Reverse the pointer ot the next_node
#         current.nextnode = previous

#         # Go one forward in the list
#         previous = current
#         current = nextnode

#     return previous

