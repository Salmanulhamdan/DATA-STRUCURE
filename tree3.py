# Implement a binary search tree and search for a node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def search(root, val):
    if not root or root.val == val:
        return root
    if val < root.val:
        return search(root.left, val)
    else:
        return search(root.right, val)

root = Node(5)
root.left = Node(3)
root.right = Node(7)
root.left.left = Node(2)
root.left.right = Node(4)
root.right.left = Node(6)
root.right.right = Node(8)

print(search(root, 7).val)
print(search(root, 10))
