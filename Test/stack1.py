'''
Dominic Wipf:
Simple stack to store command objects for the Operations Control Simulation
Implements a basic LIFO stack structure
'''
class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        #Push an item onto the stack.
        self._items.append(item)

    def pop(self):
        #Remove and return the most-recent item, or None if empty.
        if not self.is_empty():
            return self._items.pop()
        return None

    def peek(self):
        #Return the most-recent item without removing it, or None.
        if not self.is_empty():
            return self._items[-1]
        return None

    def is_empty(self):
        #Return True if the stack has no items.
        return len(self._items) == 0