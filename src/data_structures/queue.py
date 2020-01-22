class Queue:
    """
    Queue (data structure) is an ordered collection of items where items
    are added to the rear end, removed at the top end. FIFO.

    Attributes:
        items (int)
    """
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        """
        Return whether the queue is empty.
        """
        return self.items == []

    def enqueue(self, item):
        """
        Add specified item to the rear end of the queue.
        """
        self.items.insert(0, item)
    
    def dequeue(self):
        """
        Remove item located at the top end of the queue.
        """
        return self.items.pop()
    
    def size(self):
        """
        Return the size (as integer) of the queue.
        """
        return len(self.items)