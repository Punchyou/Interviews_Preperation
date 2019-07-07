"""

Binary Heap Operations

The basic operations we will implement for our
binary heap are as follows:

    BinaryHeap() creates a new, empty, binary heap.
    insert(k) adds a new item to the heap.
    findMin() returns the item with the minimum
    key value, leaving item in the heap.
    delMin() returns the item with the minimum
    key value, removing the item from the heap.
    isEmpty() returns true if the heap is empty,
    false otherwise.
    size() returns the number of items in the heap.
    buildHeap(list) builds a new heap from a list
    of keys.

"""

class BinaryHeap():
    def __init__(self):
        # we initialize the first elements to 0
        # otherwise we won't be able to find the children
        # of the first parent (heapList[1])
        self.heapList = [0]
        self.currentSize = 0

    def percUp(self, i):
        """ Retains the priority in the heap."""
        # while parent
        while i // 2 > 0:
            # if element < its parent then swap
            if self.heapList[i] < self.heapList[i // 2]:
                self.heapList[i // 2], self.heapList[i] = \
                self.heapList[i], self.heapList[i // 2]
                
            i = i // 2

    def insert(self, k):
        """ Inserts elements to the heap."""
        self.heapList.append(k)
        self.currentSize += 1
        self.percUp(self.currentSize)

    def percDown(self, i):
        """ Swaps the element in the i position 
        with the smallest child."""
        # while child
        while (i * 2) <= self.currentSize:
            # min child
            mc = self.minChild(i)
            # if element > min child then swap them
            if self.heapList[i] > self.heapList[mc]:
                self.heapList[i], self.heapList[mc] = \
                self.heapList[mc], self.heapList[i]

    def minChild(self, i):
        """ Returns the index of the smallest child."""
        # if right or left child > element
        if i * 2 + 1 > self.currentSize:
            return i * 2
        elif self.heapList[i*2] < self.heapList[i * 2 + 1]:
            return i * 2
        else:
            return i * 2 + 1

    def delMin(self):
        """ Deletes the minimum element."""
        # heapList[1] is the root node, the minimum value
        return_val = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize -= 1
        self.heapList.pop()
        self.percDown(1)
        return return_val
    
    def buildHeap(self, a_list):
        """ Creates an entile list and then builds a heap."""
        i = len(a_list) // 2
        self.currentSize = len(a_list)
        self.heapList = [0] + a_list[:]
        while (i > 0):
            self.percDown(i)
            i -= 1

    
