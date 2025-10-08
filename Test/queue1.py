'''
River Wallerstedt
Simple Queue to manage events for the Operations Control Simulation
Implements a basic FIFO queue structure
'''
class Queue:
    def __init__(self):
        self.events = []

    def enqueue(self, event):
        self.events.append(event)
        print(f"Enqueued event: {event}")

    def dequeue(self):
        if not self.is_empty():
            print(f"Dequeued event: {self.events[0]}")
            return self.events.pop(0)
        return None
    
    def peek(self):
        if not self.is_empty():
            print(f"Next event: {self.events[0]}")
            return self.events[0]
        return None
    
    def is_empty(self):
        return len(self.events) == 0