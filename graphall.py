class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def add_edge(self, v1, v2):
        if v1 not in self.adj_list:
            self.adj_list[v1] = []
        if v2 not in self.adj_list:
            self.adj_list[v2] = []
        self.adj_list[v1].append(v2)
        self.adj_list[v2].append(v1)

    def remove_vertex(self, vertex):
        if vertex in self.adj_list:
            del self.adj_list[vertex]
            for adj_list in self.adj_list.values():
                if vertex in adj_list:
                    adj_list.remove(vertex)

    def remove_edge(self, v1, v2):
        if v1 in self.adj_list and v2 in self.adj_list:
            self.adj_list[v1].remove(v2)
            self.adj_list[v2].remove(v1)

    def is_cyclic(self):
        visited = set()
        for vertex in self.adj_list:
            if vertex not in visited:
                if self._is_cyclic_helper(vertex, visited, None):
                    return True
        return False

    def _is_cyclic_helper(self, vertex, visited, parent):
        visited.add(vertex)
        for adj_vertex in self.adj_list[vertex]:
            if adj_vertex not in visited:
                if self._is_cyclic_helper(adj_vertex, visited, vertex):
                    return True
            elif adj_vertex != parent:
                return True
        return False

    def bfs(self, start_vertex):
        visited = set()
        queue = [start_vertex]
        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                visited.add(vertex)
                print(vertex)
                for adj_vertex in self.adj_list[vertex]:
                    if adj_vertex not in visited:
                        queue.append(adj_vertex)

    def dfs(self, start_vertex):
        visited = set()
        self._dfs_helper(start_vertex, visited)

    def _dfs_helper(self, vertex, visited):
        visited.add(vertex)
        print(vertex)
        for adj_vertex in self.adj_list[vertex]:
            if adj_vertex not in visited:
                self._dfs_helper(adj_vertex, visited)


g = Graph()
g.add_vertex(1)
g.add_vertex(2)
g.add_vertex(3)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 1)

print(g.adj_list) # prints: {1: [2, 3], 2: [1, 3], 3: [2, 1]}

g.remove_edge(1, 2)
g.remove_vertex(2)

print(g.adj_list) # prints: {1: [3], 3: [1]}

print(g.is_cyclic()) # prints: True

g.bfs(1) # prints: 1 3
g.dfs(1) # prints: 1 3
