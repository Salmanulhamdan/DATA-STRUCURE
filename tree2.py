#Implement a tree data structure and find the height of the tree.
class Node:
    def __init__(self, val):
        self.val = val
        self.children = []

def height(root):
    if not root:
        return 0
    max_height = 0
    for child in root.children:
        max_height = max(max_height, height(child))
    return max_height + 1

root = Node(1)
root.children = [Node(2), Node(3), Node(4)]
root.children[0].children = [Node(5), Node(6)]
root.children[2].children = [Node(7), Node(8), Node(9)]
root.children[0].children[1].children = [Node(10)]

print(height(root))
