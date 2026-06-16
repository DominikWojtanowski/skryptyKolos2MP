import math

def bellmanFord(V, edges, src):
    dist = [math.inf] * V
    dist[src] = 0

    #edge to jest (od, do, src)
    for i in range(V):
        for edge in edges:
            u, v, wt = edge

            if dist[v] > dist[u] + wt:
                if i == V - 1:
                    return -1
                
                dist[v] = dist[u] + wt
    return dist