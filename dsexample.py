class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            curr_node = self.head
            while curr_node.next:
                curr_node = curr_node.next
            curr_node.next = new_node

    def array_to_linked_list(self, arr):
        linked_list = LinkedList()
        for item in arr:
            linked_list.add_node(item)
        print(linked_list)


arr = [1, 2, 3, 45, 9]
a1 = LinkedList()
a1.array_to_linked_list(arr)
