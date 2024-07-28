# A Linked list in which the first element points to the last element and the last element points to the first element
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    # Inserts a new node at the end of the circular linked list.
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head  # Pointing to itself
        else:
            current_node = self.head
            while current_node.next != self.head:
                current_node = current_node.next
            current_node.next = new_node
            new_node.next = self.head  # Making it circular

    # Removes the first node from the circular linked list.
    def remove_first_node(self):
        if self.head is None:
            return
        if self.head.next == self.head:  # Only one node
            self.head = None
            return
        
        current_node = self.head
        while current_node.next != self.head:
            current_node = current_node.next
        current_node.next = self.head.next
        self.head = self.head.next

    # Prints the list
    def print_as_list(self):
        result = []
        if self.head is None:
            return result
        
        current_node = self.head
        while True:
            result.append(current_node.data)
            current_node = current_node.next
            if current_node == self.head:
                break
        return result

    # Returns the size of the circular linked list.
    def size_of_circular_linked_list(self):
        if self.head is None:
            return 0
        
        count = 0
        current_node = self.head
        while True:
            count += 1
            current_node = current_node.next
            if current_node == self.head:
                break
        return count

    # Removes the node with the specified data value from the circular linked list.
    def remove_node(self, data):
        if self.head is None:
            return
        
        current_node = self.head
        previous_node = None
        
        while True:
            if current_node.data == data:
                if previous_node is None:  # Removing head
                    self.remove_first_node()
                else:
                    previous_node.next = current_node.next
                return
            previous_node = current_node
            current_node = current_node.next
            if current_node == self.head:
                break
        print("Node with data not found.")

# Example:

circular_list = CircularLinkedList()
circular_list.insert_at_end(1)
circular_list.insert_at_end(2)
circular_list.insert_at_end(3)

print(circular_list.print_as_list()) 
print(circular_list.size_of_circular_linked_list()) 

circular_list.remove_first_node()
print(circular_list.print_as_list()) 

circular_list.remove_node(3)
print(circular_list.print_as_list())  