class Stack:
    """
    Stack (data structure) is an ordered collection of items where items
    are added to and removed from the same end (known as top). LIFO.

    Attributes:
        items (int)
    """

    def __init__(self):
        self.items = []

    def isEmpty(self):
        """
        Return whether the stack is empty.
        """
        return self.items == []
    
    def push(self, item):
        """
        Add specified item to the top of the stack.
        """
        self.items.append(item)
    
    def pop(self):
        """
        Remove item from the top of the stack.
        """
        return self.items.pop()
    
    def peek(self):
        """
        Return item located at the top of the stack.
        """
        return self.items[len(self.items) - 1]
    
    def size(self):
        """
        Return the size (as integer) of the stack.
        """
        return len(self.items)