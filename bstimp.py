class Node:
    def __init__(self,value):
        self.left=None
        self.data=value
        self.right=None
class bst:
    def __init__(self):
        self.root=None
    def insert(self,data):
        new=Node(data)
        if self.root is None:
            self.root=new
            return

        current=self.root
        while True:
            if data< current.data:
                if current.left is None:
                    current.left=Node(data)
                    break
                else:
                    current=current.left
            else:
                if current.right is None:
                    current.right=Node(data)
                    break
                else:
                    current=current.right
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.data)
            self.inorder(root.right)

    def validate_bst(self,node, last_visited):
        if node is None:
            return True

        if not self.validate_bst(node.left, last_visited):
            return False

        if last_visited is not None and node.data <= last_visited.data:
            return False

        last_visited = node

        return self.validate_bst(node.right, last_visited)
tree=bst()
tree.insert(6)
tree.insert(3)
tree.insert(9)
tree.insert(2)
tree.insert(8)
tree.inorder(tree.root)

if tree.validate_bst(tree.root,None):
    print("t")
else:
    print("n")
