# queue is a linear data structure that stores items in a First In First Out manner
class Queue:
    def __init__(self):
        self.items = []

    # Check if the queue is empty
    def is_empty(self):
        return len(self.items) == 0
    
    # Add an item to the end of the queue 
    def enqueue(self, item):
        self.items.append(item)
    
    # Remove and return the first item added to the queue
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items.pop(0)
    
    # Return the size
    def size(self):
        return len(self.items)
    
    # Return the first item in the queue without removing it
    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items[0]

#example:
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(f"the first item: {queue.peek()}") 
print(f"Removed item: {queue.dequeue()}")  
print(f"size of the queue: {queue.size()}")  
print(f"Is the queue empty? {queue.is_empty()}")  