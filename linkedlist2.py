class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
    def insert(self,newNode):
        if self.head is None:
            self.head= newNode
        else:
            lastnode=self.head
            while True:
                if lastnode.next is None:
                    break
                lastnode=lastnode.next
                lastnode.next=newNode

    def print_linked_list(head):
        current_node = head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

for i in range(4):
    node1=Node(input())
    linkedlist=Linkedlist()
    linkedlist.insert(node1)
linkedlist.print_linked_list()


# list=linkedList()
# list.addElements(10)
# list.addElements(20)
# list.addElements(30)
# list.addElements(23)

