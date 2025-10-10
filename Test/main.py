from structures.queue1 import Queue 
from structures.linkedlist1 import LinkedList
from structures.stack1 import Stack

def main():

    event_queue = Queue()
    undo_stack = Stack()
    event_log = LinkedList()

    # Test Queue adding operations
    print("Testing Queue Operations")

    event1 = "(9:00) Chicago Flight Landing"
    event2 = "(9:30) New York Flight Departing"
    event3 = "(9:45) Boston Flight Gate Change to A15"

    # Enqueue events and push to undo stack
    event_queue.enqueue(event1)
    undo_stack.push("ADD", event1)

    event_queue.enqueue(event2)
    undo_stack.push("ADD", event2)

    event_queue.enqueue(event3)
    undo_stack.push("ADD", event3)

    # Check to see the front of the queue
    print("Checking front of queue:")
    event_queue.peek()

    # Test Dequeue operations
    print("Processing events:")
    event_queue.dequeue()
    undo_stack.push("REMOVE", event1)
    event_log.append(event1)

    event_queue.dequeue()
    undo_stack.push("REMOVE", event2)
    event_log.append(event2)

    stackTest = Stack()

if __name__ == "__main__":
    main()
