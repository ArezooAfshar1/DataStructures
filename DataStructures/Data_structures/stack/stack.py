# stack is a data structure that follows the Last In, First Out principle.

class Stack:
    # Initializes an empty list to store stack items.
    def __init__(self):
        self.items = []

    # Checks if the stack is empty
    def is_empty(self):
        return len(self.items) == 0

    # Adds an item to the top of the stack
    def push(self, item):
        self.items.append(item)
        print(f" Pushed: {item}")

    # Removes and returns the top item from the stack
    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty!")

        popped_item = self.items.pop()
        print(f"Popped: {popped_item}")
        return popped_item

    # Returns the top item 
    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty!")
        top_item = self.items[-1]
        print(f"Top item: {top_item}")
        return top_item

    # Returns the current number of items in the stack
    def size(self):
        size = len(self.items)
        print(f"stack size: {size}")
        return size

    # Prints all items currently in the stack.
    def display(self):
        print("Stack elements:", self.items)


# Example:
stack = Stack()

# Pushing items onto the stack
stack.push(1)
stack.push(2)
stack.push(3)

# Display the current stack contents
stack.display()

# View the top item of the stack without removing it
stack.peek()

# Remove the top item from the stack
stack.pop()

# Get the current size of the stack
stack.size()

stack.display()