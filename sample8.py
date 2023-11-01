class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if not self.root:
            self.root = Node(val)
            return
        curr_node = self.root
        while curr_node:
            if val < curr_node.val:
                if not curr_node.left:
                    curr_node.left = Node(val)
                    break
                curr_node = curr_node.left
            else:
                if not curr_node.right:
                    curr_node.right = Node(val)
                    break
                curr_node = curr_node.right

    def contains(self, val):
        curr_node = self.root
        while curr_node:
            if val == curr_node.val:
                return True
            elif val < curr_node.val:
                curr_node = curr_node.left
            else:
                curr_node = curr_node.right
        return False

    def delete(self, val):
        def get_min_node(node):
            while node.left:
                node = node.left
            return node

        def delete_helper(node, val):
            if not node:
                return node
            if val < node.val:
                node.left = delete_helper(node.left, val)
            elif val > node.val:
                node.right = delete_helper(node.right, val)
            else:
                if not node.left:
                    return node.right
                if not node.right:
                    return node.left
                temp = get_min_node(node.right)
                node.val = temp.val
                node.right = delete_helper(node.right, temp.val)
            return node

        self.root = delete_helper(self.root, val)

    def postorder_traversal(self, node):
        if node:
            self.postorder_traversal(node.left)
            self.postorder_traversal(node.right)
            print(node.val, end=' ')

    def preorder_traversal(self, node):
        if node:
            print(node.val, end=' ')
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)

    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.val, end=' ')
            self.inorder_traversal(node.right)


bst = BinarySearchTree()

bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(2)
bst.insert(4)
bst.insert(6)
bst.insert(8)

print(bst.contains(4))  # True
print(bst.contains(9))  # False

bst.delete(3)

bst.postorder_traversal(bst.root)
print()

bst.preorder_traversal(bst.root)
print()

bst.inorder_traversal(bst.root)
print()
