class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.head is None:
            return None
        popped_node = self.head
        self.head = self.head.next
        popped_node.next = None
        return popped_node.data

    def peek(self):
        if self.head is None:
            return None
        return self.head.data

    def is_empty(self):
        return self.head is None
stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)

print(stack.peek())  # prints 3

stack.pop()

print(stack.peek())  # prints 2

print(stack.is_empty())  # prints False
