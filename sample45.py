class Node:
    def __init__(self,val):
        self.left=None
        self.value=val
        self.right=None
class bintree:
    def createNode(self,data):
        return  Node(data)