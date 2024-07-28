#A simple linked list is a collection of nodes that are linked with each other. 
#A node contains two things first is data and second is a link that connects it with another node

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Inserts a new node at the beginning of the linked list.
    def insert_at_the_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return 
        else:
            new_node.next = self.head
            self.head = new_node

    # Inserts a new node at the specified index in the linked list.
    def insert_at_index(self, data, index):
        new_node = Node(data)
        if index ==0:
            new_node.next = self.head
            self.head = new_node
            return
        current_node = self.head
        count = 0
        while current_node and count < index -1:
            current_node = current_node.next
            count +=1
        if current_node is None:
            print("Index out of bounds")
            return
        new_node.next = current_node.next
        current_node.next = new_node

    # Inserts a new node at the end of the linked list.    
    def insert_at_the_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return 
        current_node = self.head 
        while (current_node.next):
            current_node = current_node.next
        current_node.next = new_node

    # Removes the first node from the linked list.
    def remove_first_node(self):
        if(self.head == None):
            return

        self.head = self.head.next

    # Removes the last node from the linked list.
    def remove_last_node(self):

        if self.head is None:
            return

        current_node = self.head
        while(current_node.next.next):
            current_node = current_node.next

        current_node.next = None

    # Removes the node at the specified index from the linked list.
    def remove_at_index(self, index):
        if self.head == None:
            return

        current_node = self.head
        position = 0
        if position == index:
            self.remove_first_node()
        else:
            while(current_node != None and position+1 != index):
                position = position+1
                current_node = current_node.next

            if current_node != None:
                current_node.next = current_node.next.next
            else:
                print("Index out of bounds")

    # Removes the node with the specified data value from the linked list.
    def remove_node(self, data):
        current_node = self.head

        if current_node.data == data:
            self.remove_first_node()
            return

        while(current_node != None and current_node.next.data != data):
            current_node = current_node.next

        if current_node == None:
            return
        else:
            current_node.next = current_node.next.next

    # Returns the size of the linked list.
    def size_of_linked_list(self):
        size = 0
        if(self.head):
            current_node = self.head
            while(current_node):
                size = size+1
                current_node = current_node.next
            return size
        else:
            return 0
        
    # Prints the list
    def print_as_list(self):
        result = []
        current_node = self.head
        while current_node:
            result.append(current_node.data)
            current_node = current_node.next
        return result    
        
#example:
linked_list = LinkedList()

# Insert nodes 
linked_list.insert_at_the_beginning(5)
linked_list.insert_at_the_beginning(10)
linked_list.insert_at_the_beginning(15)
linked_list.insert_at_index(100, 3)
linked_list.insert_at_the_end(50)

# Print the size of the linked list
print(linked_list.size_of_linked_list())

# print list 
print(linked_list.print_as_list())

# Removing elements
linked_list.remove_at_index(1)
linked_list.remove_last_node()
linked_list.remove_first_node()

print(linked_list.print_as_list())
