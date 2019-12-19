class BinaryTree:
    """
    A tree (data structure)  consists of a set of nodes and a set of edjes 
    that connect pairs of nodes. A tree has the following properties:

     * One node of the tree is designated as the root node.

     * Every node n, except the root node, is connected by an edge from exactly
       one other node p, where p is the parent of n.

     * A unique path traverses from the root node to each node.

     * If each node in the tree has a maximum of two children, we say that the
       tree is a binary tree.
    """

    def __init__(self, rootObject):
        self.key = rootObject
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.left = self.leftChild
            self.leftChild = t
    
    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.left = self.rightChild
            self.rightChild = t
    
    def getLeftChild(self):
        return self.leftChild
    
    def getRightChild(self):
        return self.rightChild
    
    def setRootVal(self, obj):
        self.key = obj
    
    def getRootVal(self):
        return self.key