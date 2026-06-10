from adjacencyMatrix import *


def floydMarshall(adjacencyMatrix):
    dist = [[0 for _ in range(len(adjacencyMatrix))]
            for _ in range(len(adjacencyMatrix))]
    dist = [row[:] for row in adjacencyMatrix]

    for i in range(len(adjacencyMatrix)):
        for j in range(len(adjacencyMatrix)):
            dist[i][j] = adjacencyMatrix[i][j]

    for k in range(len(adjacencyMatrix)):
        for i in range(len(adjacencyMatrix)):
            for j in range(len(adjacencyMatrix)):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist
