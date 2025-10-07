from structures.queue1 import Queue 
from structures.linkedlist1 import LinkedList
from structures.stack1 import Stack

def main():

    # Test Queue operations
    queueTest = Queue()
    queueTest.enqueue(1)
    queueTest.enqueue(2)

    stackTest = Stack()
    lltest = LinkedList()
    queueTest.dequeue()
    queueTest.dequeue()
    queueTest.is_empty()

if __name__ == "__main__":
    main()
