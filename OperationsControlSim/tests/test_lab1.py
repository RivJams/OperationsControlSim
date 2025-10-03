from OperationsControlSim.sim.core import Event_queue

def main():

    # Test Queue operations
    queue = Event_queue()
    queue.enqueue(1)
    queue.enqueue(2)
    assert queue.dequeue() == 1
    assert queue.dequeue() == 2
    assert queue.is_empty()

if __name__ == "__main__":
    main()
