class Node: # Need this for the list
    def __init__(id, desc):
        id.desc = desc
        id.next = None


class LinkedList: # This is where the orders will be held after the fact

    def __init__(self):
       self.head = None

    def append(self, desc): #add to back ; verified work
        new_node = Node(desc)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def remove_first_with_id(self, key): #removes the first node in the chain that has the id that is entered ; verified work 
        temp = self.head
        if temp is not None:
            if temp.desc == key:
                self.head = temp.next
                temp = None
                return
        prev = None
        while temp is not None:
            if temp.desc == key:
                break
            prev = temp
            temp = temp.next
        if temp is None:
            print(f"{key} not found in the list.")
            return
        prev.next = temp.next
        temp = None 

    def find(self, key): # This will find a an id and return the first one it finds ; verified work
        temp = self.head
        if temp is not None:
            if temp.desc == key:
                return temp.desc
        while temp is not None:
            if temp.desc == key:
                return temp.desc
            prev = temp
            temp = temp.next
        if temp is None:
            print(f"{key} not found in the list.")
            return 

    
    def insert_after_node(self, prev_node, new_data): # This will insert a new node after node given ; verified work
        if prev_node is None:
            print("The given previous node must be in the list.")
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def print_list(self): # this is just for testing purposes
        temp = self.head
        while temp:
           print(temp.desc, end=" -> ")
           temp = temp.next
        print("None")
    
    def iter(self): # This is incomplete


        pass


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
#linked_list.iter()

