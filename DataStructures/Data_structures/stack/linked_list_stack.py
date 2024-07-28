# Linked list stack provides dynamic memory management
# for efficient push and pop operations. each node contains a value and a pointer to the next node
# without a fixed size limitation

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
        self.count = 0

    def is_empty(self):
        return self.head is None

    # Adds an item to the top of the stack
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.count += 1

    # Removes the top item from the stack
    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty!")
        popped_node = self.head
        self.head = self.head.next
        self.count -= 1
        return popped_node.data

    # Returns the top item 
    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty!")
        return self.head.data

    # Returns the size of stack
    def size(self):
        return self.count

    # Prints all items in the stack
    def display(self):
        current = self.head
        if self.is_empty():
            return "Stack is empty"
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print('null')


# example:

MyStack = Stack()
# add items to stack
MyStack.push(11)
MyStack.push(22)
MyStack.push(33)
MyStack.push(44)

# Display stack elements
MyStack.display()

print(f'Top item is: {MyStack.peek()}')
print(f'popped item: {MyStack.pop()}')
MyStack.display()
print(f"Size of stack: {MyStack.size()}")
