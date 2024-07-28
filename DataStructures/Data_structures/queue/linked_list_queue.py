class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.front = None  
        self.rear = None   
        self.size = 0      

    # Check if the queue is empty
    def is_empty(self):
        return self.size == 0
    
    # Add an item to the end of the queue 
    def enqueue(self, value):
        new_node = Node(value)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1
    
    # Remove and return the first item added to the queue
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        removed_value = self.front.value
        self.front = self.front.next
        if self.front is None:  
            self.rear = None
        self.size -= 1
        return removed_value
    
    # Return the size
    def get_size(self):
        return self.size
    
    # Return the first item in the queue without removing it
    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.front.value

# Example usage:
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(f"The first item: {queue.peek()}")  
print(f"Removed item: {queue.dequeue()}")  
print(f"Size of the queue: {queue.get_size()}") 
print(f"Is the queue empty? {queue.is_empty()}")   
