from structures.queue1 import Queue 
from structures.linkedlist1 import LinkedList
from structures.stack1 import Stack

def main():

    # Test Queue adding operations
    print("Testing Queue Operations")
    event_queue = Queue()
    event_queue.enqueue("(9:00) Chicago Flight Landing")
    event_queue.enqueue("(9:30) New York Flight Departing")
    event_queue.enqueue("(9:45) Boston Flight Gate Change to A15")

    # Check to see the front of the queue
    print("Checking front of queue:")
    event_queue.peek()

    # Test Dequeue operations
    print("Processing events:")
    event_queue.dequeue()
    event_queue.dequeue()

    stackTest = Stack()
    lltest = LinkedList()

if __name__ == "__main__":
    main()
