"""
Implementation of a Deque.
Create a Deque structure
"""

class Deque(object):

    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        """ Tests to see whether the deque is empty. """
        return self.items == []
    
    def addFront(self, item):
        """ Adds a new item to the front of the deque."""
        self.items.append(item)
    
    def addRear(self, item):
        """ Adds a new item to the rear of the deque."""
        self.items.insert(0, item)
    
    def removeFront(self):
        """ Removes the front item from the deque."""
        return self.items.pop()

    def removeRear(self):
        """ Removes the rear item from the deque."""
        self.items.pop(0)
    
    def size(self):
        """ Returns the number of items in the deque."""
        return len(self.items)
    
dequeue = Deque()
dequeue.isEmpty()
dequeue.addFront(5)
dequeue.items