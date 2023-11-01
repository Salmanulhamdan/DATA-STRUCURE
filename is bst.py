# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.right = None
#         self.left = None
# def insert(root,data):
#     if root is None:
#         return Node(data)
#     if data < root.data:
#         root.left = insert(root.left, data)
#     if data >= root.data:
#         root.right = insert(root.right, data)
#     return root
#
#
# def traverse_inorder(root):
#     if root:
#         traverse_inorder(root.left)
#         print(root.data, end=' ')
#         traverse_inorder(root.right)
#
#
# root = None
# root = insert(root, 50)
#
#
# insert(root, 40)
# insert(root, 100)
# insert(root, 400)
# insert(root, 10)
#
#
# traverse_inorder(root)


#heap

# class Node:
#     def __init__(self):
#         self.heap = []
#
#
#     def insert(self, val):
#         self.heap.append(val)


# /d = sum(int(digit) ** 2 for digit in str(4))
# print(d)


b=[1,2,3,4,5]

a= len(b)-1
c=0
while c < a:
    b[a],b[c]=b[c],b[a]
    a=1
    c+=1
print(b)
print(b[::-1])
