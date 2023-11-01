class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        self.head = None

    def insert(self, newNode):
        if self.head is None:
            self.head = ListNode(self.val)
        else:
            lastnode = self.head
            while True:
                if lastnode.next is None:
                    break
                lastnode = lastnode.next
                lastnode.next = newNode
class sol:
    def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        curr = dummy

        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next

        if l1:
            curr.next = l1
        else:
            curr.next = l2

        return dummy.next
l1=ListNode()
l1.insert(1)
l1.insert(2)
l1.insert(3)
l2=ListNode()
l2.insert(1)
l2.insert(3)
l2.insert(4)
s=sol()
s.mergeTwoLists(l1.val,l2.val)
print(s)