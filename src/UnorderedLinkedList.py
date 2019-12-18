class Node:
    """
    Building block for the implementation of a linked list.
    """
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def getData(self):
        return self.data
    
    def getNext(self):
        return self.next
    
    def setData(self, newData):
        self.data = newData
    
    def setNext(self, newNext):
        self.next = newNext

class UnorderedLinkedList:
    """
    An unordered linked list is a collection of items where each item
    holds a relative position with respect to others.
    """

    def __init__(self):
        self.head = None
    
    def isEmpty(self):
        return self.head == None
    
    def add(self, item):
