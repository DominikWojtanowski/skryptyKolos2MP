import heapq
from adjacencyList import *
import math


def dijkstra(adj, src):
    dist = [math.inf] * len(adj)
    poprzednicy = [-1] * len(adj)
    dist[src] = 0

    pq = []
    for key in adj.keys():
        heapq.heappush(pq, (dist[key], key))

    while len(pq) > 0:
        d, u = heapq.heappop(pq)

        if dist[u] < d:
            continue

        for v, w in adj[u]:
            if dist[v] > d + w:
                dist[v] = d + w
                poprzednicy[v] = u
                heapq.heappush(pq, (dist[v], v))
