class graph:
    def __init__(self,nu_nod,edges):
        self.nu_nod=nu_nod
        self.data=[[] for _ in range(nu_nod)]
        for n1,n2 in edges:
            self.data[n1].append(n2)
            self.data[n2].append(n1)
nu_nods=5
edges=[(0,1),(0,4),(1,2),(1,4),(2,3),(3,4)]
g1=graph(nu_nods,edges)
print(g1.data)