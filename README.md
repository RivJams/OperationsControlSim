Operations Control Simulator
  Goals
    Simulate a airport getting changes that are then kept up with on three data structures.
  Pieces
    Stack: This holds what the last action taken was, and allows for it to be undone.
    Queue: This holds all the active events and news, so that the can be handled by FIFO.
    LinkedList: This holds all the completed actions, and allows for removal of them.
    TestEnv: This will test the other pieces.
    Core: This will house the other pieces aside from TestEnv
  Workers
    River
    Dominic
    Chad
