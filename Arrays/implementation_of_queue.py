"""
Implementation of a Queue.
FIFO concept.
"""

class Queue(object):

    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        """ Tests to see whether the queue is empty."""
        return self.items == []
    
    def enqueue(self, item):
        """ Adds a new item to the rear of the queue."""
        self.items.insert(0, item)
    
    def dequeue(self):
        """ Removes the front item from the queue."""
        self.items.pop()
    
    def size(self):
        """ Returns the number of items in the queue."""
        return len(self.items)


queue = Queue()
queue.isEmpty()
queue.enqueue(7)
queue.items