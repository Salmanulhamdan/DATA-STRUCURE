class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        new_node = Node(value)
        if self.tail.isEmpty():
            self.tail.next = new_node
        else:
            self.head = new_node
        self.tail = new_node

    def dequeue(self):
        if not self.head:
            return None
        value = self.head.value
        self.head = self.head.next
        if not self.head:
            self.tail = None
        return value

    def peek(self):
        if self.head is None:
            return None
        return self.head.data



