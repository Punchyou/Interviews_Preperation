"""
Tree implementation with OOP
"""

class BinaryTree(object):

    def __init__(self, rootObj):
        """ Initialized the attributes of the class."""
        # init the root
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild == None:
        # no left child - add a tree as a child
            self.leftChild = BinaryTree(newNode)
        else:
            # push the existing child down one level
            # on the tree
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t
    
    def insertRight(self, newNode):
        if self.rightChild == None:
        # no left child - add a tree as a child
            self.rightChild = BinaryTree(newNode)
        else:
            # push the existing child down one level
            # on the tree
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t
    
    def getRightChild(self):
        return self.rightChild
    
    def getLeftChild(self):
        return self.leftChild
     
    def setRootVal(self, obj):
        self.key = obj
    
    def getRootVal(self):
        return self.key

r = BinaryTree("a")
r.insertLeft("b")
r.insertRight("c")
r.getLeftChild().getRootVal()
r.getRightChild().getRootVal()
