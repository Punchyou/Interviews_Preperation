# -*- coding: utf-8 -*-
"""
Created on Wed May 22 19:54:59 2019

@author: Maria
"""

"""
Creating a dynamic array.
"""
import ctypes

class DynamicArray(object):
    
    def __init__(self):
        """ Initialize the attributes."""
        self.n = 0
        self.capacity = 1
        self.A = self.make_array(self.capacity)
    
    def __len__(self):
        """ Returns number of elements stored in the array."""
        return self.n
    
    def __getitem__(self, k):
        """ Return the elemnt at index k."""
        
        if not 0 <= k <self.n:
            return IndexError('K is out of bounds!')
        
        return self.A[k]
    
    def append(self, ele):
        """ Add an element to the end of the array."""
        
        if self.n == self.capacity:
            self._resize(2*self.capacity) # 2x if capacity isn't enough
        
        self.A[self.n] = ele
        self.n +=1
    
    
    def _resize(self, new_cap):
        """ Resizes the capasity of the array."""
        
        B = self.make_array(new_cap) #New bigger array
        
        for k in range(self.n):
            B[k] = self.A[k] # Referenceing the existing values of A
            
            self.A = B #call A the B
            self.capacity = new_cap #reset the capacity
    
    def make_array(self, new_cap):
        """ Returns an array with a new capacity."""
        
        return(new_cap * ctypes.py_object)()