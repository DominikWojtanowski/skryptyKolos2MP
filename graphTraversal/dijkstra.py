import heapq
import math
def dijkstra(adj, src):
    V = len(adj)

    pq = []

    dist = [math.inf] * V

    dist[src] = 0
    heapq.heappush(pq, (dist[src], src))

    while pq:
        d,u = heapq.heappop(pq)

        if dist[u] < d:
            continue

        for v,w in adj[u]:

            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                heapq.heappush((dist[v], v))

    return dist

