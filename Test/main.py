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

    linked_list = LinkedList()
    linked_list.append(10)
    linked_list.append(20)
    linked_list.append(30)
    linked_list.append(40)
    linked_list.insert_after_node(linked_list.head, 15)
    linked_list.insert_after_node(linked_list.head.next, 50)
    linked_list.insert_after_node(linked_list.head.next.next.next.next.next, 55)
    linked_list.append(5)
    linked_list.remove_first_with_id(30)
    print(linked_list.find(40))
    
    linked_list.print_list()

if __name__ == "__main__":
    main()
