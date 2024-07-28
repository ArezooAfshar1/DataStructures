# Doubly Linked List contains a data element and two links pointing to the next and previous node in the sequence.
class Node:
    def __init__(self, data):
        self.data = data
        self.Llink = None
        self.Rlink = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Inserts a new node at the beginning.
    def insert_at_the_beginning(self, data):
        new_node = Node(data)
        if self.head:
            new_node.Rlink = self.head
            self.head.Llink = new_node
        self.head = new_node
        return self.head

    # Inserts a new node at the specified index. 
    def insert_at_index(self, index, data):
        new_node = Node(data)
        current_node = self.head
        position = 0

        while current_node and position < index:
            current_node = current_node.Rlink
            position += 1

        if current_node is None:
            print("Index out of bounds")
            return

        new_node.Llink = current_node.Llink
        new_node.Rlink = current_node
        if current_node.Llink is not None:
            current_node.Llink.Rlink = new_node
        else:
            self.head = new_node
        current_node.Llink = new_node

    # Inserts a new node at the end. 
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node 
            return self.head
        
        current_node = self.head 
        while current_node.Rlink:
            current_node = current_node.Rlink
        
        current_node.Rlink = new_node
        new_node.Llink = current_node
        return self.head
    
    # Delete the first node from the beginning.
    def delete_at_beginning(self):
        if self.head is None:
            print("Empty doubly linked list")
            return None

        if self.head.Rlink is None:
            return None

        new_node = self.head.Rlink
        new_node.Llink = None
        del self.head
        self.head = new_node
        return self.head
    
    # Delete the node at a given index
    def delete_at_position(self, index):
        if self.head is None:
            print("Empty doubly linked list")
            return None
    
        if index < 0:
            print("Invalid index")
            return self.head
    
        if index == 0:
            if self.head.Rlink:
                self.head.Rlink.Llink = None
            self.head = self.head.Rlink
            return self.head
    
        current_node = self.head
        count = 0
        while current_node and count < index:
            current_node = current_node.Rlink
            count += 1
    
        if current_node is None:
            print("index out of range")
            return self.head
    
        if current_node.Rlink:
            current_node.Rlink.Llink = current_node.Llink
        if current_node.Llink:
            current_node.Llink.Rlink = current_node.Rlink
    
        del current_node
        return self.head
    
        
    # Delete the last node from the end 
    def delete_at_end(self):
        if self.head is None:
            print("Empty doubly linked list")
            return None

        if self.head.Rlink is None:
            return None

        current_node = self.head
        while current_node.Rlink.Rlink:
            current_node = current_node.Rlink

        last_node= current_node.Rlink
        current_node.Rlink = None
        del last_node
        return self.head

    # Returns the size.
    def size_of_doubly_linked_list(self):
        count = 0
        current_node = self.head
        while current_node:
            count += 1
            current_node = current_node.Rlink
        return count


    # Prints the list
    def print_as_list(self):
        result = []
        current_node = self.head
        while current_node:
            result.append(current_node.data)
            current_node = current_node.Rlink
        return result   

#example
DoublyLinkedList
dll = DoublyLinkedList()

# Insert nodes at the beginning
dll.insert_at_the_beginning(1)
dll.insert_at_the_beginning(2)
dll.insert_at_the_beginning(3)
print("Doubly Linked List:", dll.print_as_list())
# Insert nodes at the end
dll.insert_at_end(4)
dll.insert_at_end(5)
print("Doubly Linked List:", dll.print_as_list())
# Insert a node at a specific index
dll.insert_at_index(2, 6)

# Print the doubly linked list
print("Doubly Linked List:", dll.print_as_list())

# Delete a node at a specific position
dll.delete_at_position(2)

# Delete the first node
dll.delete_at_beginning()
print("Doubly Linked List:", dll.print_as_list())
# Delete the last node
dll.delete_at_end()

# Print the updated doubly linked list
print("Updated Doubly Linked List:", dll.print_as_list())

# Check the size of the doubly linked list
print("Size of the Doubly Linked List:", dll.size_of_doubly_linked_list())
