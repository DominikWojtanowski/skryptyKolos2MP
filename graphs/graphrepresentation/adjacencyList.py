class AdjacencyList:
    def __init__(self, numOfVertices):
        self.graph = dict()
        for i in range(numOfVertices):
            self.graph[i] = []

        self.numOfVertices = numOfVertices

    def addEdge(self, u, v, weight=1, isDirected=False):
        assert u >= 0 and u < self.numOfVertices and v >= 0 and v < self.numOfVertices
        self.graph[u].append((v, weight))

        if not isDirected:
            self.graph[v].append((u, weight))
