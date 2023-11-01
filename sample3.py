class Node:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None


class bst:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
            return
        current = self.root
        while True:
            if data < current.data:
                if current.left is None:
                    current.left = Node(data)
                    break
                current = current.left
            else:
                if current.right is None:
                    current.right = Node(data)
                    break
                current = current.right

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data)
            self.inorder(root.right)
    def isbst(self,node,last_visited):
        if node is None:
            return True
        if not self.isbst(node.left,last_visited):
            return False
        if last_visited is not None and node.data<=last_visited.data:
            return False
        last_visited=node
        return self.isbst(node.right,last_visited)


bst1 = bst()
bst1.insert(9)
bst1.insert(5)
bst1.insert(4)
bst1.insert(3)
bst1.insert(6)
bst1.inorder(bst1.root)
if bst1.isbst(bst1.root,None):
    print("it is a bst")
else:
    print("not a bst")