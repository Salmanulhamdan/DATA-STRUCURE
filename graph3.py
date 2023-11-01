class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def add_edge(self, v1, v2):
        if v1 in self.adj_list and v2 in self.adj_list:
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
        else:
            print("One or more vertices not found in graph.")

    def display(self):
        for vertex in self.adj_list:
            print(vertex, ":", self.adj_list[vertex])
d=Graph()
d.add_vertex(50)
d.add_vertex(80)
d.add_vertex(8)
d.add_vertex(9)
d.add_edge(50,80)
d.display()