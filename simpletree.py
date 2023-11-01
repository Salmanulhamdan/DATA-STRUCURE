class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)


def build_tree():
    # Create the root node
    root = Node("A")

    # Add children to the root
    b = Node("B")
    c = Node("C")
    d = Node("D")
    e = Node("E")
    f = Node("F")
    root.add_child(b)
    root.add_child(c)
    root.add_child(d)
    root.add_child(e)
    root.add_child(f)

    # Add children to node B
    g = Node("G")
    h = Node("H")
    i = Node("I")
    b.add_child(g)
    b.add_child(h)
    b.add_child(i)

    # Add children to node C
    j = Node("J")
    c.add_child(j)

    return root


# Example usage
tree = build_tree()
print(tree.children[0].children[1].value)  # Output: "H"
