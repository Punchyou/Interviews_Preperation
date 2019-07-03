"""
Implementation of a tree as list of lists.
r[0] is the root
r[1] is the left child as a list
r[2] is the right child as a list
"""

# build the binary tree
def BinaryTree(r):
    return [r, [], []]

# inserting a left child
def insertLeft(root, newBranch):
    # pop the left branch
    t = root.pop(1)

    if len(t) > 1:
        root.insert(1, [newBranch, t, []])

    else:
        root.insert(1, [newBranch, [], []])

    return root

def insertRight(root, newBranch):
    """ Inserts the right branch."""
    # pop the left branch
    t = root.pop(2)

    if len(t) > 1:
        root.insert(2, [newBranch, [], t])

    else:
        root.insert(2, [newBranch, [], []])

    return root

def getRootValue(root):
    """ Returns the valus of the root."""
    return root[0]

def setRootValue(root, newVal):
    """ Sets a new value to the root."""
    root[0] = newVal

def getLeftChild(root):
    """ Returns the left chils of the tree."""
    return root[1]

def getRightChild(root):
    """ Returns the left chils of the tree."""
    return root[2]

