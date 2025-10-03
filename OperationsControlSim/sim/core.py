from OperationsControlSim.Structures.queue import Queue
from OperationsControlSim.Structures.stack import Stack
from OperationsControlSim.Structures.linkedlist import LinkedList

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

event_queue = Queue()

class Event_queue:
    def add_event(event):
        event_queue.enqueue(event)

    def process_event():
        event = event_queue.dequeue()
