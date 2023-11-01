#queue using deque
from collections import deque
class queue:
    def __init__(self):
        self.list = []

    def add_element(self, data):
        self.list.append(data)

    def remove_elements(self):
        self.list.pop(0)
    def display(self):
        print(self.list)
queue1=queue()
queue1.add_element(3)
queue1.add_element(5)
queue1.add_element(7)
queue1.display()
print("-------")
queue1.remove_elements()
queue1.display()
