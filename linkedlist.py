class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def array_to_linked_list(arr):
    head = Node(arr[0])
    current_node = head
    for i in range(1, len(arr)):
        new_node = Node(arr[i])
        current_node.next = new_node
        current_node = new_node
    return head
def print_linked_list(head):
    current_node = head
    while current_node:
        print(current_node.data, end=" -> ")
        current_node = current_node.next
    print("None")
arr = [1, 2, 3, 4, 5]
head = array_to_linked_list(arr)
print_linked_list(head)

# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class Linkedlist:
#     def __init__(self):
#         self.head=None
#     def insert(self,newNode):
#         if self.head is None:
#             self.head= newNode
#         else:
#             lastnode=self.head
#             while True:
#                 if lastnode.next is None:
#                     break
#                 lastnode=lastnode.next
#                 lastnode.next=newNode
#
# for i in range(4):
#     node1=Node(input())
#     linkedlist=Linkedlist()
#     linkedlist.insert(node1)

