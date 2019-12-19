class Deque:
    """
    A deque (data structure) is an ordered collection of items where items
    are added and removed from either end (top or rear).

    Attributes:
        items (int)
    """
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        """
        Return whether the deque is empty.
        """
        return self.items == []

    def addFront(self, item):
        """
        add specified item to the top end of the deque.
        """
        self.items.append(item)

    def addRear(self, item):
        """
        Add specified item to the rear end of the deque.
        """
        self.items.insert(0, item)
    
    def removeFront(self):
        """
        Remove item located at the top end of the deque.
        """
        return self.items.pop()
    
    def removeRear(self):
        """
        Remove item located at the rear end of the deque.
        """
        return self.items.pop(0)
    
    def size(self):
        """
        Return the size (as integer) of the deque.
        """
        return len(self.items)