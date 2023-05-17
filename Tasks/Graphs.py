class Graph:
    def __init__(self, vertex, edge):
        self.E = set(frozenset((u, v)) for u, v in edge)
        self._nbrs = {}
        for v in vertex:
            self.add_vertex(v)
        for u, v in self.E:
            self.add_edge(u, v)

    def deg(self, vertex):
        return len(self._nbrs[vertex])

    def add_vertex(self, vertex):
        if vertex not in self._nbrs:
            self._nbrs[vertex] = set()

    def add_edge(self, u, v):
        self.add_vertex(u)
        self.add_vertex(v)
        self.E.add(frozenset([u, v]))
        self._nbrs[u].add(v)
        self._nbrs[v].add(u)

    def nbrs(self, vertex):
        return iter(self._nbrs[vertex])

    @property
    def m(self):
        return len(self.E)

    @property
    def n(self):
        return len(self._nbrs)

    def remove_edge(self, u, v):
        self.E.remove(frozenset([u, v]))
        self._nbrs[u].remove(v)
        self._nbrs[v].remove(u)

    def remove_vertex(self, u):
        to_delete = list(self.nbrs(u))
        for v in to_delete:
            self.remove_edge(u, v)
        del self._nbrs[u]


if __name__ == "__main__":
    g = Graph([1, 2, 3], {(1, 2), (2, 3)})
    assert(g.deg(1) == 1)
    assert (g.deg(2) == 2)
    assert (g.deg(3) == 1)
    print(g.deg(3))
    print(*g.nbrs(2))
    print("Good")




